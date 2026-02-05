'use client'

import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Separator } from '@/components/ui/separator'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Download, FileText, Code, Calendar, Package, User, Database } from 'lucide-react'
import { SpecDetail } from '@/types/api-spec'
import { formatFileSize, formatDate, downloadMarkdown, downloadOriginal } from '@/lib/api'
import { toast } from 'sonner'
import { useState } from 'react'

interface SpecDetailModalProps {
  spec: SpecDetail | null
  open: boolean
  onClose: () => void
}

export function SpecDetailModal({ spec, open, onClose }: SpecDetailModalProps) {
  const [downloading, setDownloading] = useState<'markdown' | 'original' | null>(null)
  const [isHovered, setIsHovered] = useState(false)

  if (!spec) return null

  const handleDownloadMarkdown = async () => {
    setDownloading('markdown')
    try {
      await downloadMarkdown(spec.id, spec.name, spec.version)
      toast.success('Markdown downloaded successfully')
    } catch (error) {
      toast.error('Failed to download markdown')
      console.error(error)
    } finally {
      setDownloading(null)
    }
  }

  const handleDownloadOriginal = async () => {
    setDownloading('original')
    try {
      await downloadOriginal(spec.id, spec.name, spec.version, spec.original_format || 'yaml')
      toast.success('Original file downloaded successfully')
    } catch (error) {
      toast.error('Failed to download original file')
      console.error(error)
    } finally {
      setDownloading(null)
    }
  }

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent 
        className={`max-w-4xl max-h-[90vh] flex flex-col overflow-hidden border-2 transition-shadow duration-300 ${
          isHovered 
            ? 'shadow-[0_25px_100px_-20px_rgba(0,0,0,0.6)] dark:shadow-[0_25px_100px_-20px_rgba(255,255,255,0.15)]' 
            : 'shadow-2xl'
        }`}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        <DialogHeader className="pb-4 border-b">
          <DialogTitle className="text-2xl font-bold bg-gradient-to-r from-foreground to-muted-foreground bg-clip-text">{spec.name}</DialogTitle>
        </DialogHeader>

        <ScrollArea className="flex-1 pr-4">
          <div className="space-y-6 py-4">
            {/* Metadata Section */}
            <div className="grid grid-cols-2 gap-4">
              <div className="flex items-center space-x-3 p-3 rounded-lg bg-muted/30 hover:bg-muted/50 transition-colors">
                <div className="p-2 rounded-md bg-primary/10">
                  <Package className="h-4 w-4 text-primary" />
                </div>
                <div>
                  <p className="text-xs text-muted-foreground">Version</p>
                  <p className="text-sm font-medium">{spec.version}</p>
                </div>
              </div>

              {spec.provider && (
                <div className="flex items-center space-x-3 p-3 rounded-lg bg-muted/30 hover:bg-muted/50 transition-colors">
                  <div className="p-2 rounded-md bg-primary/10">
                    <User className="h-4 w-4 text-primary" />
                  </div>
                  <div>
                    <p className="text-xs text-muted-foreground">Provider</p>
                    <p className="text-sm font-medium">{spec.provider}</p>
                  </div>
                </div>
              )}

              <div className="flex items-center space-x-3 p-3 rounded-lg bg-muted/30 hover:bg-muted/50 transition-colors">
                <div className="p-2 rounded-md bg-primary/10">
                  <Calendar className="h-4 w-4 text-primary" />
                </div>
                <div>
                  <p className="text-xs text-muted-foreground">Uploaded</p>
                  <p className="text-sm font-medium">{formatDate(spec.uploaded_at)}</p>
                </div>
              </div>

              <div className="flex items-center space-x-3 p-3 rounded-lg bg-muted/30 hover:bg-muted/50 transition-colors">
                <div className="p-2 rounded-md bg-primary/10">
                  <Database className="h-4 w-4 text-primary" />
                </div>
                <div>
                  <p className="text-xs text-muted-foreground">File Size</p>
                  <p className="text-sm font-medium">{formatFileSize(spec.file_size_bytes)}</p>
                </div>
              </div>

              {spec.original_filename && (
                <div className="flex items-center space-x-3 p-3 rounded-lg bg-muted/30 hover:bg-muted/50 transition-colors">
                  <div className="p-2 rounded-md bg-primary/10">
                    <FileText className="h-4 w-4 text-primary" />
                  </div>
                  <div className="min-w-0 flex-1">
                    <p className="text-xs text-muted-foreground">Original File</p>
                    <p className="text-sm font-medium truncate">{spec.original_filename}</p>
                  </div>
                </div>
              )}

              {spec.original_format && (
                <div className="flex items-center space-x-3 p-3 rounded-lg bg-muted/30 hover:bg-muted/50 transition-colors">
                  <div className="p-2 rounded-md bg-primary/10">
                    <Code className="h-4 w-4 text-primary" />
                  </div>
                  <div>
                    <p className="text-xs text-muted-foreground">Format</p>
                    <p className="text-sm font-medium uppercase">{spec.original_format}</p>
                  </div>
                </div>
              )}
            </div>

            {/* Tags */}
            {spec.tags && spec.tags.length > 0 && (
              <div className="p-4 rounded-lg bg-muted/30">
                <p className="text-xs text-muted-foreground mb-3 font-semibold">Tags</p>
                <div className="flex flex-wrap gap-2">
                  {spec.tags.map((tag) => (
                    <Badge key={tag} variant="secondary" className="hover:bg-primary/20 transition-colors">
                      {tag}
                    </Badge>
                  ))}
                </div>
              </div>
            )}

            <Separator className="my-4" />

            {/* Download Buttons */}
            <div className="flex gap-3 px-1">
              <Button
                onClick={handleDownloadMarkdown}
                disabled={downloading !== null}
                className="flex-1 shadow-md hover:shadow-lg transition-all duration-200 hover:scale-[1.02] active:scale-[0.98]"
              >
                <Download className="mr-2 h-4 w-4" />
                {downloading === 'markdown' ? 'Downloading...' : 'Download Markdown'}
              </Button>
              <Button
                onClick={handleDownloadOriginal}
                disabled={downloading !== null}
                variant="outline"
                className="flex-1 shadow-md hover:shadow-lg transition-all duration-200 hover:scale-[1.02] active:scale-[0.98]"
              >
                <Download className="mr-2 h-4 w-4" />
                {downloading === 'original' ? 'Downloading...' : 'Download Original'}
              </Button>
            </div>

            <Separator className="my-4" />

            {/* Markdown Preview */}
            <div>
              <p className="text-sm font-semibold mb-3 flex items-center gap-2">
                <FileText className="h-4 w-4 text-primary" />
                Markdown Preview
              </p>
              <div className="rounded-lg border-2 bg-muted/50 shadow-inner hover:shadow-md transition-shadow max-h-[600px] overflow-auto scrollbar-thin">
                <pre className="text-xs whitespace-pre-wrap font-mono p-4 min-w-0 break-words">
                  {spec.markdown_content}
                </pre>
              </div>
            </div>
          </div>
        </ScrollArea>
      </DialogContent>
    </Dialog>
  )
}

