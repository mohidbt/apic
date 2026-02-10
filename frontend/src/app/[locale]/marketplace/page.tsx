import { fetchSpecs, fetchTags } from '@/lib/api'
import { MarketplaceClient } from './marketplace-client'

export default async function MarketplacePage() {
  // Fetch initial data on the server
  const [specsData, tags] = await Promise.all([
    fetchSpecs(1, 20), // First page with 20 items
    fetchTags()
  ])

  return (
    <MarketplaceClient
      initialSpecs={specsData.specs}
      initialTags={tags}
      initialTotal={specsData.total}
    />
  )
}

