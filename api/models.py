import logging
from typing import List, Optional
from dataclasses import dataclass


def nullable(func):
    def wrapper(obj):
        if obj is None:
            return None
        return func(obj)

    return wrapper


@dataclass
class ID:
    scheme_id: Optional[str]
    scheme_name: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "ID":
        if type(obj) is not dict:
            return ID(None, None, obj)
        _scheme_id = str(obj.get("@schemeID"))
        _scheme_name = str(obj.get("@schemeName"))
        _text = str(obj.get("#text"))
        return ID(_scheme_id, _scheme_name, _text)


@dataclass
class PartyIdentification:
    id: ID | str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "PartyIdentification":
        _id = ID.from_dict(obj.get("cbc:ID"))
        return PartyIdentification(_id)


@dataclass
class CompanyID:
    scheme_id: Optional[str]
    scheme_name: Optional[str]
    scheme_agency_id: Optional[str]
    scheme_agency_name: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "CompanyID":
        if type(obj) is not dict:
            return CompanyID(None, None, None, None, obj)
        _scheme_id = str(obj.get("@schemeID"))
        _scheme_name = str(obj.get("@schemeName"))
        _scheme_agency_id = str(obj.get("@schemeAgencyID"))
        _scheme_agency_name = str(obj.get("@schemeAgencyName"))
        _text = str(obj.get("#text"))
        return CompanyID(
            _scheme_id, _scheme_name, _scheme_agency_id, _scheme_agency_name, _text
        )


@dataclass
class CorporateRegistrationScheme:
    id: str
    name: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "CorporateRegistrationScheme":
        _id = str(obj.get("cbc:ID"))
        _name = str(obj.get("cbc:Name"))
        return CorporateRegistrationScheme(_id, _name)


@dataclass
class PartyLegalEntity:
    registration_name: str
    company_id: CompanyID
    corporate_registration_scheme: CorporateRegistrationScheme

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "PartyLegalEntity":
        _registration_name = str(obj.get("cbc:RegistrationName"))
        _company_id = CompanyID.from_dict(obj.get("cbc:CompanyID"))
        _corporate_registration_scheme = CorporateRegistrationScheme.from_dict(
            obj.get("cac:CorporateRegistrationScheme")
        )
        return PartyLegalEntity(
            _registration_name, _company_id, _corporate_registration_scheme
        )


@dataclass
class PartyName:
    name: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "PartyName":
        _name = str(obj.get("cbc:Name"))
        return PartyName(_name)


@dataclass
class TaxScheme:
    id: str
    name: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "TaxScheme":
        _id = str(obj.get("cbc:ID"))
        _name = str(obj.get("cbc:Name"))
        return TaxScheme(_id, _name)


@dataclass
class TaxLevelCode:
    list_name: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "TaxLevelCode":
        if type(obj) is not dict:
            return TaxLevelCode(None, obj)
        _list_name = str(obj.get("@listName"))
        _text = str(obj.get("#text"))
        return TaxLevelCode(_list_name, _text)


@dataclass
class Name:
    language_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "Name":
        if type(obj) is not dict:
            return Name(None, obj)
        _language_id = str(obj.get("@languageID"))
        _text = str(obj.get("#text"))
        return Name(_language_id, _text)


@dataclass
class Country:
    identification_code: str
    name: Name

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Country":
        _identification_code = str(obj.get("cbc:IdentificationCode"))
        _name = Name.from_dict(obj.get("cbc:Name"))
        return Country(_identification_code, _name)


@dataclass
class AddressLine:
    line: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "AddressLine":
        _line = str(obj.get("cbc:Line"))
        return AddressLine(_line)


@dataclass
class Address:
    id: str
    city_name: str
    postal_zone: str
    country_subentity: str
    country_subentity_code: str
    address_line: List[AddressLine]
    country: Country

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Address":
        _id = str(obj.get("cbc:ID"))
        _city_name = str(obj.get("cbc:CityName"))
        _postal_zone = str(obj.get("cbc:PostalZone"))
        _country_subentity = str(obj.get("cbc:CountrySubentity"))
        _country_subentity_code = str(obj.get("cbc:CountrySubentityCode"))
        _address_line = (
            [AddressLine.from_dict(y) for y in obj.get("cac:AddressLine")]
            if type(obj.get("cac:AddressLine")) is list
            else [AddressLine.from_dict(obj.get("cac:AddressLine"))]
        )
        _country = Country.from_dict(obj.get("cac:Country"))
        return Address(
            _id,
            _city_name,
            _postal_zone,
            _country_subentity,
            _country_subentity_code,
            _address_line,
            _country,
        )


@dataclass
class PartyTaxScheme:
    registration_name: str
    company_id: CompanyID
    tax_level_code: TaxLevelCode
    registration_address: Address
    tax_scheme: TaxScheme

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "PartyTaxScheme":
        _registration_name = str(obj.get("cbc:RegistrationName"))
        _company_id = CompanyID.from_dict(obj.get("cbc:CompanyID"))
        _tax_level_code = TaxLevelCode.from_dict(obj.get("cbc:TaxLevelCode"))
        _registration_address = Address.from_dict(
            obj.get("cac:RegistrationAddress")
        )
        _tax_scheme = TaxScheme.from_dict(obj.get("cac:TaxScheme"))
        return PartyTaxScheme(
            _registration_name,
            _company_id,
            _tax_level_code,
            _registration_address,
            _tax_scheme,
        )


