import { Inter } from "next/font/google";
import "./globals.css";
import "@mantine/core/styles.css";
import { ColorSchemeScript, MantineProvider } from "@mantine/core";

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
                <MantineProvider>{children}</MantineProvider>
            </body>
        </html>
    );
}
