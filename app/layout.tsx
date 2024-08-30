import "./globals.css";
import { Inter } from "next/font/google";
import { Analytics } from "@vercel/analytics/next";
import { SpeedInsights } from "@vercel/speed-insights/next";
import Header from "./header";
import Footer from "./footer";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "MisRecibos",
  description: "Sitio para leer facilmente tus facturas electronicas (Colombia)",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body className="min-h-screen flex flex-col">
        <ToastContainer/>
        <Header />
        {children}
        <Footer />
      </body>
      <Analytics />
      <SpeedInsights />
    </html>
  );
}
