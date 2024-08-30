# Main file for standalone execution
import models
import xmltodict
import service as service

filename = input("Enter the filename: ")

file = service.open_file(filename)
ddict = xmltodict.parse(file)

root: models.Root = models.Root.from_dict(ddict)
invoice: models.Invoice = root.invoice

print(
    "Comercio: "
    + invoice.accounting_supplier_party.party.party_name.name
)
print(
    "Cliente: "
    + invoice.accounting_customer_party.party.party_name.name
)
print("Direccion: " + invoice.accounting_customer_party.party.physical_location.address.address_line.line)
print("Fecha: " + invoice.issue_date)
print("Moneda: " + invoice.document_currency_code)
print("Total: " + str(invoice.legal_monetary_total.tax_inclusive_amount))

for prod in invoice.invoice_line:
    print("Descripcion: " + prod.item.description)
    print("Cantidad: " + str(prod.invoiced_quantity))
    print("Precio: " + str(prod.price.price_amount))
    print("Descuento: " + str(prod.allowance_charge.amount if prod.allowance_charge else 0))
    print("Total: " + str(prod.line_extension_amount))
    print("---------------------------------")

    print("")
