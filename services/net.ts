export async function postFile (file: File): Promise<Invoice> {
  const formData = new FormData();
  formData.append("file", file);
  
  const res = await fetch("/api/invoice", {
    method: "POST",
    headers: {
      "Accept": "application/json",
    },
    body: formData,
  });
  return await res.json();
}