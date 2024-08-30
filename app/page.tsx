'use client'
// Page should contain an area to load a file, and a button to submit it
// The input should be of type file, and it has to allow drag and drop files in the drop zone

import DropFile from "@/components/DropFile";
import { useState } from "react";
import { postFile } from "@/services/net";
import Modal from "@/components/Modal";

// Style it using tailwindcss
export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [invoice, setInvoice] = useState<Invoice | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [showModal, setShowModal] = useState<boolean>(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>|null) => {
    if (e === null) {
      setFile(null);
      return
    }
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const submit = async () => {
    console.log(file);
    if (!file) return;
    setLoading(true);
    const invoice = await postFile(file);
    console.log(invoice);
    setLoading(false);
    setInvoice(invoice);
    setShowModal(true);
  }

  return (
    <>
      {showModal && invoice && <Modal setShow={setShowModal} invoice={invoice}></Modal>}
      <div className="flex-grow flex flex-col items-center justify-center min-h-[calc(100%-4rem)] py-2 dark:bg-gray-800">
        <main className="flex flex-col items-center justify-between w-full flex-1 px-20">
          <h1 className="text-6xl font-bold text-center text-gray-800 dark:text-gray-100">
            Sube tu factura
          </h1>
          <DropFile file={file} handleChange={handleChange}></DropFile>
          <div className="mt-8">
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded disabled:bg-gray-500"
              onClick={submit}
              disabled={!file}
            >
              Consultar
            </button>
          </div>
        </main>
      </div>
    </>
  );
}
