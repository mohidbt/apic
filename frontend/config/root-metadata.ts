import type { Metadata } from 'next'

export const rootMetadata: Metadata = {
  title: {
    default: 'API Ingest',
    template: '%s | API Ingest',
  },
  description: 'Let LLMs finally understand API Docs.',
  keywords: ['API', 'Documentation', 'LLM', 'AI', 'OpenAPI', 'Swagger'],
  authors: [{ name: 'Mohid Butt' }],
  creator: 'Mohid Butt',
  metadataBase: new URL('https://apiingest.koyeb.app'),
  icons: {
    icon: '/favicon.ico',
    shortcut: '/favicon.ico',
    apple: '/favicon.ico',
  },
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://apiingest.koyeb.app/',
    title: 'API Ingest',
    description: 'Let LLMs finally understand API Docs.',
    siteName: 'API Ingest',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'API Ingest',
    description: 'Let LLMs finally understand API Docs.',
    creator: '@mohidbt',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
}
