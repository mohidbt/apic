/**
 * API service for interacting with the backend API
 */

import { ApiSpec, SpecDetail, SpecListResponse, Tag } from '@/types/api-spec'

/**
 * Get the appropriate API base URL based on the environment
 * - Server-side: Uses internal localhost URL for same-container communication
 * - Client-side: Uses NEXT_PUBLIC_API_URL (public URL)
 */
function getApiBaseUrl(): string {
  // Check if we're running on the server
  const isServer = typeof window === 'undefined'
  
  if (isServer) {
    // Server-side: use localhost for internal communication
    // In production (Koyeb), both frontend and backend run in the same container
    // So we can use localhost:8000 for faster, internal communication
    return 'http://localhost:8000'
  } else {
    // Client-side: use the public URL from environment variable
    return process.env.NEXT_PUBLIC_API_URL || ''
  }
}

/**
 * Fetch specs with pagination and optional filtering
 */
export async function fetchSpecs(
  page: number = 1,
  limit: number = 20,
  search?: string,
  tag?: string
): Promise<SpecListResponse> {
  const API_BASE_URL = getApiBaseUrl()
  const skip = (page - 1) * limit
  const params = new URLSearchParams({
    skip: skip.toString(),
    limit: limit.toString(),
  })

  if (tag) {
    params.append('tag', tag)
  }

  let url = `${API_BASE_URL}/api/specs`
  
  // Use search endpoint if search query is provided
  if (search) {
    url = `${API_BASE_URL}/api/specs/search`
    params.append('q', search)
  }

  const response = await fetch(`${url}?${params.toString()}`)

  if (!response.ok) {
    throw new Error(`Failed to fetch specs: ${response.statusText}`)
  }

  return response.json()
}

/**
 * Fetch detailed information about a specific spec
 */
export async function fetchSpecDetail(id: number): Promise<SpecDetail> {
  const API_BASE_URL = getApiBaseUrl()
  const response = await fetch(`${API_BASE_URL}/api/specs/${id}`)

  if (!response.ok) {
    if (response.status === 404) {
      throw new Error('Spec not found')
    }
    throw new Error(`Failed to fetch spec detail: ${response.statusText}`)
  }

  return response.json()
}

/**
 * Fetch all available tags with their spec counts
 */
export async function fetchTags(): Promise<Tag[]> {
  const API_BASE_URL = getApiBaseUrl()
  const response = await fetch(`${API_BASE_URL}/api/tags`)

  if (!response.ok) {
    throw new Error(`Failed to fetch tags: ${response.statusText}`)
  }

  return response.json()
}

/**
 * Download markdown file for a spec
 * 
 * Optimized approach: Instead of fetching and converting to blob,
 * we directly navigate to the download URL which triggers immediate download.
 */
export async function downloadMarkdown(id: number, name: string, version: string): Promise<void> {
  // #region agent log
  const startTime = Date.now()
  fetch('http://127.0.0.1:7242/ingest/26f372ca-c5c1-4e8f-a08b-c5daee8e57f0',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'api.ts:98',message:'downloadMarkdown called (optimized)',data:{id,name,version},timestamp:Date.now(),hypothesisId:'F'})}).catch(()=>{})
  // #endregion
  
  const API_BASE_URL = getApiBaseUrl()
  const url = `${API_BASE_URL}/api/specs/${id}/download/markdown`
  
  // Create a temporary anchor element and trigger download
  // This approach starts the download immediately without waiting for blob conversion
  const a = document.createElement('a')
  a.href = url
  a.download = `${name}-v${version}.md`.replace(/\s+/g, '-')
  a.style.display = 'none'
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  
  // #region agent log
  const totalDuration = Date.now() - startTime
  fetch('http://127.0.0.1:7242/ingest/26f372ca-c5c1-4e8f-a08b-c5daee8e57f0',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'api.ts:119',message:'Download link triggered (optimized)',data:{total_duration_ms:totalDuration},timestamp:Date.now(),hypothesisId:'F'})}).catch(()=>{})
  // #endregion
}

/**
 * Download original OpenAPI file for a spec
 * 
 * Optimized approach: Direct download link instead of blob conversion
 */
export async function downloadOriginal(
  id: number,
  name: string,
  version: string,
  format: string
): Promise<void> {
  const API_BASE_URL = getApiBaseUrl()
  const url = `${API_BASE_URL}/api/specs/${id}/download/original`
  
  // Create a temporary anchor element and trigger download
  const a = document.createElement('a')
  a.href = url
  const ext = format === 'json' ? 'json' : 'yaml'
  a.download = `${name}-v${version}.${ext}`.replace(/\s+/g, '-')
  a.style.display = 'none'
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
}

/**
 * Format file size in bytes to human-readable format
 */
export function formatFileSize(bytes: number | null): string {
  if (!bytes) return 'N/A'
  
  const units = ['B', 'KB', 'MB', 'GB']
  let size = bytes
  let unitIndex = 0
  
  while (size >= 1024 && unitIndex < units.length - 1) {
    size /= 1024
    unitIndex++
  }
  
  return `${size.toFixed(unitIndex === 0 ? 0 : 1)} ${units[unitIndex]}`
}

/**
 * Format date string to human-readable format
 */
export function formatDate(dateString: string): string {
  const date = new Date(dateString)
  const now = new Date()
  const diffMs = now.getTime() - date.getTime()
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))
  
  if (diffDays === 0) {
    return 'Today'
  } else if (diffDays === 1) {
    return 'Yesterday'
  } else if (diffDays < 7) {
    return `${diffDays} days ago`
  } else if (diffDays < 30) {
    const weeks = Math.floor(diffDays / 7)
    return `${weeks} week${weeks > 1 ? 's' : ''} ago`
  } else if (diffDays < 365) {
    const months = Math.floor(diffDays / 30)
    return `${months} month${months > 1 ? 's' : ''} ago`
  } else {
    return date.toLocaleDateString()
  }
}

/**
 * Fetch GitHub repository statistics (cached on backend)
 */
export async function fetchGitHubStats(): Promise<{
  stargazers_count: number
  forks_count?: number
  watchers_count?: number
  cached?: boolean
}> {
  const API_BASE_URL = getApiBaseUrl()
  const response = await fetch(`${API_BASE_URL}/api/github/stats`)

  if (!response.ok) {
    // Return default if API fails
    return { stargazers_count: 0 }
  }

  return response.json()
}

