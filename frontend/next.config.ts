import bundleAnalyzer from '@next/bundle-analyzer'
import type { NextConfig } from 'next'
import createNextIntlPlugin from 'next-intl/plugin'
import { resolve } from 'path'

const withNextIntl = createNextIntlPlugin()
const withBundleAnalyzer = bundleAnalyzer({ enabled: process.env.ANALYZE === 'true' })

const nextConfig: NextConfig = {
  // standalone output for Docker
  // output: 'standalone',

  typedRoutes: true,

  // Fix for workspace root warning
  outputFileTracingRoot: resolve(__dirname, '..'),

  images: {
    remotePatterns: [],
  },
}

export default withBundleAnalyzer(withNextIntl(nextConfig))