@dataclass
class PhysicalLocation:
    name: str
    address: Address

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "PhysicalLocation":
        _name = str(obj.get("cbc:Name"))
        _address = Address.from_dict(obj.get("cac:Address"))
        return PhysicalLocation(_name, _address)


@dataclass
class Contact:
    telephone: str
    electronic_mail: str
    name: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Contact":
        _telephone = str(obj.get("cbc:Telephone"))
        _electronic_mail = str(obj.get("cbc:ElectronicMail"))
        _name = str(obj.get("cbc:Name"))
        return Contact(_telephone, _electronic_mail, _name)


@dataclass
class Person:
    first_name: str
    family_name: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Person":
        _first_name = str(obj.get("cbc:FirstName"))
        _family_name = str(obj.get("cbc:FamilyName"))
        return Person(_first_name, _family_name)


@dataclass
class Party:
    party_name: PartyName
    person: Person
    physical_location: PhysicalLocation
    party_tax_scheme: PartyTaxScheme
    party_legal_entity: PartyLegalEntity
    contact: Contact
    party_identification: PartyIdentification
    industry_classification_code: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Party":
        _party_name = PartyName.from_dict(obj.get("cac:PartyName"))
        _person = Person.from_dict(obj.get("cac:Person"))
        _physical_location = PhysicalLocation.from_dict(obj.get("cac:PhysicalLocation"))
        _party_tax_scheme = PartyTaxScheme.from_dict(obj.get("cac:PartyTaxScheme"))
        _party_legal_entity = PartyLegalEntity.from_dict(
            obj.get("cac:PartyLegalEntity")
        )
        _contact = Contact.from_dict(obj.get("cac:Contact"))
        _party_identification = PartyIdentification.from_dict(
            obj.get("cac:PartyIdentification")
        )
        _industry_classification_code = str(obj.get("cbc:IndustryClassificationCode"))
        return Party(
            _party_name,
            _person,
            _physical_location,
            _party_tax_scheme,
            _party_legal_entity,
            _contact,
            _party_identification,
            _industry_classification_code,
        )


@dataclass
class AccountingCustomerParty:
    additional_account_id: str
    party: Party

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "AccountingCustomerParty":
        _additional_account_id = str(obj.get("cbc:AdditionalAccountID"))
        _party = Party.from_dict(obj.get("cac:Party"))
        return AccountingCustomerParty(_additional_account_id, _party)


@dataclass
class AccountingSupplierParty:
    additional_account_id: str
    party: Party

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "AccountingSupplierParty":
        _additional_account_id = str(obj.get("cbc:AdditionalAccountID"))
        _party = Party.from_dict(obj.get("cac:Party"))
        return AccountingSupplierParty(_additional_account_id, _party)


@dataclass
class Amount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "Amount":
        if type(obj) is not dict:
            return Amount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return Amount(_currency_id, _text)


@dataclass
class BaseAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "BaseAmount":
        if type(obj) is not dict:
            return BaseAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return BaseAmount(_currency_id, _text)


@dataclass
class AllowanceCharge:
    id: str
    charge_indicator: str
    multiplier_factor_numeric: str
    amount: Amount
    base_amount: BaseAmount

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "AllowanceCharge":
        _id = str(obj.get("cbc:ID"))
        _charge_indicator = str(obj.get("cbc:ChargeIndicator"))
        _multiplier_factor_numeric = str(obj.get("cbc:MultiplierFactorNumeric"))
        _amount = Amount.from_dict(obj.get("cbc:Amount"))
        _base_amount = BaseAmount.from_dict(obj.get("cbc:BaseAmount"))
        return AllowanceCharge(
            _id, _charge_indicator, _multiplier_factor_numeric, _amount, _base_amount
        )


@dataclass
class Note:
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "Note":
        if type(obj) is not dict:
            return Note(obj)
        _text = str(obj.get("#text"))
        return Note(_text)


@dataclass
class InvoicedQuantity:
    unit_code: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "InvoicedQuantity":
        if type(obj) is not dict:
            return InvoicedQuantity(None, obj)
        _unit_code = str(obj.get("@unitCode"))
        _text = str(obj.get("#text"))
        return InvoicedQuantity(_unit_code, _text)


@dataclass
class LineExtensionAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "LineExtensionAmount":
        if type(obj) is not dict:
            return LineExtensionAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return LineExtensionAmount(_currency_id, _text)


@dataclass
class TaxAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "TaxAmount":
        if type(obj) is not dict:
            return TaxAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return TaxAmount(_currency_id, _text)


@dataclass
class TaxCategory:
    percent: str
    tax_scheme: TaxScheme

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "TaxCategory":
        _percent = str(obj.get("cbc:Percent"))
        _tax_scheme = TaxScheme.from_dict(obj.get("cac:TaxScheme"))
        return TaxCategory(_percent, _tax_scheme)


