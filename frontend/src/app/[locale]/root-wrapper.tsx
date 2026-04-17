'use client'

// import { useScan } from 'react-scan'

import { NextIntlClientProvider } from 'next-intl'
import React from 'react'
import { ThemeProvider } from '../../components/theme-provider'
import { AuthProvider } from '@/lib/auth-context'

export const RootWrapper = ({
  children,
  locale,
}: {
  children: React.ReactNode
  locale: string
}) => {
  // uncomment if you  want to use react-scan, this can be annoying sometimes - so by default it's disabled
  //   useScan({ enabled: process.env.NODE_ENV === 'development' })
  return (
    <>
      <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false} disableTransitionOnChange>
        <NextIntlClientProvider locale={locale}>
          <AuthProvider>{children}</AuthProvider>
        </NextIntlClientProvider>
      </ThemeProvider>
    </>
  )
}
