/**
 * TypeScript types for API Spec marketplace
 * Matches backend Pydantic schemas
 */

export interface Tag {
  id: number
  name: string
  spec_count: number
}

export interface ApiSpec {
  id: number
  name: string
  version: string
  provider: string | null
  original_filename: string | null
  original_format: string | null
  token_count: number | null
  uploaded_at: string
  uploaded_by: string | null
  file_size_bytes: number | null
  tags: string[]
}

export interface SpecDetail extends ApiSpec {
  original_content: string
  markdown_content: string
}

export interface SpecListResponse {
  total: number
  page: number
  page_size: number
  specs: ApiSpec[]
}

export interface ChunkedSpec {
  manifest: string
  tags: Record<string, string>
  endpoints: Record<string, string>
  schemas: Record<string, string>
}

export interface ToolSchema {
  name: string
  description: string
  parameters: {
    type: string
    properties: Record<string, any>
    required?: string[]
  }
}