@dataclass
class TaxableAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "TaxableAmount":
        if type(obj) is not dict:
            return TaxableAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return TaxableAmount(_currency_id, _text)


@dataclass
class TaxSubtotal:
    taxable_amount: TaxableAmount
    tax_amount: TaxAmount
    tax_category: TaxCategory

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "TaxSubtotal":
        _taxable_amount = TaxableAmount.from_dict(obj.get("cbc:TaxableAmount"))
        _tax_amount = TaxAmount.from_dict(obj.get("cbc:TaxAmount"))
        _tax_category = TaxCategory.from_dict(obj.get("cac:TaxCategory"))
        return TaxSubtotal(_taxable_amount, _tax_amount, _tax_category)


@dataclass
class TaxTotal:
    tax_amount: TaxAmount
    tax_subtotal: TaxSubtotal
    tax_rounding_amount: TaxAmount  # It's the same implementation as TaxAmount

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "TaxTotal":
        _tax_amount = TaxAmount.from_dict(obj.get("cbc:TaxAmount"))
        _tax_subtotal = TaxSubtotal.from_dict(obj.get("cac:TaxSubtotal"))
        _tax_rounding_amount = TaxAmount.from_dict(obj.get("cbc:TaxAmount"))
        return TaxTotal(_tax_amount, _tax_subtotal, _tax_rounding_amount)


@dataclass
class StandardItemIdentification:
    id: ID

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "StandardItemIdentification":
        _id = ID.from_dict(obj.get("cbc:ID"))
        return StandardItemIdentification(_id)


@dataclass
class Item:
    description: str
    standard_item_identification: StandardItemIdentification
    sellers_item_identification: StandardItemIdentification
    brand_name: str
    pack_size_numeric: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Item":
        _description = str(obj.get("cbc:Description"))
        _standard_item_identification = StandardItemIdentification.from_dict(
            obj.get("cac:StandardItemIdentification")
        )
        _sellers_item_identification = StandardItemIdentification.from_dict(
            obj.get("cac:SellersItemIdentification")
        )
        _brand_name = str(obj.get("cbc:BrandName"))
        _pack_size_numeric = str(obj.get("cbc:PackSizeNumeric"))

        return Item(
            _description,
            _standard_item_identification,
            _sellers_item_identification,
            _brand_name,
            _pack_size_numeric,
        )


@dataclass
class PriceAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "PriceAmount":
        if type(obj) is not dict:
            return PriceAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return PriceAmount(_currency_id, _text)


@dataclass
class BaseQuantity:
    unit_code: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "BaseQuantity":
        if type(obj) is not dict:
            return BaseQuantity(None, obj)
        _unit_code = str(obj.get("@unitCode"))
        _text = str(obj.get("#text"))
        return BaseQuantity(_unit_code, _text)


@dataclass
class Price:
    price_amount: PriceAmount
    base_quantity: BaseQuantity

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Price":
        _price_amount = PriceAmount.from_dict(obj.get("cbc:PriceAmount"))
        _base_quantity = BaseQuantity.from_dict(obj.get("cbc:BaseQuantity"))
        return Price(_price_amount, _base_quantity)


@dataclass
class InvoiceLine:
    id: str
    note: List[Note]
    invoiced_quantity: InvoicedQuantity
    line_extension_amount: LineExtensionAmount
    allowance_charge: AllowanceCharge
    tax_total: TaxTotal
    item: Item
    price: Price

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "InvoiceLine":
        _id = str(obj.get("cbc:ID"))
        _note = (
            [Note.from_dict(y) for y in obj.get("cbc:Note", {})]
            if type(obj.get("cbc:Note")) is list
            else [Note.from_dict(obj.get("cbc:Note"))]
        )
        _invoiced_quantity = InvoicedQuantity.from_dict(obj.get("cbc:InvoicedQuantity"))
        _line_extension_amount = LineExtensionAmount.from_dict(
            obj.get("cbc:LineExtensionAmount")
        )
        _allowance_charge = AllowanceCharge.from_dict(obj.get("cac:AllowanceCharge"))
        _tax_total = TaxTotal.from_dict(obj.get("cac:TaxTotal"))
        _item = Item.from_dict(obj.get("cac:Item"))
        _price = Price.from_dict(obj.get("cac:Price"))
        return InvoiceLine(
            _id,
            _note,
            _invoiced_quantity,
            _line_extension_amount,
            _allowance_charge,
            _tax_total,
            _item,
            _price,
        )


@dataclass
class PaymentMeans:
    id: str
    payment_means_code: str
    payment_due_date: str
    payment_id: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "PaymentMeans":
        _id = str(obj.get("cbc:ID"))
        _payment_means_code = str(obj.get("cbc:PaymentMeansCode"))
        _payment_due_date = str(obj.get("cbc:PaymentDueDate"))
        _payment_id = str(obj.get("cbc:PaymentID"))

        return PaymentMeans(_id, _payment_means_code, _payment_due_date, _payment_id)


@dataclass
class AllowanceTotalAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "AllowanceTotalAmount":
        if type(obj) is not dict:
            return AllowanceTotalAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return AllowanceTotalAmount(_currency_id, _text)


