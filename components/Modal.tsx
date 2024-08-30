import React, { useState } from "react";

export default function Modal({
  invoice,
  setShow,
}: Readonly<{ invoice: Invoice; setShow: (show: boolean) => void }>) {
  const [tab, setTab] = useState<number>(0);

  return (
    // tab navigation. Include a tab for the invoice general data, customer data, seller data, products, totals, and other info
    // Be aware of dark mode and make titles different from the content
    <div className="fixed inset-0 z-50 bg-gray-900 bg-opacity-50 flex items-center justify-center">
      <div className="bg-white dark:bg-gray-800 w-3/4 h-3/4 rounded-lg">
        <div className="flex justify-between items-center px-4 py-2 border-b border-gray-300 dark:border-gray-600 h-12">
          <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100">
            Factura
          </h2>
          <button
            className="text-gray-500 dark:text-gray-400"
            onClick={() => setShow(false)}
          >
            <svg
              className="w-6 h-6"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
        <div className="flex flex-col h-[calc(100%-3rem)]">
          <div className="flex items-center justify-around px-4 py-2 border-b border-gray-300 dark:border-gray-600">
            <button
              className={`text-sm font-semibold ${
                tab === 0
                  ? "text-blue-500 dark:text-blue-400"
                  : "text-gray-500 dark:text-gray-400"
              }`}
              onClick={() => setTab(0)}
            >
              General
            </button>
            <button
              className={`text-sm font-semibold ${
                tab === 1
                  ? "text-blue-500 dark:text-blue-400"
                  : "text-gray-500 dark:text-gray-400"
              }`}
              onClick={() => setTab(1)}
            >
              Cliente
            </button>
            <button
              className={`text-sm font-semibold ${
                tab === 2
                  ? "text-blue-500 dark:text-blue-400"
                  : "text-gray-500 dark:text-gray-400"
              }`}
              onClick={() => setTab(2)}
            >
              Vendedor
            </button>
            <button
              className={`text-sm font-semibold ${
                tab === 3
                  ? "text-blue-500 dark:text-blue-400"
                  : "text-gray-500 dark:text-gray-400"
              }`}
              onClick={() => setTab(3)}
            >
              Productos
            </button>
            <button
              className={`text-sm font -semibold ${
                tab === 4
                  ? "text-blue-500 dark:text-blue-400"
                  : "text-gray-500 dark:text-gray-400"
              }`}
              onClick={() => setTab(4)}
            >
              Totales
            </button>
            <button
              className={`text-sm font-semibold ${
                tab === 5
                  ? "text-blue-500 dark:text-blue-400"
                  : "text-gray-500 dark:text-gray-400"
              }`}
              onClick={() => setTab(5)}
            >
              Otros
            </button>
          </div>
          <div className="flex-1 p-4 overflow-y-auto">
            {tab === 0 && (
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100">
                  General
                </h3>
                <div className="grid md:grid-cols-2 grid-cols-1 gap-4">
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Numero de factura
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.id.text}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Fecha
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.issue_date}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Hora
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.issue_time}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Moneda
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.document_currency_code}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Cantidad de productos
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.line_count_numeric}
                    </p>
                  </div>
                </div>
              </div>
            )}
            {tab === 1 && (
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100">
                  Cliente
                </h3>
                <div className="grid md:grid-cols-2 grid-cols-1 gap-4">
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Nombre
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.accounting_customer_party.party.party_name.name}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Contacto
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_customer_party.party.contact
                          .electronic_mail
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Teléfono
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_customer_party.party.contact
                          .telephone
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Dirección
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_customer_party.party
                          .physical_location.address.address_line.line
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Ciudad
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_customer_party.party
                          .physical_location.address.city_name
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Departamento
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_customer_party.party
                          .physical_location.address.country_subentity
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      País
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_customer_party.party
                          .physical_location.address.country.name.text
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Código Postal
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_customer_party.party
                          .physical_location.address.postal_zone
                      }
                    </p>
                  </div>
                </div>
              </div>
            )}
            {tab === 2 && (
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100">
                  Vendedor
                </h3>
                <div className="grid md:grid-cols-2 grid-cols-1 gap-4">
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Nombre
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.accounting_supplier_party.party.party_name.name}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Contacto
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_supplier_party.party.contact
                          .electronic_mail
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Teléfono
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_supplier_party.party.contact
                          .telephone
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Dirección
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_supplier_party.party
                          .physical_location.address.address_line.line
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Ciudad
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_supplier_party.party
                          .physical_location.address.city_name
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Departamento
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_supplier_party.party
                          .physical_location.address.country_subentity
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      País
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_supplier_party.party
                          .physical_location.address.country.name.text
                      }
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Código Postal
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {
                        invoice.accounting_supplier_party.party
                          .physical_location.address.postal_zone
                      }
                    </p>
                  </div>
                </div>
              </div>
            )}
            {tab === 3 && (
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100">
                  Productos
                </h3>
                <div className="grid lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-4">
                  {invoice.invoice_line.map((line: InvoiceLine) => (
                    <div
                      key={line.id}
                      className="bg-gray-100 dark:bg-gray-700 p-4 rounded-lg"
                    >
                      <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                        Código
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {line.item.sellers_item_identification?.id?.text}
                        {line.item.sellers_item_identification &&
                        line.item.standard_item_identification
                          ? "/"
                          : ""}
                        {line.item.standard_item_identification?.id?.text}
                      </p>
                      <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                        Producto
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {line.item.description}
                      </p>
                      <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                        Cantidad
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {Number(line.invoiced_quantity.text)}
                      </p>
                      <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                        Precio Unitario
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {Number(line.price.price_amount.text)}
                      </p>
                      <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                        Impuestos
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {Number(line.tax_total.tax_rounding_amount.text)}
                      </p>
                      <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                        Descuentos
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {line.allowance_charge?.amount?.text || 0}
                      </p>
                      <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                        Total
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {Number(line.line_extension_amount.text)}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}
            {tab === 4 && (
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100">
                  Totales
                </h3>
                <div className="grid md:grid-cols-2 grid-cols-1 gap-4">
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Total
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.legal_monetary_total.payable_amount.text}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Impuestos
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.tax_total.tax_amount.text}
                    </p>
                  </div>
                </div>
              </div>
            )}
            {tab === 5 && (
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100">
                  Otros
                </h3>
                <div className="grid md:grid-cols-2 grid-cols-1 gap-4">
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      CUFE
                    </h4>
                    <p className="break-all text-sm text-blue-700 dark:text-violet-700 underline">
                      <a
                        href={
                          "https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=" +
                          invoice.UUID.text
                        }
                      >
                        {invoice.UUID.text}
                      </a>
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Versión UBL
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.ubl_version_id}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Perfil ID
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.profile_id}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Perfil ejecución ID
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.profile_execution_id}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Tipo de factura
                    </h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {invoice.invoice_type_code}
                    </p>
                  </div>
                  <div>
                    <h4 className="text-sm font-semibold text-gray-800 dark:text-gray-100">
                      Notas
                    </h4>
                    <div className="text-sm text-gray-500 dark:text-gray-400 grid">
                      {invoice.note.map((note: Note, index: number) => (
                        <p key={index}>{note.text}</p>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

// rewrite the Modal component and be aware of responsiveness. Use tailwindcss classes to make it look good
