import zipfile
from bs4 import BeautifulSoup
import flask
import werkzeug
import werkzeug.datastructures

import models


def safe_find(element: BeautifulSoup, tag: str):
    try:
        return element.find(tag)
    except AttributeError:
        return None


def open_file(
    file_path: str, file=None, type="S"
) -> str:  # S for standalone, F for flask
    if type == "S":
        file = file_path
    if file_path.endswith(".zip"):
        with zipfile.ZipFile(file, "r") as zip_ref:
            # read the only one xml file in the zip with functional proggramming
            file = BeautifulSoup(
                zip_ref.read(
                    list(filter(lambda x: x.endswith(".xml"), zip_ref.namelist()))[0]
                ),
                "xml",
            )
    elif file_path.endswith(".xml"):
        if type == "S":
            file = BeautifulSoup(open(file, "r", encoding="utf8"), "xml")
        else:
            file = BeautifulSoup(file.read(), "xml")
    else:
        raise ValueError("Invalid file type")
    if (file.find("Invoice") is not None) or (file.find("CreditNote") is not None):
        return str(file)
    return file.find("cac:Attachment").find("cbc:Description").text


def open_file_storage(
    file: werkzeug.datastructures.FileStorage,
) -> str:  # comming from flask
    return open_file(file.filename, file, "F")