@dataclass
class ChargeTotalAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "ChargeTotalAmount":
        if type(obj) is not dict:
            return ChargeTotalAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return ChargeTotalAmount(_currency_id, _text)


@dataclass
class IdentificationCode:
    list_agency_id: Optional[str]
    list_agency_name: Optional[str]
    list_scheme_uri: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "IdentificationCode":
        if type(obj) is not dict:
            return IdentificationCode(None, None, None, obj)
        _list_agency_id = str(obj.get("@listAgencyID"))
        _list_agency_name = str(obj.get("@listAgencyName"))
        _list_scheme_uri = str(obj.get("@listSchemeURI"))
        _text = str(obj.get("#text"))
        return IdentificationCode(
            _list_agency_id, _list_agency_name, _list_scheme_uri, _text
        )


@dataclass
class PayableAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "PayableAmount":
        if type(obj) is not dict:
            return PayableAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return PayableAmount(_currency_id, _text)


@dataclass
class PayableRoundingAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "PayableRoundingAmount":
        if type(obj) is not dict:
            return PayableRoundingAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return PayableRoundingAmount(_currency_id, _text)


@dataclass
class TaxExclusiveAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "TaxExclusiveAmount":
        if type(obj) is not dict:
            return TaxExclusiveAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return TaxExclusiveAmount(_currency_id, _text)


@dataclass
class TaxInclusiveAmount:
    currency_id: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "TaxInclusiveAmount":
        if type(obj) is not dict:
            return TaxInclusiveAmount(None, obj)
        _currency_id = str(obj.get("@currencyID"))
        _text = str(obj.get("#text"))
        return TaxInclusiveAmount(_currency_id, _text)


@dataclass
class UUID:
    scheme_id: Optional[str]
    scheme_name: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "UUID":
        if type(obj) is not dict:
            return UUID(None, None, obj)
        _scheme_id = str(obj.get("@schemeID"))
        _scheme_name = str(obj.get("@schemeName"))
        _text = str(obj.get("#text"))
        return UUID(_scheme_id, _scheme_name, _text)


@dataclass
class LegalMonetaryTotal:
    line_extension_amount: LineExtensionAmount
    tax_exclusive_amount: TaxExclusiveAmount
    tax_inclusive_amount: TaxInclusiveAmount
    allowance_total_amount: AllowanceTotalAmount
    charge_total_amount: ChargeTotalAmount
    payable_rounding_amount: PayableRoundingAmount
    payable_amount: PayableAmount

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "LegalMonetaryTotal":
        _line_extension_amount = LineExtensionAmount.from_dict(
            obj.get("cbc:LineExtensionAmount")
        )
        _tax_exclusive_amount = TaxExclusiveAmount.from_dict(
            obj.get("cbc:TaxExclusiveAmount")
        )
        _tax_inclusive_amount = TaxInclusiveAmount.from_dict(
            obj.get("cbc:TaxInclusiveAmount")
        )
        _allowance_total_amount = AllowanceTotalAmount.from_dict(
            obj.get("cbc:AllowanceTotalAmount")
        )
        _charge_total_amount = ChargeTotalAmount.from_dict(
            obj.get("cbc:ChargeTotalAmount")
        )
        _payable_rounding_amount = PayableRoundingAmount.from_dict(
            obj.get("cbc:PayableRoundingAmount")
        )
        _payable_amount = PayableAmount.from_dict(obj.get("cbc:PayableAmount"))
        return LegalMonetaryTotal(
            _line_extension_amount,
            _tax_exclusive_amount,
            _tax_inclusive_amount,
            _allowance_total_amount,
            _charge_total_amount,
            _payable_rounding_amount,
            _payable_amount,
        )


@dataclass
class DsCanonicalizationMethod:
    algorithm: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsCanonicalizationMethod":
        _algorithm = str(obj.get("@Algorithm"))
        return DsCanonicalizationMethod(_algorithm)


@dataclass
class DsDigestMethod:
    algorithm: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsDigestMethod":
        _algorithm = str(obj.get("@Algorithm"))
        return DsDigestMethod(_algorithm)


@dataclass
class DsRSAKeyValue:
    modulus: str
    exponent: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsRSAKeyValue":
        _modulus = str(obj.get("ds:Modulus"))
        _exponent = str(obj.get("ds:Exponent"))
        return DsRSAKeyValue(_modulus, _exponent)


@dataclass
class DsKeyValue:
    rsa_key_value: DsRSAKeyValue

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsKeyValue":
        _rsa_key_value = DsRSAKeyValue.from_dict(obj.get("ds:RSAKeyValue"))
        return DsKeyValue(_rsa_key_value)


@dataclass
class DsX509Data:
    x509_certificate: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsX509Data":
        _x509_certificate = str(obj.get("ds:X509Certificate"))
        return DsX509Data(_x509_certificate)


@dataclass
class DsKeyInfo:
    id: str
    x509_data: DsX509Data
    key_value: DsKeyValue

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsKeyInfo":
        _id = str(obj.get("@Id"))
        _x509_data = DsX509Data.from_dict(obj.get("ds:X509Data"))
        _key_value = DsKeyValue.from_dict(obj.get("ds:KeyValue"))
        return DsKeyInfo(_id, _x509_data, _key_value)


