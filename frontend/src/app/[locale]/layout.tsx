import { Toaster } from '@/components/ui/sonner'

import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import type React from 'react'
import '../../styles/globals.css'

import { rootMetadata } from '#/config/root-metadata'
import { routing } from '@/i18n/routing'
import { hasLocale } from 'next-intl'
import { notFound } from 'next/navigation'
import { RootWrapper } from './root-wrapper'

const inter = Inter({ subsets: ['latin'] })

export default async function RootLayout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ locale: string }>
}) {
  const { locale } = await params
  if (!hasLocale(routing.locales, locale)) {
    notFound()
  }

  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <RootWrapper locale={locale}>{children}</RootWrapper>
        <Toaster />
      </body>
    </html>
  )
}

export const metadata: Metadata = { ...rootMetadata }
