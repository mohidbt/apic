'use client'

import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Checkbox } from '@/components/ui/checkbox'
import { ThemeToggle } from '@/components/theme-toggle'
import { Github, Sparkles, Star, Upload, FileText, Loader2, Package } from 'lucide-react'
import { useState, useRef } from 'react'
import { toast } from 'sonner'
import { Link } from '@/i18n/navigation'

interface HomeClientProps {
  starCount: number
}

export default function HomeClient({ starCount }: HomeClientProps) {
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [isUploading, setIsUploading] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const validateFile = (file: File): boolean => {
    const validExtensions = ['.yaml', '.yml', '.json']
    const fileExtension = file.name.substring(file.name.lastIndexOf('.')).toLowerCase()
    
    if (!validExtensions.includes(fileExtension)) {
      toast.error('Invalid file type. Please upload a YAML, YML or JSON spec.')
      return false
    }
    return true
  }

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file && validateFile(file)) {
      setSelectedFile(file)
      toast.success(`File selected: ${file.name}`)
    }
  }

  const handleUploadClick = () => {
    fileInputRef.current?.click()
  }

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    e.stopPropagation()
  }

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    e.stopPropagation()
    
    const file = e.dataTransfer.files?.[0]
    if (file && validateFile(file)) {
      setSelectedFile(file)
      toast.success(`File selected: ${file.name}`)
    }
  }

  const handleConvert = async () => {
    if (!selectedFile) {
      toast.error('Please select a file first')
      return
    }

    setIsUploading(true)
    const formData = new FormData()
    formData.append('file', selectedFile)

    // Use environment variable for API URL, fallback to relative path for production
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || ''

    try {
      const response = await fetch(`${apiUrl}/api/convert`, {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Conversion failed')
      }

      // Get the filename from the response headers or create one
      const contentDisposition = response.headers.get('Content-Disposition')
      let filename = 'converted.md'
      if (contentDisposition) {
        const filenameMatch = contentDisposition.match(/filename="?(.+)"?/)
        if (filenameMatch) {
          filename = filenameMatch[1]
        }
      }

      // Download the file
      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = filename
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)

      toast.success('File converted and downloaded successfully!')
      setSelectedFile(null)
      if (fileInputRef.current) {
        fileInputRef.current.value = ''
      }
    } catch (error) {
      console.error('Conversion error:', error)
      console.error('API URL used:', apiUrl)
      console.error('Full endpoint:', `${apiUrl}/api/convert`)
      toast.error(error instanceof Error ? error.message : 'Failed to convert file')
    } finally {
      setIsUploading(false)
    }
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card">
        <div className="container mx-auto flex h-16 items-center justify-between px-4">
          <div className="flex items-center space-x-2">
            <span className="text-2xl font-bold">
              <span className="text-foreground">API Ingest</span>
            </span>
          </div>
          <div className="flex items-center space-x-4">
            <Link 
              href="/marketplace"
              className="flex items-center space-x-2 rounded-lg px-3 py-2 transition-colors hover:bg-muted"
            >
              <Package className="h-5 w-5 text-muted-foreground" />
              <span className="text-sm text-muted-foreground">Specs Marketplace</span>
            </Link>
            <a 
              href="https://github.com/mohidbt/apic" 
              target="_blank" 
              rel="noopener noreferrer"
              className="flex items-center space-x-2 rounded-lg px-3 py-2 transition-colors hover:bg-muted"
            >
              <Github className="h-5 w-5 text-muted-foreground" />
              <span className="text-sm text-muted-foreground">GitHub</span>
              {starCount > 0 && (
                <div className="flex items-center">
                  <Star className="h-4 w-4 fill-primary text-primary" />
                  <span className="ml-1 text-sm text-muted-foreground">{starCount}</span>
                </div>
              )}
            </a>
            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="relative flex min-h-[calc(100vh-4rem)] items-center justify-center px-4 py-16">
        <div className="relative z-10 mx-auto w-full max-w-4xl">
          {/* Title Section */}
          <div className="mb-8 text-center">
            <h1 className="mb-4 text-6xl font-bold tracking-tight text-foreground md:text-7xl">
              API Docs
              <br />
              as LLM Skills
            </h1>
            <p className="mx-auto mb-2 max-w-2xl text-lg text-muted-foreground">
            Let LLMs finally understand API Docs.
            </p>
            <p className="mx-auto max-w-2xl text-lg text-muted-foreground">
              Just insert your API specs (YAML, YML, or JSON) and get LLM-Ready Markdown back.
              Or use the marketplace download ready-made API-Skills.
            </p>
          </div>

          {/* File Upload Container */}
          <div className="rounded-3xl border-4 border-border bg-card p-8 shadow-xl md:p-12">
            {/* Hidden File Input */}
            <input
              ref={fileInputRef}
              type="file"
              accept=".yaml,.yml,.json"
              onChange={handleFileChange}
              className="hidden"
            />

            {/* Upload Area */}
            <div 
              onClick={handleUploadClick}
              onDragOver={handleDragOver}
              onDrop={handleDrop}
              className="mb-6 cursor-pointer rounded-2xl border-4 border-dashed border-muted bg-background p-12 text-center transition-all hover:border-accent hover:bg-muted"
            >
              <div className="mx-auto mb-4 flex h-20 w-20 items-center justify-center rounded-full bg-muted">
                {selectedFile ? (
                  <FileText className="h-10 w-10 text-muted-foreground" />
                ) : (
                  <Upload className="h-10 w-10 text-muted-foreground" />
                )}
              </div>
              
              {selectedFile ? (
                <div>
                  <p className="mb-2 text-lg text-foreground">
                    {selectedFile.name}
                  </p>
                  <p className="text-sm text-muted-foreground">
                    {(selectedFile.size / 1024).toFixed(2)} KB
                  </p>
                  <p className="mt-2 text-xs text-muted-foreground">
                    Click to select a different file
                  </p>
                </div>
              ) : (
                <div>
                  <p className="mb-2 text-lg text-foreground">
                    Click to upload or drag and drop
                  </p>
                  <p className="text-sm text-muted-foreground">
                    YAML, YML, or JSON files only
                  </p>
                </div>
              )}
            </div>

            {/* Convert Button */}
            <div className="mb-8 flex justify-center">
              <Button
                onClick={handleConvert}
                disabled={!selectedFile || isUploading}
                size="lg"
                className="h-14 rounded-xl px-12 text-lg shadow-md"
              >
                {isUploading ? (
                  <>
                    <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                    Converting...
                  </>
                ) : (
                  'Convert'
                )}
              </Button>
            </div>

            {/* Example Files Notice */}
            <div className="space-y-4">
              <p className="text-center text-sm text-card-foreground">
                Upload your OpenAPI specification file (YAML/YML/JSON) and get LLM-optimized Markdown
              </p>
              <div className="rounded-lg border-2 border-border bg-background p-4 text-center">
                <p className="mb-2 text-sm font-bold text-muted-foreground">
                  ✨ Why LLMs not only love, but actually need this ✨ 
                </p>
                <ul className="space-y-1 text-xs text-muted-foreground">
                  <li>Dereferences $ref schemas</li>
                  <li>Generates runnable curl examples</li>
                  <li>Organized by tags and endpoints</li>
                  <li>Includes authentication details</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