def parse_invoice(xml_content: str) -> models.Invoice:
    soup = BeautifulSoup(xml_content, "xml")

    def get_text(element: BeautifulSoup, tag, default=""):
        try:
            found = safe_find(element, tag)
            return found.text if found else default
        except AttributeError:
            return default

    def parse_authorization_period(auth_period: BeautifulSoup):
        return models.AuthorizationPeriod(
            start_date=get_text(auth_period, "cbc:StartDate"),
            end_date=get_text(auth_period, "cbc:EndDate"),
        )

    def parse_authorized_invoices(auth_invoices: BeautifulSoup):
        return models.AuthorizedInvoices(
            prefix=get_text(auth_invoices, "sts:Prefix"),
            from_invoice=int(get_text(auth_invoices, "sts:From")),
            to_invoice=int(get_text(auth_invoices, "sts:To")),
        )

    def parse_invoice_control(invoice_control: BeautifulSoup):
        return models.InvoiceControl(
            invoice_authorization=get_text(invoice_control, "sts:InvoiceAuthorization"),
            authorization_period=parse_authorization_period(
                safe_find(invoice_control, "sts:AuthorizationPeriod")
            ),
            authorized_invoices=parse_authorized_invoices(
                safe_find(invoice_control, "sts:AuthorizedInvoices")
            ),
        )

    def parse_invoice_source(invoice_source: BeautifulSoup):
        return models.InvoiceSource(
            identification_code=get_text(invoice_source, "cbc:IdentificationCode")
        )

    def parse_software_provider(software_provider: BeautifulSoup):
        return models.SoftwareProvider(
            provider_id=get_text(software_provider, "sts:ProviderID"),
            software_id=get_text(software_provider, "sts:SoftwareID"),
        )

    def parse_authorization_provider(auth_provider: BeautifulSoup):
        return models.AuthorizationProvider(
            authorization_provider_id=get_text(
                auth_provider, "sts:AuthorizationProviderID"
            )
        )

    def parse_dian_extensions(dian_extensions: BeautifulSoup):
        return models.DianExtensions(
            invoice_control=parse_invoice_control(
                safe_find(dian_extensions, "sts:InvoiceControl")
            ),
            invoice_source=parse_invoice_source(
                safe_find(dian_extensions, "sts:InvoiceSource")
            ),
            software_provider=parse_software_provider(
                safe_find(dian_extensions, "sts:SoftwareProvider")
            ),
            software_security_code=get_text(
                dian_extensions, "sts:SoftwareSecurityCode"
            ),
            authorization_provider=parse_authorization_provider(
                safe_find(dian_extensions, "sts:AuthorizationProvider")
            ),
            qr_code=get_text(dian_extensions, "sts:QRCode"),
        )

    def parse_ubl_extensions(ubl_extensions: BeautifulSoup):
        extensions = []
        for ext in ubl_extensions.find_all("ext:UBLExtension"):
            if safe_find(ext, "sts:DianExtensions"):
                extensions.append(
                    models.UBLExtension(
                        dian_extensions=parse_dian_extensions(
                            safe_find(ext, "sts:DianExtensions")
                        )
                    )
                )
            elif safe_find(ext, "ds:Signature"):
                extensions.append(
                    models.UBLExtension(signature=get_text(ext, "ds:Signature"))
                )
        return extensions

    def parse_address(address_element: BeautifulSoup):
        return models.Address(
            id=get_text(address_element, "cbc:ID"),
            city_name=get_text(address_element, "cbc:CityName"),
            postal_zone=get_text(address_element, "cbc:PostalZone"),
            country_subentity=get_text(address_element, "cbc:CountrySubentity"),
            country_subentity_code=get_text(
                address_element, "cbc:CountrySubentityCode"
            ),
            line=get_text(safe_find(address_element, "cac:AddressLine"), "cbc:Line"),
            country_code=get_text(
                safe_find(address_element, "cac:Country"), "cbc:IdentificationCode"
            ),
            country_name=get_text(
                safe_find(address_element, "cac:Country"), "cbc:Name"
            ),
        )

    def parse_party_tax_scheme(party_tax_scheme_element: BeautifulSoup):
        return models.PartyTaxScheme(
            registration_name=get_text(
                party_tax_scheme_element, "cbc:RegistrationName"
            ),
            company_id=get_text(party_tax_scheme_element, "cbc:CompanyID"),
            tax_level_code=get_text(party_tax_scheme_element, "cbc:TaxLevelCode"),
            address=parse_address(
                safe_find(party_tax_scheme_element, "cac:RegistrationAddress")
            ),
            tax_scheme_id=get_text(
                safe_find(party_tax_scheme_element, "cac:TaxScheme"), "cbc:ID"
            ),
            tax_scheme_name=get_text(
                safe_find(party_tax_scheme_element, "cac:TaxScheme"), "cbc:Name"
            ),
        )

    def parse_party_legal_entity(party_legal_entity_element: BeautifulSoup):
        return models.PartyLegalEntity(
            registration_name=get_text(
                party_legal_entity_element, "cbc:RegistrationName"
            ),
            company_id=get_text(party_legal_entity_element, "cbc:CompanyID"),
            corporate_registration_id=get_text(
                safe_find(
                    party_legal_entity_element, "cac:CorporateRegistrationScheme"
                ),
                "cbc:ID",
                "",
            ),
        )

    def parse_contact(contact_element: BeautifulSoup):
        return models.Contact(
            telephone=get_text(contact_element, "cbc:Telephone"),
            email=get_text(contact_element, "cbc:ElectronicMail"),
        )

    def parse_party(party_element: BeautifulSoup):
        return models.Party(
            party_name=get_text(safe_find(party_element, "cac:PartyName"), "cbc:Name"),
            physical_location=parse_address(
                safe_find(
                    safe_find(party_element, "cac:PhysicalLocation"), "cac:Address"
                )
            ),
            party_tax_scheme=parse_party_tax_scheme(
                safe_find(party_element, "cac:PartyTaxScheme")
            ),
            party_legal_entity=parse_party_legal_entity(
                safe_find(party_element, "cac:PartyLegalEntity")
            ),
            contact=parse_contact(safe_find(party_element, "cac:Contact")),
        )

    def parse_accounting_supplier_party(supplier_element: BeautifulSoup):
        return models.AccountingSupplierParty(
            additional_account_id=get_text(supplier_element, "cbc:AdditionalAccountID"),
            party=parse_party(safe_find(supplier_element, "cac:Party")),
        )

    def parse_accounting_customer_party(customer_element: BeautifulSoup):
        return models.AccountingCustomerParty(
            additional_account_id=get_text(customer_element, "cbc:AdditionalAccountID"),
            party=parse_party(safe_find(customer_element, "cac:Party")),
        )

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
                get_text(
                    safe_find(invoice_line_element, "cac:TaxTotal"), "cbc:TaxAmount"
                )
            ),
            item_description=get_text(
                safe_find(invoice_line_element, "cac:Item"), "cbc:Description"
            ),
            item_id=get_text(
                safe_find(invoice_line_element, "cac:StandardItemIdentification"),
                "cbc:ID",
            ),
            price_amount=(
                get_text(
                    safe_find(invoice_line_element, "cac:Price"), "cbc:PriceAmount"
                )
            ),
            base_quantity=(
                get_text(
                    safe_find(invoice_line_element, "cac:Price"), "cbc:BaseQuantity"
                )
            ),
            allowance_charge=parse_allowance_charge(
                safe_find(invoice_line_element, "cac:AllowanceCharge")
            ),
        )

    def parse_allowance_charge(
        allowance_charge_element: BeautifulSoup,
    ):
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

    def parse_tax_total(tax_total_element: BeautifulSoup):
        return models.TaxTotal(
            tax_amount=(get_text(tax_total_element, "cbc:TaxAmount")),
            taxable_amount=(
                get_text(
                    safe_find(tax_total_element, "cac:TaxSubtotal"), "cbc:TaxableAmount"
                )
            ),
            tax_percentage=get_text(
                (
                    safe_find(
                        safe_find(tax_total_element, "cac:TaxSubtotal"),
                        "cac.TaxCategory",
                    )
                ),
                "cbc:Percent",
            ),
            tax_name=get_text(
                (
                    safe_find(
                        safe_find(
                            safe_find(tax_total_element, "cac:TaxSubtotal"),
                            "cac:TaxCategory",
                        ),
                        "cac:TaxScheme",
                    )
                ),
                "cbc:Name",
            ),
        )

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

    ubl_extensions = parse_ubl_extensions(safe_find(soup, "ext:UBLExtensions"))

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
            safe_find(soup, "cac:AccountingSupplierParty")
        ),
        accounting_customer_party=parse_accounting_customer_party(
            safe_find(soup, "cac:AccountingCustomerParty")
        ),
        tax_total=parse_tax_total(safe_find(soup, "cac:TaxTotal")),
        legal_monetary_total=parse_legal_monetary_total(
            safe_find(soup, "cac:LegalMonetaryTotal")
        ),
        invoice_lines=[
            parse_invoice_line(line)
            for line in soup.find_all("cac:InvoiceLine")
            + soup.find_all("cac:CreditNoteLine")
        ],
        allowance_charge=[
            parse_allowance_charge(ac) for ac in soup.find_all("cac:AllowanceCharge")
        ],
        ubl_extensions=ubl_extensions,
    )
