// Generated using py-ts-interfaces.
// See https://github.com/cs-cordero/py-ts-interfaces

interface ID {
    scheme_id: string | null;
    scheme_name: string | null;
    text: string;
}

interface PartyIdentification {
    id: UNKNOWN;
}

interface CompanyID {
    scheme_id: string | null;
    scheme_name: string | null;
    scheme_agency_id: string | null;
    scheme_agency_name: string | null;
    text: string;
}

interface CorporateRegistrationScheme {
    id: string;
    name: string;
}

interface PartyLegalEntity {
    registration_name: string;
    company_id: CompanyID;
    corporate_registration_scheme: CorporateRegistrationScheme;
}

interface PartyName {
    name: string;
}

interface TaxScheme {
    id: string;
    name: string;
}

interface TaxLevelCode {
    list_name: string | null;
    text: string;
}

interface Name {
    language_id: string | null;
    text: string;
}

interface Country {
    identification_code: string;
    name: Name;
}

interface AddressLine {
    line: string;
}

interface Address {
    id: string;
    city_name: string;
    postal_zone: string;
    country_subentity: string;
    country_subentity_code: string;
    address_line: Array<AddressLine>;
    country: Country;
}

interface RegistrationAddress {
    id: string;
    city_name: string;
    postal_zone: string;
    country_subentity: string;
    country_subentity_code: string;
    address_line: AddressLine;
    country: Country;
}

interface PartyTaxScheme {
    registration_name: string;
    company_id: CompanyID;
    tax_level_code: TaxLevelCode;
    registration_address: RegistrationAddress;
    tax_scheme: TaxScheme;
}

interface PhysicalLocation {
    name: string;
    address: Address;
}

interface Contact {
    telephone: string;
    electronic_mail: string;
    name: string;
}

interface Person {
    first_name: string;
    family_name: string;
}

interface Party {
    party_name: PartyName;
    person: Person;
    physical_location: PhysicalLocation;
    party_tax_scheme: PartyTaxScheme;
    party_legal_entity: PartyLegalEntity;
    contact: Contact;
    party_identification: PartyIdentification;
    industry_classification_code: string;
}

interface AccountingCustomerParty {
    additional_account_id: string;
    party: Party;
}

interface AccountingSupplierParty {
    additional_account_id: string;
    party: Party;
}

interface Amount {
    currency_id: string | null;
    text: string;
}

interface BaseAmount {
    currency_id: string | null;
    text: string;
}

interface AllowanceCharge {
    id: string;
    charge_indicator: string;
    multiplier_factor_numeric: string;
    amount: Amount;
    base_amount: BaseAmount;
}

interface Note {
    text: string;
}

interface InvoicedQuantity {
    unit_code: string | null;
    text: string;
}

interface LineExtensionAmount {
    currency_id: string | null;
    text: string;
}

interface TaxAmount {
    currency_id: string | null;
    text: string;
}

interface TaxCategory {
    percent: string;
    tax_scheme: TaxScheme;
}

interface TaxableAmount {
    currency_id: string | null;
    text: string;
}

interface TaxSubtotal {
    taxable_amount: TaxableAmount;
    tax_amount: TaxAmount;
    tax_category: TaxCategory;
}

interface TaxTotal {
    tax_amount: TaxAmount;
    tax_subtotal: TaxSubtotal;
    tax_rounding_amount: TaxAmount;
}

interface StandardItemIdentification {
    id: ID;
}

interface Item {
    description: string;
    standard_item_identification: StandardItemIdentification;
    sellers_item_identification: StandardItemIdentification;
    brand_name: string;
    pack_size_numeric: string;
}

interface PriceAmount {
    currency_id: string | null;
    text: string;
}

interface BaseQuantity {
    unit_code: string | null;
    text: string;
}

interface Price {
    price_amount: PriceAmount;
    base_quantity: BaseQuantity;
}

interface InvoiceLine {
    id: string;
    note: Array<Note>;
    invoiced_quantity: InvoicedQuantity;
    line_extension_amount: LineExtensionAmount;
    allowance_charge: AllowanceCharge;
    tax_total: TaxTotal;
    item: Item;
    price: Price;
}

interface PaymentMeans {
    id: string;
    payment_means_code: string;
    payment_due_date: string;
    payment_id: string;
}

interface AllowanceTotalAmount {
    currency_id: string | null;
    text: string;
}

interface ChargeTotalAmount {
    currency_id: string | null;
    text: string;
}

interface IdentificationCode {
    list_agency_id: string | null;
    list_agency_name: string | null;
    list_scheme_uri: string | null;
    text: string;
}

interface PayableAmount {
    currency_id: string | null;
    text: string;
}

interface PayableRoundingAmount {
    currency_id: string | null;
    text: string;
}

interface TaxExclusiveAmount {
    currency_id: string | null;
    text: string;
}

interface TaxInclusiveAmount {
    currency_id: string | null;
    text: string;
}

interface UUID {
    scheme_id: string | null;
    scheme_name: string | null;
    text: string;
}

interface LegalMonetaryTotal {
    line_extension_amount: LineExtensionAmount;
    tax_exclusive_amount: TaxExclusiveAmount;
    tax_inclusive_amount: TaxInclusiveAmount;
    allowance_total_amount: AllowanceTotalAmount;
    charge_total_amount: ChargeTotalAmount;
    payable_rounding_amount: PayableRoundingAmount;
    payable_amount: PayableAmount;
}

interface DsCanonicalizationMethod {
    algorithm: string;
}

interface DsDigestMethod {
    algorithm: string;
}

