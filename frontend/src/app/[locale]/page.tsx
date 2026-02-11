import { fetchGitHubStats } from '@/lib/api'
import HomeClient from './home-client'

export default async function HomePage() {
  // Fetch GitHub star count on server (leverages 1-hour cache)
  const githubStats = await fetchGitHubStats()
  
  return <HomeClient starCount={githubStats.stargazers_count} />
}


