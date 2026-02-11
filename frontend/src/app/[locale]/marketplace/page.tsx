import { fetchSpecs, fetchTags, fetchGitHubStats } from '@/lib/api'
import { MarketplaceClient } from './marketplace-client'

export default async function MarketplacePage() {
  // Fetch initial data on the server (including GitHub stats)
  const [specsData, tags, githubStats] = await Promise.all([
    fetchSpecs(1, 20), // First page with 20 items
    fetchTags(),
    fetchGitHubStats() // Fetch star count server-side
  ])

  return (
    <MarketplaceClient
      initialSpecs={specsData.specs}
      initialTags={tags}
      initialTotal={specsData.total}
      starCount={githubStats.stargazers_count}
    />
  )
}