@dataclass
class XadesSigPolicyId:
    xades_identifier: str
    xades_description: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesSigPolicyId":
        _xades_identifier = str(obj.get("xades:Identifier"))
        _xades_description = str(obj.get("xades:Description"))
        return XadesSigPolicyId(_xades_identifier, _xades_description)


@dataclass
class XadesSigPolicyHash:
    digest_method: DsDigestMethod
    digest_value: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesSigPolicyHash":
        _digest_method = DsDigestMethod.from_dict(obj.get("ds:DigestMethod"))
        _digest_value = str(obj.get("ds:DigestValue"))
        return XadesSigPolicyHash(_digest_method, _digest_value)


@dataclass
class XadesSignaturePolicyId:
    xades_sig_policy_id: XadesSigPolicyId
    xades_sig_policy_hash: XadesSigPolicyHash

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesSignaturePolicyId":
        _xades_sig_policy_id = XadesSigPolicyId.from_dict(obj.get("xades:SigPolicyId"))
        _xades_sig_policy_hash = XadesSigPolicyHash.from_dict(
            obj.get("xades:SigPolicyHash")
        )
        return XadesSignaturePolicyId(_xades_sig_policy_id, _xades_sig_policy_hash)


@dataclass
class XadesSignaturePolicyIdentifier:
    xades_signature_policy_id: XadesSignaturePolicyId

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesSignaturePolicyIdentifier":
        _xades_signature_policy_id = XadesSignaturePolicyId.from_dict(
            obj.get("xades:SignaturePolicyId")
        )
        return XadesSignaturePolicyIdentifier(_xades_signature_policy_id)


@dataclass
class XadesClaimedRoles:
    xades_claimed_role: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesClaimedRoles":
        _xades_claimed_role = str(obj.get("xades:ClaimedRole"))
        return XadesClaimedRoles(_xades_claimed_role)


@dataclass
class XadesSignerRole:
    xades_claimed_roles: XadesClaimedRoles

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesSignerRole":
        _xades_claimed_roles = XadesClaimedRoles.from_dict(
            obj.get("xades:ClaimedRoles")
        )
        return XadesSignerRole(_xades_claimed_roles)


@dataclass
class XadesCertDigest:
    digest_method: DsDigestMethod
    digest_value: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesCertDigest":
        _digest_method = DsDigestMethod.from_dict(obj.get("ds:DigestMethod"))
        _digest_value = str(obj.get("ds:DigestValue"))
        return XadesCertDigest(_digest_method, _digest_value)


@dataclass
class XadesIssuerSerial:
    x509_issuer_name: str
    x509_serial_number: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesIssuerSerial":
        _x509_issuer_name = str(obj.get("ds:X509IssuerName"))
        _x509_serial_number = str(obj.get("ds:X509SerialNumber"))
        return XadesIssuerSerial(_x509_issuer_name, _x509_serial_number)


@dataclass
class XadesCert:
    xades_cert_digest: XadesCertDigest
    xades_issuer_serial: XadesIssuerSerial

    @nullable
    @staticmethod
    def from_dict(obj: dict | list | None) -> "XadesCert":
        if type(obj) is list:
            obj = obj[0]
        _xades_cert_digest = XadesCertDigest.from_dict(obj.get("xades:CertDigest"))
        _xades_issuer_serial = XadesIssuerSerial.from_dict(
            obj.get("xades:IssuerSerial")
        )
        return XadesCert(_xades_cert_digest, _xades_issuer_serial)


@dataclass
class XadesSigningCertificate:
    xades_cert: XadesCert

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesSigningCertificate":
        _xades_cert = XadesCert.from_dict(obj.get("xades:Cert"))
        return XadesSigningCertificate(_xades_cert)


@dataclass
class XadesSignedSignatureProperties:
    xades_signing_time: str
    xades_signing_certificate: XadesSigningCertificate
    xades_signature_policy_identifier: XadesSignaturePolicyIdentifier
    xades_signer_role: XadesSignerRole

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesSignedSignatureProperties":
        _xades_signing_time = str(obj.get("xades:SigningTime"))
        _xades_signing_certificate = XadesSigningCertificate.from_dict(
            obj.get("xades:SigningCertificate")
        )
        _xades_signature_policy_identifier = XadesSignaturePolicyIdentifier.from_dict(
            obj.get("xades:SignaturePolicyIdentifier")
        )
        _xades_signer_role = XadesSignerRole.from_dict(obj.get("xades:SignerRole"))
        return XadesSignedSignatureProperties(
            _xades_signing_time,
            _xades_signing_certificate,
            _xades_signature_policy_identifier,
            _xades_signer_role,
        )


@dataclass
class XadesSignedProperties:
    id: str
    xades_signed_signature_properties: XadesSignedSignatureProperties

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesSignedProperties":
        _id = str(obj.get("@Id"))
        _xades_signed_signature_properties = XadesSignedSignatureProperties.from_dict(
            obj.get("xades:SignedSignatureProperties")
        )
        return XadesSignedProperties(_id, _xades_signed_signature_properties)


