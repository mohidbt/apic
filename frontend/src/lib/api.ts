/**
 * API service for interacting with the backend API
 */

import { ApiSpec, SpecDetail, SpecListResponse, Tag } from '@/types/api-spec'

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || ''

/**
 * Fetch specs with pagination and optional filtering
 */
export async function fetchSpecs(
  page: number = 1,
  limit: number = 20,
  search?: string,
  tag?: string
): Promise<SpecListResponse> {
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
  const response = await fetch(`${API_BASE_URL}/api/tags`)

  if (!response.ok) {
    throw new Error(`Failed to fetch tags: ${response.statusText}`)
  }

  return response.json()
}

/**
 * Download markdown file for a spec
 */
export async function downloadMarkdown(id: number, name: string, version: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/specs/${id}/download/markdown`)

  if (!response.ok) {
    throw new Error(`Failed to download markdown: ${response.statusText}`)
  }

  const blob = await response.blob()
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `${name}-v${version}.md`.replace(/\s+/g, '-')
  document.body.appendChild(a)
  a.click()
  window.URL.revokeObjectURL(url)
  document.body.removeChild(a)
}

/**
 * Download original OpenAPI file for a spec
 */
export async function downloadOriginal(
  id: number,
  name: string,
  version: string,
  format: string
): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/specs/${id}/download/original`)

  if (!response.ok) {
    throw new Error(`Failed to download original file: ${response.statusText}`)
  }

  const blob = await response.blob()
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  const ext = format === 'json' ? 'json' : 'yaml'
  a.download = `${name}-v${version}.${ext}`.replace(/\s+/g, '-')
  document.body.appendChild(a)
  a.click()
  window.URL.revokeObjectURL(url)
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

