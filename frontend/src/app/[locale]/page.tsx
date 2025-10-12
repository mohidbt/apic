'use client'

import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Checkbox } from '@/components/ui/checkbox'
import { Github, Sparkles, Star, Upload, FileText, Loader2 } from 'lucide-react'
import { useState, useRef } from 'react'
import { toast } from 'sonner'

export default function HomePage() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [isUploading, setIsUploading] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      // Validate file type
      const validExtensions = ['.yaml', '.yml', '.json']
      const fileExtension = file.name.substring(file.name.lastIndexOf('.')).toLowerCase()
      
      if (!validExtensions.includes(fileExtension)) {
        toast.error('Invalid file type. Please upload a YAML or JSON file.')
        return
      }
      
      setSelectedFile(file)
      toast.success(`File selected: ${file.name}`)
    }
  }

  const handleUploadClick = () => {
    fileInputRef.current?.click()
  }

  const handleConvert = async () => {
    if (!selectedFile) {
      toast.error('Please select a file first')
      return
    }

    setIsUploading(true)
    const formData = new FormData()
    formData.append('file', selectedFile)

    // Use environment variable for API URL, fallback to localhost for development
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

    try {
      const response = await fetch(`${apiUrl}/convert`, {
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
      toast.error(error instanceof Error ? error.message : 'Failed to convert file')
    } finally {
      setIsUploading(false)
    }
  }

  return (
    <div className="min-h-screen bg-[#f5f3ef] dark:bg-slate-950">
      {/* Header */}
      <header className="border-b border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-900">
        <div className="container mx-auto flex h-16 items-center justify-between px-4">
          <div className="flex items-center space-x-2">
            <span className="text-2xl font-bold">
              <span className="text-slate-900 dark:text-white">API</span>
              <span className="text-red-500">Ingest</span>
            </span>
          </div>
          <div className="flex items-center space-x-2">
            <Github className="h-5 w-5 text-slate-700 dark:text-slate-300" />
            <span className="text-sm font-medium text-slate-700 dark:text-slate-300">GitHub</span>
            <div className="flex items-center">
              <Star className="h-4 w-4 fill-yellow-400 text-yellow-400" />
              <span className="ml-1 text-sm font-medium text-slate-700 dark:text-slate-300">.</span>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="relative flex min-h-[calc(100vh-4rem)] items-center justify-center px-4 py-16">
        {/* Left Sparkle Decoration */}
        <div className="absolute left-[10%] top-[35%] hidden lg:block">
          <div className="relative">
            <Sparkles className="h-16 w-16 text-red-400" fill="currentColor" />
            <div className="absolute -right-2 -top-2">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" className="text-red-400">
                <path d="M12 2L13.5 8.5L20 10L13.5 11.5L12 18L10.5 11.5L4 10L10.5 8.5L12 2Z" fill="currentColor"/>
              </svg>
            </div>
          </div>
        </div>

        {/* Right Sparkle Decoration */}
        <div className="absolute right-[10%] top-[40%] hidden lg:block">
          <div className="relative">
            <Sparkles className="h-16 w-16 text-green-400" fill="currentColor" />
            <div className="absolute -left-2 -top-2">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" className="text-green-400">
                <path d="M12 2L13.5 8.5L20 10L13.5 11.5L12 18L10.5 11.5L4 10L10.5 8.5L12 2Z" fill="currentColor"/>
              </svg>
            </div>
          </div>
        </div>

        {/* Bottom Left Icon */}
        <div className="absolute bottom-[15%] left-[8%] hidden lg:block">
          <svg width="80" height="80" viewBox="0 0 80 80" fill="none" className="text-green-500">
            <path d="M40 10C40 10 25 20 20 40C25 60 40 70 40 70C40 70 55 60 60 40C55 20 40 10 40 10Z" fill="currentColor" opacity="0.6"/>
          </svg>
        </div>

        <div className="relative z-10 mx-auto w-full max-w-4xl">
          {/* Title Section */}
          <div className="mb-8 text-center">
            <h1 className="mb-4 text-6xl font-bold tracking-tight text-slate-900 dark:text-white md:text-7xl">
              LLM-Ready
              <br />
              API Docs
            </h1>
            <p className="mx-auto mb-2 max-w-2xl text-lg text-slate-600 dark:text-slate-400">
            Let LLMs finally understand API Docs.
            </p>
            <p className="mx-auto max-w-2xl text-lg text-slate-600 dark:text-slate-400">
              Just insert your YAML or JSON API spec and get LLM-Ready Markdown back.
            </p>
          </div>

          {/* File Upload Container */}
          <div className="rounded-3xl border-4 border-slate-900 bg-[#fdf8e8] p-8 shadow-xl dark:border-slate-700 dark:bg-slate-800 md:p-12">
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
              className="mb-6 cursor-pointer rounded-2xl border-4 border-dashed border-slate-300 bg-white p-12 text-center transition-all hover:border-slate-400 hover:bg-slate-50 dark:border-slate-600 dark:bg-slate-700 dark:hover:border-slate-500 dark:hover:bg-slate-650"
            >
              <div className="mx-auto mb-4 flex h-20 w-20 items-center justify-center rounded-full bg-slate-100 dark:bg-slate-600">
                {selectedFile ? (
                  <FileText className="h-10 w-10 text-slate-600 dark:text-slate-300" />
                ) : (
                  <Upload className="h-10 w-10 text-slate-600 dark:text-slate-300" />
                )}
              </div>
              
              {selectedFile ? (
                <div>
                  <p className="mb-2 text-lg font-semibold text-slate-900 dark:text-white">
                    {selectedFile.name}
                  </p>
                  <p className="text-sm text-slate-600 dark:text-slate-400">
                    {(selectedFile.size / 1024).toFixed(2)} KB
                  </p>
                  <p className="mt-2 text-xs text-slate-500 dark:text-slate-500">
                    Click to select a different file
                  </p>
                </div>
              ) : (
                <div>
                  <p className="mb-2 text-lg font-semibold text-slate-900 dark:text-white">
                    Click to upload or drag and drop
                  </p>
                  <p className="text-sm text-slate-600 dark:text-slate-400">
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
                className="h-14 rounded-xl bg-[#ffb366] px-12 text-lg font-semibold text-slate-900 shadow-md transition-all hover:bg-[#ffa347] disabled:cursor-not-allowed disabled:opacity-50 dark:bg-[#ffb366] dark:text-slate-900 dark:hover:bg-[#ffa347]"
              >
                {isUploading ? (
                  <>
                    <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                    Converting...
                  </>
                ) : (
                  'Convert to Markdown'
                )}
              </Button>
            </div>

            {/* Example Files Notice */}
            <div className="space-y-4">
              <p className="text-center text-sm font-medium text-slate-700 dark:text-slate-300">
                Upload your OpenAPI specification file (YAML/JSON) and get LLM-ready Markdown
              </p>
              <div className="rounded-lg border-2 border-slate-200 bg-white p-4 dark:border-slate-600 dark:bg-slate-700">
                <p className="mb-2 text-xs font-semibold text-slate-600 dark:text-slate-400">
                  ✨ Features:
                </p>
                <ul className="space-y-1 text-xs text-slate-600 dark:text-slate-400">
                  <li>• Dereferences $ref schemas</li>
                  <li>• Generates runnable curl examples</li>
                  <li>• Organized by tags and endpoints</li>
                  <li>• Includes authentication details</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