@dataclass
class XadesQualifyingProperties:
    xmlnsxades: str
    target: str
    id: str
    xades_signed_properties: XadesSignedProperties

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "XadesQualifyingProperties":
        _xmlnsxades = str(obj.get("@xmlns:xades"))
        _target = str(obj.get("@Target"))
        _id = str(obj.get("@Id"))
        _xades_signed_properties = XadesSignedProperties.from_dict(
            obj.get("xades:SignedProperties")
        )
        return XadesQualifyingProperties(
            _xmlnsxades, _target, _id, _xades_signed_properties
        )


@dataclass
class DsObject:
    xades_qualifying_properties: XadesQualifyingProperties

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsObject":
        _xades_qualifying_properties = XadesQualifyingProperties.from_dict(
            obj.get("xades:QualifyingProperties")
        )
        return DsObject(_xades_qualifying_properties)


@dataclass
class DsTransform:
    algorithm: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsTransform":
        _algorithm = str(obj.get("@Algorithm"))
        return DsTransform(_algorithm)


@dataclass
class DsTransforms:
    transform: DsTransform

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsTransforms":
        _transform = DsTransform.from_dict(obj.get("ds:Transform"))
        return DsTransforms(_transform)


@dataclass
class DsReference:
    id: str
    URI: str
    transforms: DsTransforms
    digest_method: DsDigestMethod
    digest_value: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsReference":
        _id = str(obj.get("@Id"))
        _URI = str(obj.get("@URI"))
        _transforms = DsTransforms.from_dict(obj.get("ds:Transforms"))
        _digest_method = DsDigestMethod.from_dict(obj.get("ds:DigestMethod"))
        _digest_value = str(obj.get("ds:DigestValue"))
        return DsReference(_id, _URI, _transforms, _digest_method, _digest_value)


@dataclass
class DsSignatureMethod:
    algorithm: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsSignatureMethod":
        _algorithm = str(obj.get("@Algorithm"))
        return DsSignatureMethod(_algorithm)


@dataclass
class DsSignedInfo:
    canonicalization_method: DsCanonicalizationMethod
    signature_method: DsSignatureMethod
    reference: List[DsReference]

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsSignedInfo":
        _canonicalization_method = DsCanonicalizationMethod.from_dict(
            obj.get("ds:CanonicalizationMethod")
        )
        _signature_method = DsSignatureMethod.from_dict(obj.get("ds:SignatureMethod"))
        _reference = [DsReference.from_dict(y) for y in obj.get("ds:Reference", {})]
        return DsSignedInfo(_canonicalization_method, _signature_method, _reference)


@dataclass
class DsSignature:
    xmlnsds: str
    id: str
    signed_info: DsSignedInfo
    signature_value: str
    key_info: DsKeyInfo
    object: DsObject

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "DsSignature":
        _xmlnsds = str(obj.get("@xmlns:ds"))
        _id = str(obj.get("@Id"))
        _signed_info = DsSignedInfo.from_dict(obj.get("ds:SignedInfo"))
        _signature_value = str(obj.get("ds:SignatureValue"))
        _key_info = DsKeyInfo.from_dict(obj.get("ds:KeyInfo"))
        _object = DsObject.from_dict(obj.get("ds:Object"))
        return DsSignature(
            _xmlnsds, _id, _signed_info, _signature_value, _key_info, _object
        )


@dataclass
class StsAuthorizationPeriod:
    start_date: str
    end_date: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "StsAuthorizationPeriod":
        _start_date = str(obj.get("cbc:StartDate"))
        _end_date = str(obj.get("cbc:EndDate"))
        return StsAuthorizationPeriod(_start_date, _end_date)


@dataclass
class StsAuthorizationProviderID:
    scheme_agency_id: Optional[str]
    scheme_agency_name: Optional[str]
    scheme_id: Optional[str]
    scheme_name: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "StsAuthorizationProviderID":
        if type(obj) is not dict:
            return StsAuthorizationProviderID(None, None, None, None, obj)
        _scheme_agency_id = str(obj.get("@schemeAgencyID"))
        _scheme_agency_name = str(obj.get("@schemeAgencyName"))
        _scheme_id = str(obj.get("@schemeID"))
        _scheme_name = str(obj.get("@schemeName"))
        _text = str(obj.get("#text"))
        return StsAuthorizationProviderID(
            _scheme_agency_id, _scheme_agency_name, _scheme_id, _scheme_name, _text
        )


@dataclass
class StsAuthorizationProvider:
    authorization_provider_id: StsAuthorizationProviderID

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "StsAuthorizationProvider":
        _sts_authorization_provider_id = StsAuthorizationProviderID.from_dict(
            obj.get("sts:AuthorizationProviderID")
        )
        return StsAuthorizationProvider(_sts_authorization_provider_id)


@dataclass
class StsAuthorizedInvoices:
    prefix: str
    stsfrom: str
    to: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "StsAuthorizedInvoices":
        _sts_prefix = str(obj.get("sts:Prefix"))
        _sts_from = str(obj.get("sts:From"))
        _sts_to = str(obj.get("sts:To"))
        return StsAuthorizedInvoices(_sts_prefix, _sts_from, _sts_to)


