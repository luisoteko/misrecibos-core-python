from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AuthorizationPeriod:
    start_date: str
    end_date: str


@dataclass
class AuthorizedInvoices:
    prefix: str
    from_invoice: int
    to_invoice: int


@dataclass
class InvoiceControl:
    invoice_authorization: str
    authorization_period: AuthorizationPeriod
    authorized_invoices: AuthorizedInvoices


@dataclass
class InvoiceSource:
    identification_code: str


@dataclass
class SoftwareProvider:
    provider_id: str
    software_id: str


@dataclass
class AuthorizationProvider:
    authorization_provider_id: str


@dataclass
class DianExtensions:
    invoice_control: InvoiceControl
    invoice_source: InvoiceSource
    software_provider: SoftwareProvider
    software_security_code: str
    authorization_provider: AuthorizationProvider
    qr_code: str


@dataclass
class UBLExtension:
    dian_extensions: Optional[DianExtensions] = None
    signature: Optional[str] = None


@dataclass
class Address:
    id: str
    city_name: str
    postal_zone: str
    country_subentity: str
    country_subentity_code: str
    line: str
    country_code: str
    country_name: str


@dataclass
class PartyTaxScheme:
    registration_name: str
    company_id: str
    tax_level_code: str
    address: Address
    tax_scheme_id: str
    tax_scheme_name: str


@dataclass
class PartyLegalEntity:
    registration_name: str
    company_id: str
    corporate_registration_id: str


@dataclass
class Contact:
    telephone: str
    email: str


@dataclass
class Party:
    party_name: str
    physical_location: Address
    party_tax_scheme: PartyTaxScheme
    party_legal_entity: PartyLegalEntity
    contact: Contact


@dataclass
class AccountingSupplierParty:
    additional_account_id: str
    party: Party


@dataclass
class AccountingCustomerParty:
    additional_account_id: str
    party: Party


@dataclass
class AllowanceCharge:
    charge_indicator: bool
    allowance_charge_reason: str
    multiplier_factor_numeric: float
    amount: float
    base_amount: float


@dataclass
class InvoiceLine:
    id: int
    notes: List[str]
    invoiced_quantity: float
    line_extension_amount: float
    tax_total: float
    item_description: str
    item_id: str
    price_amount: float
    base_quantity: float
    allowance_charge: AllowanceCharge


@dataclass
class TaxTotal:
    tax_amount: float
    taxable_amount: float
    tax_percentage: float
    tax_name: str


@dataclass
class LegalMonetaryTotal:
    line_extension_amount: float
    tax_exclusive_amount: float
    tax_inclusive_amount: float
    allowance_total_amount: float
    charge_total_amount: float
    payable_rounding_amount: float
    payable_amount: float


@dataclass
class Invoice:
    ubl_version_id: str
    customization_id: str
    profile_id: str
    profile_execution_id: str
    id: str
    uuid: str
    issue_date: str
    issue_time: str
    invoice_type_code: str
    document_currency_code: str
    line_count_numeric: int
    accounting_supplier_party: AccountingSupplierParty
    accounting_customer_party: AccountingCustomerParty
    tax_total: TaxTotal
    legal_monetary_total: LegalMonetaryTotal
    invoice_lines: List[InvoiceLine]
    ubl_extensions: List[UBLExtension] = field(default_factory=list)