interface DsRSAKeyValue {
    modulus: string;
    exponent: string;
}

interface DsKeyValue {
    rsa_key_value: DsRSAKeyValue;
}

interface DsX509Data {
    x509_certificate: string;
}

interface DsKeyInfo {
    id: string;
    x509_data: DsX509Data;
    key_value: DsKeyValue;
}

interface XadesSigPolicyId {
    xades_identifier: string;
    xades_description: string;
}

interface XadesSigPolicyHash {
    digest_method: DsDigestMethod;
    digest_value: string;
}

interface XadesSignaturePolicyId {
    xades_sig_policy_id: XadesSigPolicyId;
    xades_sig_policy_hash: XadesSigPolicyHash;
}

interface XadesSignaturePolicyIdentifier {
    xades_signature_policy_id: XadesSignaturePolicyId;
}

interface XadesClaimedRoles {
    xades_claimed_role: string;
}

interface XadesSignerRole {
    xades_claimed_roles: XadesClaimedRoles;
}

interface XadesCertDigest {
    digest_method: DsDigestMethod;
    digest_value: string;
}

interface XadesIssuerSerial {
    x509_issuer_name: string;
    x509_serial_number: string;
}

interface XadesCert {
    xades_cert_digest: XadesCertDigest;
    xades_issuer_serial: XadesIssuerSerial;
}

interface XadesSigningCertificate {
    xades_cert: XadesCert;
}

interface XadesSignedSignatureProperties {
    xades_signing_time: string;
    xades_signing_certificate: XadesSigningCertificate;
    xades_signature_policy_identifier: XadesSignaturePolicyIdentifier;
    xades_signer_role: XadesSignerRole;
}

interface XadesSignedProperties {
    id: string;
    xades_signed_signature_properties: XadesSignedSignatureProperties;
}

interface XadesQualifyingProperties {
    xmlnsxades: string;
    target: string;
    id: string;
    xades_signed_properties: XadesSignedProperties;
}

interface DsObject {
    xades_qualifying_properties: XadesQualifyingProperties;
}

interface DsTransform {
    algorithm: string;
}

interface DsTransforms {
    transform: DsTransform;
}

interface DsReference {
    id: string;
    URI: string;
    transforms: DsTransforms;
    digest_method: DsDigestMethod;
    digest_value: string;
}

interface DsSignatureMethod {
    algorithm: string;
}

interface DsSignedInfo {
    canonicalization_method: DsCanonicalizationMethod;
    signature_method: DsSignatureMethod;
    reference: Array<DsReference>;
}

interface DsSignature {
    xmlnsds: string;
    id: string;
    signed_info: DsSignedInfo;
    signature_value: string;
    key_info: DsKeyInfo;
    object: DsObject;
}

interface StsAuthorizationPeriod {
    start_date: string;
    end_date: string;
}

interface StsAuthorizationProviderID {
    scheme_agency_id: string | null;
    scheme_agency_name: string | null;
    scheme_id: string | null;
    scheme_name: string | null;
    text: string;
}

interface StsAuthorizationProvider {
    authorization_provider_id: StsAuthorizationProviderID;
}

interface StsAuthorizedInvoices {
    prefix: string;
    stsfrom: string;
    to: string;
}

interface StsInvoiceControl {
    invoice_authorization: string;
    authorization_period: StsAuthorizationPeriod;
    authorized_invoices: StsAuthorizedInvoices;
}

interface StsInvoiceSource {
    identification_code: IdentificationCode;
}

interface StsProviderID {
    scheme_agency_id: string | null;
    scheme_agency_name: string | null;
    scheme_id: string | null;
    scheme_name: string | null;
    text: string;
}

interface StsSoftwareID {
    scheme_agency_id: string | null;
    scheme_agency_name: string | null;
    text: string;
}

interface StsSoftwareProvider {
    provider_id: StsProviderID;
    software_id: StsSoftwareID;
}

interface StsSoftwareSecurityCode {
    scheme_agency_id: string | null;
    scheme_agency_name: string | null;
    text: string;
}

interface StsDianExtensions {
    invoice_control: StsInvoiceControl;
    invoice_source: StsInvoiceSource;
    software_provider: StsSoftwareProvider;
    software_security_code: StsSoftwareSecurityCode;
    authorization_provider: StsAuthorizationProvider;
    qr_code: string;
}

interface ExtExtensionContent {
    dian_extensions: StsDianExtensions;
    signature: DsSignature;
}

interface ExtUBLExtension {
    ext_extension_content: ExtExtensionContent;
}

interface ExtUBLExtensions {
    ext_ubl_extension: Array<ExtUBLExtension>;
}

interface Delivery {
    actual_delivery_date: string;
    actual_delivery_time: string;
}

interface OrderReference {
    id: string;
    issue_date: string;
}

interface Invoice {
    ext_ubl_extensions: ExtUBLExtensions;
    ubl_version_id: string;
    customization_id: string;
    profile_id: string;
    profile_execution_id: string;
    id: ID;
    UUID: UUID;
    issue_date: string;
    issue_time: string;
    invoice_type_code: string;
    note: Array<Note>;
    document_currency_code: string;
    delivery: Delivery;
    line_count_numeric: string;
    accounting_supplier_party: AccountingSupplierParty;
    accounting_customer_party: AccountingCustomerParty;
    order_reference: OrderReference;
    payment_means: PaymentMeans;
    tax_total: TaxTotal;
    legal_monetary_total: LegalMonetaryTotal;
    invoice_line: Array<InvoiceLine>;
}

interface Root {
    invoice: Invoice;
}
