import { fetchSpecs, fetchGitHubStats } from '@/lib/api'
import { MarketplaceClient } from './marketplace-client'

export default async function MarketplacePage() {
  // Fetch initial data on the server (including GitHub stats).
  // If the backend is temporarily unavailable, render a resilient empty state.
  let specsData: Awaited<ReturnType<typeof fetchSpecs>> = { specs: [], total: 0 }
  let githubStats: Awaited<ReturnType<typeof fetchGitHubStats>> = { stargazers_count: 0 }

  try {
    ;[specsData, githubStats] = await Promise.all([
      fetchSpecs(1, 20), // First page with 20 items
      fetchGitHubStats(), // Fetch star count server-side
    ])
  } catch (error) {
    console.error('Failed to fetch marketplace data:', error)
  }

  return (
    <MarketplaceClient
      initialSpecs={specsData.specs}
      initialTotal={specsData.total}
      starCount={githubStats.stargazers_count}
    />
  )
}

