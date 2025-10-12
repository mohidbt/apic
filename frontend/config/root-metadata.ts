import type { Metadata } from 'next'

export const rootMetadata: Metadata = {
  title: {
    default: 'Next.js Boilerplate',
    template: '%s | Next.js Boilerplate',
  },
  description: 'A comprehensive Next.js boilerplate with modern tooling',
  keywords: ['Next.js', 'React', 'TypeScript', 'Tailwind CSS'],
  authors: [{ name: 'Your Name' }],
  creator: 'Your Name',
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://your-domain.com',
    title: 'Next.js Boilerplate',
    description: 'A comprehensive Next.js boilerplate with modern tooling',
    siteName: 'Next.js Boilerplate',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Next.js Boilerplate',
    description: 'A comprehensive Next.js boilerplate with modern tooling',
    creator: '@yourusername',
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