@dataclass
class StsInvoiceControl:
    invoice_authorization: str
    authorization_period: StsAuthorizationPeriod
    authorized_invoices: StsAuthorizedInvoices

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "StsInvoiceControl":
        _sts_invoice_authorization = str(obj.get("sts:InvoiceAuthorization"))
        _sts_authorization_period = StsAuthorizationPeriod.from_dict(
            obj.get("sts:AuthorizationPeriod")
        )
        _sts_authorized_invoices = StsAuthorizedInvoices.from_dict(
            obj.get("sts:AuthorizedInvoices")
        )
        return StsInvoiceControl(
            _sts_invoice_authorization,
            _sts_authorization_period,
            _sts_authorized_invoices,
        )


@dataclass
class StsInvoiceSource:
    identification_code: IdentificationCode

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "StsInvoiceSource":
        _identification_code = IdentificationCode.from_dict(
            obj.get("cbc:IdentificationCode")
        )
        return StsInvoiceSource(_identification_code)


@dataclass
class StsProviderID:
    scheme_agency_id: Optional[str]
    scheme_agency_name: Optional[str]
    scheme_id: Optional[str]
    scheme_name: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "StsProviderID":
        if type(obj) is not dict:
            return StsProviderID(None, None, None, None, obj)
        _scheme_agency_id = str(obj.get("@schemeAgencyID"))
        _scheme_agency_name = str(obj.get("@schemeAgencyName"))
        _scheme_id = str(obj.get("@schemeID"))
        _scheme_name = str(obj.get("@schemeName"))
        _text = str(obj.get("#text"))
        return StsProviderID(
            _scheme_agency_id, _scheme_agency_name, _scheme_id, _scheme_name, _text
        )


@dataclass
class StsSoftwareID:
    scheme_agency_id: Optional[str]
    scheme_agency_name: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "StsSoftwareID":
        if type(obj) is not dict:
            return StsSoftwareID(None, None, obj)
        _scheme_agency_id = str(obj.get("@schemeAgencyID"))
        _scheme_agency_name = str(obj.get("@schemeAgencyName"))
        _text = str(obj.get("#text"))
        return StsSoftwareID(_scheme_agency_id, _scheme_agency_name, _text)


@dataclass
class StsSoftwareProvider:
    provider_id: StsProviderID
    software_id: StsSoftwareID

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "StsSoftwareProvider":
        _sts_provider_id = StsProviderID.from_dict(obj.get("sts:ProviderID"))
        _sts_software_id = StsSoftwareID.from_dict(obj.get("sts:SoftwareID"))
        return StsSoftwareProvider(_sts_provider_id, _sts_software_id)


@dataclass
class StsSoftwareSecurityCode:
    scheme_agency_id: Optional[str]
    scheme_agency_name: Optional[str]
    text: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | str | None) -> "StsSoftwareSecurityCode":
        if type(obj) is not dict:
            return StsSoftwareSecurityCode(None, None, obj)
        _scheme_agency_id = str(obj.get("@schemeAgencyID"))
        _scheme_agency_name = str(obj.get("@schemeAgencyName"))
        _text = str(obj.get("#text"))
        return StsSoftwareSecurityCode(_scheme_agency_id, _scheme_agency_name, _text)


@dataclass
class StsDianExtensions:
    invoice_control: StsInvoiceControl
    invoice_source: StsInvoiceSource
    software_provider: StsSoftwareProvider
    software_security_code: StsSoftwareSecurityCode
    authorization_provider: StsAuthorizationProvider
    qr_code: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "StsDianExtensions":
        _sts_invoice_control = StsInvoiceControl.from_dict(
            obj.get("sts:InvoiceControl")
        )
        _sts_invoice_source = StsInvoiceSource.from_dict(obj.get("sts:InvoiceSource"))
        _sts_software_provider = StsSoftwareProvider.from_dict(
            obj.get("sts:SoftwareProvider")
        )
        _sts_software_security_code = StsSoftwareSecurityCode.from_dict(
            obj.get("sts:SoftwareSecurityCode")
        )
        _sts_authorization_provider = StsAuthorizationProvider.from_dict(
            obj.get("sts:AuthorizationProvider")
        )
        _sts_qr_code = str(obj.get("sts:QRCode"))
        return StsDianExtensions(
            _sts_invoice_control,
            _sts_invoice_source,
            _sts_software_provider,
            _sts_software_security_code,
            _sts_authorization_provider,
            _sts_qr_code,
        )


@dataclass
class ExtExtensionContent:
    dian_extensions: StsDianExtensions
    signature: DsSignature

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "ExtExtensionContent":
        _dian_extensions = StsDianExtensions.from_dict(obj.get("sts:DianExtensions"))
        _signature = DsSignature.from_dict(obj.get("ds:Signature"))
        return ExtExtensionContent(_dian_extensions, _signature)


