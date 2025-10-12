import bundleAnalyzer from '@next/bundle-analyzer'
import type { NextConfig } from 'next'
import createNextIntlPlugin from 'next-intl/plugin'

const withNextIntl = createNextIntlPlugin()
const withBundleAnalyzer = bundleAnalyzer({ enabled: process.env.ANALYZE === 'true' })

const nextConfig: NextConfig = {
  // standalone output for Docker
  // output: 'standalone',

  typedRoutes: true,

  // Fix for workspace root warning
  outputFileTracingRoot: '/Users/m0/Documents/Building/bigberlinhack',

  eslint: {
    ignoreDuringBuilds: process.env.NODE_ENV === 'production',
  },

  typescript: {
    ignoreBuildErrors: process.env.NODE_ENV === 'production',
  },

  images: {
    remotePatterns: [],
  },
}

export default withBundleAnalyzer(withNextIntl(nextConfig))
