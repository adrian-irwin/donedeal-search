import Providers from "@/app/providers";
import { ColorSchemeScript } from "@mantine/core";
import "@mantine/core/styles.css";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
    title: "Better DoneDeal Frontend",
    description: "Created By airwin",
};

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <head>
                <ColorSchemeScript />
            </head>
            <body className={inter.className}>
                <Providers>{children}</Providers>
            </body>
        </html>
    );
}
