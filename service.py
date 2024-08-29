from bs4 import BeautifulSoup

import models


def none_allowed(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AttributeError:
            return None

    return wrapper


def parse_invoice(xml_content: str) -> models.Invoice:
    soup = BeautifulSoup(xml_content, "xml")

    def get_text(element: BeautifulSoup, tag, default=""):
        if element is None:
            return default
        try:
            return element.find(tag).text if element.find(tag) else default
        except AttributeError:
            return default

    @none_allowed
    def parse_authorization_period(auth_period: BeautifulSoup):
        return models.AuthorizationPeriod(
            start_date=get_text(auth_period, "cbc:StartDate"),
            end_date=get_text(auth_period, "cbc:EndDate"),
        )

    @none_allowed
    def parse_authorized_invoices(auth_invoices: BeautifulSoup):
        return models.AuthorizedInvoices(
            prefix=get_text(auth_invoices, "sts:Prefix"),
            from_invoice=int(get_text(auth_invoices, "sts:From")),
            to_invoice=int(get_text(auth_invoices, "sts:To")),
        )

    @none_allowed
    def parse_invoice_control(invoice_control: BeautifulSoup):
        return models.InvoiceControl(
            invoice_authorization=get_text(invoice_control, "sts:InvoiceAuthorization"),
            authorization_period=parse_authorization_period(
                invoice_control.find("sts:AuthorizationPeriod")
            ),
            authorized_invoices=parse_authorized_invoices(
                invoice_control.find("sts:AuthorizedInvoices")
            ),
        )

    @none_allowed
    def parse_invoice_source(invoice_source: BeautifulSoup):
        return models.InvoiceSource(
            identification_code=get_text(invoice_source, "cbc:IdentificationCode")
        )

    @none_allowed
    def parse_software_provider(software_provider: BeautifulSoup):
        return models.SoftwareProvider(
            provider_id=get_text(software_provider, "sts:ProviderID"),
            software_id=get_text(software_provider, "sts:SoftwareID"),
        )

    @none_allowed
    def parse_authorization_provider(auth_provider: BeautifulSoup):
        return models.AuthorizationProvider(
            authorization_provider_id=get_text(
                auth_provider, "sts:AuthorizationProviderID"
            )
        )

    @none_allowed
    def parse_dian_extensions(dian_extensions: BeautifulSoup):
        return models.DianExtensions(
            invoice_control=parse_invoice_control(
                dian_extensions.find("sts:InvoiceControl")
            ),
            invoice_source=parse_invoice_source(
                dian_extensions.find("sts:InvoiceSource")
            ),
            software_provider=parse_software_provider(
                dian_extensions.find("sts:SoftwareProvider")
            ),
            software_security_code=get_text(
                dian_extensions, "sts:SoftwareSecurityCode"
            ),
            authorization_provider=parse_authorization_provider(
                dian_extensions.find("sts:AuthorizationProvider")
            ),
            qr_code=get_text(dian_extensions, "sts:QRCode"),
        )

    @none_allowed
    def parse_ubl_extensions(ubl_extensions: BeautifulSoup):
        extensions = []
        for ext in ubl_extensions.find_all("ext:UBLExtension"):
            if ext.find("sts:DianExtensions"):
                extensions.append(
                    models.UBLExtension(
                        dian_extensions=parse_dian_extensions(
                            ext.find("sts:DianExtensions")
                        )
                    )
                )
            elif ext.find("ds:Signature"):
                extensions.append(
                    models.UBLExtension(signature=get_text(ext, "ds:Signature"))
                )
        return extensions

    @none_allowed
    def parse_address(address_element: BeautifulSoup):
        if address_element is None:
            return None
        return models.Address(
            id=get_text(address_element, "cbc:ID"),
            city_name=get_text(address_element, "cbc:CityName"),
            postal_zone=get_text(address_element, "cbc:PostalZone"),
            country_subentity=get_text(address_element, "cbc:CountrySubentity"),
            country_subentity_code=get_text(
                address_element, "cbc:CountrySubentityCode"
            ),
            line=get_text(address_element.find("cac:AddressLine"), "cbc:Line"),
            country_code=get_text(
                address_element.find("cac:Country"), "cbc:IdentificationCode"
            ),
            country_name=get_text(address_element.find("cac:Country"), "cbc:Name"),
        )

    @none_allowed
    def parse_party_tax_scheme(party_tax_scheme_element: BeautifulSoup):
        return models.PartyTaxScheme(
            registration_name=get_text(
                party_tax_scheme_element, "cbc:RegistrationName"
            ),
            company_id=get_text(party_tax_scheme_element, "cbc:CompanyID"),
            tax_level_code=get_text(party_tax_scheme_element, "cbc:TaxLevelCode"),
            address=parse_address(
                party_tax_scheme_element.find("cac:RegistrationAddress")
            ),
            tax_scheme_id=get_text(
                party_tax_scheme_element.find("cac:TaxScheme"), "cbc:ID"
            ),
            tax_scheme_name=get_text(
                party_tax_scheme_element.find("cac:TaxScheme"), "cbc:Name"
            ),
        )

    @none_allowed
    def parse_party_legal_entity(party_legal_entity_element: BeautifulSoup):
        return models.PartyLegalEntity(
            registration_name=get_text(
                party_legal_entity_element, "cbc:RegistrationName"
            ),
            company_id=get_text(party_legal_entity_element, "cbc:CompanyID"),
            corporate_registration_id=get_text(
                party_legal_entity_element.find("cac:CorporateRegistrationScheme"),
                "cbc:ID",
                "",
            ),
        )

    @none_allowed
    def parse_contact(contact_element: BeautifulSoup):
        return models.Contact(
            telephone=get_text(contact_element, "cbc:Telephone"),
            email=get_text(contact_element, "cbc:ElectronicMail"),
        )

    @none_allowed
    def parse_party(party_element: BeautifulSoup):
        p = models.Party(
            party_name=get_text(party_element.find("cac:PartyName"), "cbc:Name"),
            physical_location=parse_address(
                (
                    party_element.find("cac:PhysicalLocation").find("cac:Address")
                    if party_element.find("cac:PhysicalLocation")
                    else None
                )
            ),
            party_tax_scheme=parse_party_tax_scheme(
                party_element.find("cac:PartyTaxScheme")
            ),
            party_legal_entity=parse_party_legal_entity(
                party_element.find("cac:PartyLegalEntity")
            ),
            contact=parse_contact(party_element.find("cac:Contact")),
        )
        return p

    @none_allowed
    def parse_accounting_supplier_party(supplier_element: BeautifulSoup):
        return models.AccountingSupplierParty(
            additional_account_id=get_text(supplier_element, "cbc:AdditionalAccountID"),
            party=parse_party(supplier_element.find("cac:Party")),
        )

    @none_allowed
    def parse_accounting_customer_party(customer_element: BeautifulSoup):
        return models.AccountingCustomerParty(
            additional_account_id=get_text(customer_element, "cbc:AdditionalAccountID"),
            party=parse_party(customer_element.find("cac:Party")),
        )

    @none_allowed
    def parse_invoice_line(invoice_line_element: BeautifulSoup):
        notes = invoice_line_element.find_all("cbc:Note")
        notes_text = [get_text(note, "cbc:Note", default="") for note in notes]
        return models.InvoiceLine(
            id=int(get_text(invoice_line_element, "cbc:ID")),
            notes=notes_text,
            invoiced_quantity=(get_text(invoice_line_element, "cbc:InvoicedQuantity")),
            line_extension_amount=(
                get_text(invoice_line_element, "cbc:LineExtensionAmount")
            ),
            tax_total=(
                get_text(invoice_line_element.find("cac:TaxTotal"), "cbc:TaxAmount")
            ),
            item_description=get_text(
                invoice_line_element.find("cac:Item"), "cbc:Description"
            ),
            item_id=get_text(
                invoice_line_element.find("cac:StandardItemIdentification"), "cbc:ID"
            ),
            price_amount=(
                get_text(invoice_line_element.find("cac:Price"), "cbc:PriceAmount")
            ),
            base_quantity=(
                get_text(invoice_line_element.find("cac:Price"), "cbc:BaseQuantity")
            ),
            allowance_charge=parse_allowance_charge(
                invoice_line_element.find("cac:AllowanceCharge")
            ),
        )

    @none_allowed
    def parse_allowance_charge(
        allowance_charge_element: BeautifulSoup,
    ):  # descuentos, made by me
        return models.AllowanceCharge(
            charge_indicator=get_text(allowance_charge_element, "cbc:ChargeIndicator"),
            allowance_charge_reason=get_text(
                allowance_charge_element, "cbc:AllowanceChargeReason"
            ),
            multiplier_factor_numeric=get_text(
                allowance_charge_element, "cbc:MultiplierFactorNumeric"
            ),
            amount=get_text(allowance_charge_element, "cbc:Amount"),
            base_amount=get_text(allowance_charge_element, "cbc:BaseAmount"),
        )

    @none_allowed
    def parse_tax_total(tax_total_element: BeautifulSoup):
        return models.TaxTotal(
            tax_amount=(get_text(tax_total_element, "cbc:TaxAmount")),
            taxable_amount=(
                get_text(tax_total_element.find("cac:TaxSubtotal"), "cbc:TaxableAmount")
            ),
            tax_percentage=(
                get_text(
                    (
                        tax_total_element.find("cac:TaxSubtotal").find(
                            "cbc:TaxCategory"
                        )
                        if tax_total_element.find("cac:TaxSubtotal")
                        else None
                    ),
                    "cbc:Percent",
                )
            ),
            tax_name=get_text(
                tax_total_element.find("cac:TaxSubtotal")
                .find("cac:TaxCategory")
                .find("cac:TaxScheme"),
                "cbc:Name",
            ),
        )

    @none_allowed
    def parse_legal_monetary_total(legal_monetary_total_element: BeautifulSoup):
        return models.LegalMonetaryTotal(
            line_extension_amount=(
                get_text(legal_monetary_total_element, "cbc:LineExtensionAmount")
            ),
            tax_exclusive_amount=(
                get_text(legal_monetary_total_element, "cbc:TaxExclusiveAmount")
            ),
            tax_inclusive_amount=(
                get_text(legal_monetary_total_element, "cbc:TaxInclusiveAmount")
            ),
            allowance_total_amount=(
                get_text(legal_monetary_total_element, "cbc:AllowanceTotalAmount")
            ),
            charge_total_amount=(
                get_text(legal_monetary_total_element, "cbc:ChargeTotalAmount")
            ),
            payable_rounding_amount=(
                get_text(legal_monetary_total_element, "cbc:PayableRoundingAmount")
            ),
            payable_amount=(
                get_text(legal_monetary_total_element, "cbc:PayableAmount")
            ),
        )

    ubl_extensions = parse_ubl_extensions(soup.find("ext:UBLExtensions"))

    return models.Invoice(
        ubl_version_id=get_text(soup, "cbc:UBLVersionID"),
        customization_id=get_text(soup, "cbc:CustomizationID"),
        profile_id=get_text(soup, "cbc:ProfileID"),
        profile_execution_id=get_text(soup, "cbc:ProfileExecutionID"),
        id=get_text(soup, "cbc:ID"),
        uuid=get_text(soup, "cbc:UUID"),
        issue_date=get_text(soup, "cbc:IssueDate"),
        issue_time=get_text(soup, "cbc:IssueTime"),
        invoice_type_code=get_text(soup, "cbc:InvoiceTypeCode"),
        document_currency_code=get_text(soup, "cbc:DocumentCurrencyCode"),
        line_count_numeric=int(get_text(soup, "cbc:LineCountNumeric")),
        accounting_supplier_party=parse_accounting_supplier_party(
            soup.find("cac:AccountingSupplierParty")
        ),
        accounting_customer_party=parse_accounting_customer_party(
            soup.find("cac:AccountingCustomerParty")
        ),
        tax_total=parse_tax_total(soup.find("cac:TaxTotal")),
        legal_monetary_total=parse_legal_monetary_total(
            soup.find("cac:LegalMonetaryTotal")
        ),
        invoice_lines=[
            parse_invoice_line(line)
            for line in soup.find_all("cac:InvoiceLine")
            + soup.find_all("cac:CreditNoteLine")
        ],
        ubl_extensions=ubl_extensions,
    )
