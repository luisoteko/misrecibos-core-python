# Main file for standalone execution
import models
import service

filename = input("Enter the filename: ")

file = service.open_file(filename)

invoice: models.Invoice = service.parse_invoice(file)

print(
    "Comercio: "
    + invoice.accounting_supplier_party.party.party_legal_entity.registration_name
)
print(
    "Cliente: "
    + invoice.accounting_customer_party.party.party_name
)
print("Direccion: " + invoice.accounting_customer_party.party.physical_location.line)
print("Fecha: " + invoice.issue_date)
print("Moneda: " + invoice.document_currency_code)
print("Total: " + str(invoice.legal_monetary_total.tax_inclusive_amount))

for prod in invoice.invoice_lines:
    print("Descripcion: " + prod.item_description)
    print("Cantidad: " + str(prod.invoiced_quantity))
    print("Precio: " + str(prod.price_amount))
    print("Descuento: " + str(prod.allowance_charge.amount))
    print("Total: " + str(prod.line_extension_amount))
    print("---------------------------------")

    print("")
