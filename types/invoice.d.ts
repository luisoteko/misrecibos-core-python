export interface Invoice {
  accounting_customer_party: AccountingErParty;
  accounting_supplier_party: AccountingErParty;
  allowance_charge: any[];
  customization_id: string;
  document_currency_code: string;
  id: string;
  invoice_lines: InvoiceLine[];
  invoice_type_code: string;
  issue_date: Date;
  issue_time: string;
  legal_monetary_total: LegalMonetaryTotal;
  line_count_numeric: string;
  profile_execution_id: string;
  profile_id: string;
  tax_total: TaxTotal;
  ubl_extensions: UblExtension[];
  ubl_version_id: string;
  uuid: string;
}

export interface AccountingErParty {
  additional_account_id: string;
  party: Party;
}

export interface Party {
  contact: Contact;
  party_legal_entity: PartyLegalEntity;
  party_name: string;
  party_tax_scheme: PartyTaxScheme;
  physical_location: PhysicalLocation;
}

export interface Contact {
  email: string;
  telephone: string;
}

export interface PartyLegalEntity {
  company_id: string;
  corporate_registration_id: string;
  registration_name: string;
}

export interface PartyTaxScheme {
  address: PhysicalLocation;
  company_id: string;
  registration_name: string;
  tax_level_code: string;
  tax_scheme_id: string;
  tax_scheme_name: string;
}

export interface PhysicalLocation {
  city_name: string;
  country_code: string;
  country_name: string;
  country_subentity: string;
  country_subentity_code: string;
  id: string;
  line: string;
  postal_zone: string;
}

export interface InvoiceLine {
  allowance_charge: AllowanceCharge;
  base_quantity: string;
  id: number;
  invoiced_quantity: string;
  item_description: string;
  item_id: string;
  line_extension_amount: string;
  notes: string[];
  price_amount: string;
  tax_total: string;
}

export interface AllowanceCharge {
  allowance_charge_reason: string;
  amount: string;
  base_amount: string;
  charge_indicator: string;
  multiplier_factor_numeric: string;
}

export interface LegalMonetaryTotal {
  allowance_total_amount: string;
  charge_total_amount: string;
  line_extension_amount: string;
  payable_amount: string;
  payable_rounding_amount: string;
  tax_exclusive_amount: string;
  tax_inclusive_amount: string;
}

export interface TaxTotal {
  tax_amount: string;
  tax_name: string;
  tax_percentage: string;
  taxable_amount: string;
}

export interface UblExtension {
  dian_extensions: DianExtensions | null;
  signature: null | string;
}

export interface DianExtensions {
  authorization_provider: AuthorizationProvider;
  invoice_control: InvoiceControl;
  invoice_source: InvoiceSource;
  qr_code: string;
  software_provider: SoftwareProvider;
  software_security_code: string;
}

export interface AuthorizationProvider {
  authorization_provider_id: string;
}

export interface InvoiceControl {
  authorization_period: AuthorizationPeriod;
  authorized_invoices: AuthorizedInvoices;
  invoice_authorization: string;
}

export interface AuthorizationPeriod {
  end_date: Date;
  start_date: Date;
}

export interface AuthorizedInvoices {
  from_invoice: number;
  prefix: string;
  to_invoice: number;
}

export interface InvoiceSource {
  identification_code: string;
}

export interface SoftwareProvider {
  provider_id: string;
  software_id: string;
}
