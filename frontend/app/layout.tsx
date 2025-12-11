import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Clash Royale Deck Brain",
  description: "AI-powered deck analysis",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body>{children}</body></html>;
}