@dataclass
class ExtUBLExtension:
    ext_extension_content: ExtExtensionContent

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "ExtUBLExtension":
        _ext_extension_content = ExtExtensionContent.from_dict(
            obj.get("ext:ExtensionContent")
        )
        return ExtUBLExtension(_ext_extension_content)


@dataclass
class ExtUBLExtensions:
    ext_ubl_extension: List[ExtUBLExtension]

    @nullable
    @staticmethod
    def from_dict(obj: dict) -> "ExtUBLExtensions":
        _ext_ubl_extension = [
            ExtUBLExtension.from_dict(y) for y in obj.get("ext:UBLExtension", {})
        ]
        return ExtUBLExtensions(_ext_ubl_extension)


@dataclass
class Delivery:
    actual_delivery_date: str
    actual_delivery_time: str
    delivery_address: Address

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Delivery":
        _actual_delivery_date = str(obj.get("cbc:ActualDeliveryDate"))
        _actual_delivery_time = str(obj.get("cbc:ActualDeliveryTime"))
        _delivery_address = Address.from_dict(obj.get("cac:DeliveryAddress"))
        return Delivery(_actual_delivery_date, _actual_delivery_time, _delivery_address)


@dataclass
class OrderReference:
    id: str
    issue_date: str

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "OrderReference":
        _id = str(obj.get("cbc:ID"))
        _issue_date = str(obj.get("cbc:IssueDate"))
        return OrderReference(_id, _issue_date)


@dataclass
class Invoice:
    ext_ubl_extensions: ExtUBLExtensions
    ubl_version_id: str
    customization_id: str
    profile_id: str
    profile_execution_id: str
    id: ID
    UUID: UUID
    issue_date: str
    issue_time: str
    invoice_type_code: str
    note: List[Note]
    document_currency_code: str
    delivery: Delivery
    line_count_numeric: str
    accounting_supplier_party: AccountingSupplierParty
    accounting_customer_party: AccountingCustomerParty
    order_reference: OrderReference
    payment_means: PaymentMeans
    tax_total: TaxTotal
    legal_monetary_total: LegalMonetaryTotal
    invoice_line: List[InvoiceLine]

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Invoice":
        print(type(obj))
        _ext_ubl_extensions = ExtUBLExtensions.from_dict(obj.get("ext:UBLExtensions"))
        _ubl_version_id = str(obj.get("cbc:UBLVersionID"))
        _customization_id = str(obj.get("cbc:CustomizationID"))
        _profile_id = str(obj.get("cbc:ProfileID"))
        _profile_execution_id = str(obj.get("cbc:ProfileExecutionID"))
        _id = ID.from_dict(obj.get("cbc:ID"))
        _UUID = UUID.from_dict(obj.get("cbc:UUID"))
        _issue_date = str(obj.get("cbc:IssueDate"))
        _issue_time = str(obj.get("cbc:IssueTime"))
        _invoice_type_code = str(obj.get("cbc:InvoiceTypeCode"))
        _note = (
            [Note.from_dict(y) for y in obj.get("cbc:Note", {})]
            if type(obj.get("cbc:Note")) is list
            else [Note.from_dict(obj.get("cbc:Note"))]
        )
        _document_currency_code = str(obj.get("cbc:DocumentCurrencyCode"))
        _delivery = Delivery.from_dict(obj.get("cac:Delivery"))
        _line_count_numeric = str(obj.get("cbc:LineCountNumeric"))
        _accounting_supplier_party = AccountingSupplierParty.from_dict(
            obj.get("cac:AccountingSupplierParty")
        )
        _accounting_customer_party = AccountingCustomerParty.from_dict(
            obj.get("cac:AccountingCustomerParty")
        )
        _order_reference = OrderReference.from_dict(obj.get("cac:OrderReference"))
        _payment_means = PaymentMeans.from_dict(obj.get("cac:PaymentMeans"))
        _tax_total = TaxTotal.from_dict(obj.get("cac:TaxTotal"))
        _legal_monetary_total = LegalMonetaryTotal.from_dict(
            obj.get("cac:LegalMonetaryTotal")
        )
        [print(y) for y in obj.get("cac:InvoiceLine", {})]
        _invoice_line = (
            [InvoiceLine.from_dict(y) for y in obj.get("cac:InvoiceLine", {})]
            if type(obj.get("cac:InvoiceLine")) is list
            else [InvoiceLine.from_dict(obj.get("cac:InvoiceLine"))]
        )
        return Invoice(
            _ext_ubl_extensions,
            _ubl_version_id,
            _customization_id,
            _profile_id,
            _profile_execution_id,
            _id,
            _UUID,
            _issue_date,
            _issue_time,
            _invoice_type_code,
            _note,
            _document_currency_code,
            _delivery,
            _line_count_numeric,
            _accounting_supplier_party,
            _accounting_customer_party,
            _order_reference,
            _payment_means,
            _tax_total,
            _legal_monetary_total,
            _invoice_line,
        )


@dataclass
class Root:
    invoice: Invoice

    @nullable
    @staticmethod
    def from_dict(obj: dict | None) -> "Root":
        _invoice = Invoice.from_dict(obj.get("Invoice"))
        return Root(_invoice)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
