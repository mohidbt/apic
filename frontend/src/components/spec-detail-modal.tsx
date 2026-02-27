'use client'

import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Separator } from '@/components/ui/separator'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Input } from '@/components/ui/input'
import {
  Download, FileText, Code, Calendar, Package, User, Database, Hash,
  ChevronRight, Search, Copy, Check, Loader2, Layers, Wrench, Tag as TagIcon,
  Box, Braces
} from 'lucide-react'
import { ChunkedSpec, SpecDetail, ToolSchema } from '@/types/api-spec'
import { formatFileSize, formatDate, formatTokenCount, downloadMarkdown, downloadOriginal, fetchSpecChunks, fetchSpecTools } from '@/lib/api'
import { toast } from 'sonner'
import { useCallback, useEffect, useRef, useState } from 'react'

interface SpecDetailModalProps {
  spec: SpecDetail | null
  open: boolean
  onClose: () => void
}

export function SpecDetailModal({ spec, open, onClose }: SpecDetailModalProps) {
  const [downloading, setDownloading] = useState<'markdown' | 'original' | null>(null)
  const [activeTab, setActiveTab] = useState('overview')
  const scrollRef = useRef<HTMLDivElement>(null)

  // Chunks state
  const [chunks, setChunks] = useState<ChunkedSpec | null>(null)
  const [chunksLoading, setChunksLoading] = useState(false)
  const [chunksError, setChunksError] = useState<string | null>(null)
  const [chunkFilter, setChunkFilter] = useState('')
  const [expandedChunk, setExpandedChunk] = useState<string | null>(null)
  const [activeChunkSection, setActiveChunkSection] = useState<'tags' | 'endpoints' | 'schemas'>('endpoints')

  // Tools state
  const [tools, setTools] = useState<ToolSchema[] | null>(null)
  const [toolsLoading, setToolsLoading] = useState(false)
  const [toolsError, setToolsError] = useState<string | null>(null)
  const [expandedTool, setExpandedTool] = useState<string | null>(null)
  const [copiedTool, setCopiedTool] = useState<string | null>(null)

  // Reset state when spec changes
  useEffect(() => {
    if (!open) {
      setActiveTab('overview')
      setChunks(null)
      setChunksError(null)
      setChunkFilter('')
      setExpandedChunk(null)
      setTools(null)
      setToolsError(null)
      setExpandedTool(null)
    }
  }, [open])

  const loadChunks = useCallback(async () => {
    if (!spec || chunks || chunksLoading) return
    setChunksLoading(true)
    setChunksError(null)
    try {
      const data = await fetchSpecChunks(spec.id)
      setChunks(data)
    } catch (e) {
      setChunksError(e instanceof Error ? e.message : 'Failed to load chunks')
    } finally {
      setChunksLoading(false)
    }
  }, [spec, chunks, chunksLoading])

  const loadTools = useCallback(async () => {
    if (!spec || tools || toolsLoading) return
    setToolsLoading(true)
    setToolsError(null)
    try {
      const data = await fetchSpecTools(spec.id)
      setTools(data)
    } catch (e) {
      setToolsError(e instanceof Error ? e.message : 'Failed to load tool schemas')
    } finally {
      setToolsLoading(false)
    }
  }, [spec, tools, toolsLoading])

  useEffect(() => {
    if (activeTab === 'chunks') loadChunks()
    if (activeTab === 'tools') loadTools()
  }, [activeTab, loadChunks, loadTools])

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

  const handleCopyTool = async (tool: ToolSchema) => {
    try {
      await navigator.clipboard.writeText(JSON.stringify(tool, null, 2))
      setCopiedTool(tool.name)
      toast.success(`Copied ${tool.name} schema`)
      setTimeout(() => setCopiedTool(null), 2000)
    } catch {
      toast.error('Failed to copy')
    }
  }

  const getFilteredItems = (items: Record<string, string>) => {
    if (!chunkFilter) return Object.keys(items)
    const q = chunkFilter.toLowerCase()
    return Object.keys(items).filter(k => k.toLowerCase().includes(q))
  }

  const sectionData = chunks ? {
    tags: { items: chunks.tags, icon: TagIcon, label: 'Tags' },
    endpoints: { items: chunks.endpoints, icon: Braces, label: 'Endpoints' },
    schemas: { items: chunks.schemas, icon: Box, label: 'Schemas' },
  } as const : null

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent
        onOverlayWheel={(event) => {
          if (!scrollRef.current) return
          event.preventDefault()
          scrollRef.current.scrollBy({ top: event.deltaY })
        }}
        className="max-w-4xl max-h-[90vh] flex flex-col overflow-hidden border-2 transition-shadow duration-300 shadow-[0_18px_60px_-20px_rgba(0,160,0,0.55)] dark:shadow-[0_18px_60px_-20px_rgba(34,255,34,0.55)] hover:shadow-[0_25px_100px_-20px_rgba(0,160,0,0.75)] dark:hover:shadow-[0_25px_100px_-20px_rgba(34,255,34,0.75)]"
      >
        <DialogHeader className="pb-4 border-b">
          <DialogTitle className="text-2xl font-bold bg-gradient-to-r from-foreground to-muted-foreground bg-clip-text">
            {spec.name}
          </DialogTitle>
        </DialogHeader>

        <Tabs value={activeTab} onValueChange={setActiveTab} className="flex-1 flex flex-col min-h-0">
          <TabsList className="w-full justify-start gap-1 bg-transparent border-b rounded-none px-0 h-auto pb-0">
            <TabsTrigger
              value="overview"
              className="rounded-b-none data-[state=active]:shadow-none data-[state=active]:border-b-2 data-[state=active]:border-primary gap-1.5"
            >
              <FileText className="h-3.5 w-3.5" />
              Overview
            </TabsTrigger>
            <TabsTrigger
              value="chunks"
              className="rounded-b-none data-[state=active]:shadow-none data-[state=active]:border-b-2 data-[state=active]:border-primary gap-1.5"
            >
              <Layers className="h-3.5 w-3.5" />
              Chunks
            </TabsTrigger>
            <TabsTrigger
              value="tools"
              className="rounded-b-none data-[state=active]:shadow-none data-[state=active]:border-b-2 data-[state=active]:border-primary gap-1.5"
            >
              <Wrench className="h-3.5 w-3.5" />
              Tool Schemas
            </TabsTrigger>
            <TabsTrigger
              value="markdown"
              className="rounded-b-none data-[state=active]:shadow-none data-[state=active]:border-b-2 data-[state=active]:border-primary gap-1.5"
            >
              <Code className="h-3.5 w-3.5" />
              Full Markdown
            </TabsTrigger>
          </TabsList>

          <div ref={scrollRef} className="flex-1 overflow-y-auto pr-2 min-h-0">

            {/* ── Overview Tab ── */}
            <TabsContent value="overview" className="mt-0 pt-4">
              <div className="space-y-6">
                <div className="grid grid-cols-2 gap-4">
                  <MetaCard icon={Package} label="Version" value={spec.version} />
                  {spec.provider && <MetaCard icon={User} label="Provider" value={spec.provider} />}
                  <MetaCard icon={Calendar} label="Uploaded" value={formatDate(spec.uploaded_at)} />
                  <MetaCard icon={Database} label="File Size" value={formatFileSize(spec.file_size_bytes)} />
                  <MetaCard icon={Hash} label="Token Count" value={formatTokenCount(spec.token_count)} />
                  {spec.original_filename && <MetaCard icon={FileText} label="Original File" value={spec.original_filename} truncate />}
                  {spec.original_format && <MetaCard icon={Code} label="Format" value={spec.original_format.toUpperCase()} />}
                </div>

                {spec.tags && spec.tags.length > 0 && (
                  <div className="p-4 rounded-lg bg-muted/30">
                    <p className="text-xs text-muted-foreground mb-3 font-semibold">Tags</p>
                    <div className="flex flex-wrap gap-2">
                      {spec.tags.map((tag) => (
                        <Badge key={tag} variant="outline" className="hover:bg-muted transition-colors">
                          {tag}
                        </Badge>
                      ))}
                    </div>
                  </div>
                )}

                <Separator />

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
              </div>
            </TabsContent>

            {/* ── Chunks Tab ── */}
            <TabsContent value="chunks" className="mt-0 pt-4">
              {chunksLoading && (
                <div className="flex items-center justify-center py-20">
                  <Loader2 className="h-6 w-6 animate-spin text-muted-foreground" />
                  <span className="ml-3 text-sm text-muted-foreground">Converting spec to chunks...</span>
                </div>
              )}

              {chunksError && (
                <div className="text-center py-20">
                  <p className="text-sm text-destructive">{chunksError}</p>
                  <Button variant="outline" size="sm" className="mt-3" onClick={() => { setChunks(null); setChunksError(null) }}>
                    Retry
                  </Button>
                </div>
              )}

              {chunks && (
                <div className="space-y-4">
                  {/* Manifest */}
                  <div className="rounded-lg border bg-muted/30">
                    <button
                      className="w-full flex items-center justify-between p-3 text-left hover:bg-muted/50 transition-colors rounded-lg"
                      onClick={() => setExpandedChunk(expandedChunk === '__manifest__' ? null : '__manifest__')}
                    >
                      <span className="text-sm font-semibold flex items-center gap-2">
                        <FileText className="h-4 w-4 text-primary" />
                        Manifest
                      </span>
                      <ChevronRight className={`h-4 w-4 text-muted-foreground transition-transform duration-200 ${expandedChunk === '__manifest__' ? 'rotate-90' : ''}`} />
                    </button>
                    {expandedChunk === '__manifest__' && (
                      <div className="border-t px-3 pb-3">
                        <pre className="text-xs whitespace-pre-wrap font-mono pt-3 break-words">{chunks.manifest}</pre>
                      </div>
                    )}
                  </div>

                  {/* Filter + section picker */}
                  <div className="flex items-center gap-2">
                    <div className="relative flex-1">
                      <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-muted-foreground" />
                      <Input
                        placeholder="Filter by name..."
                        value={chunkFilter}
                        onChange={(e) => setChunkFilter(e.target.value)}
                        className="pl-9 h-9 text-sm"
                      />
                    </div>
                    <div className="flex rounded-lg border bg-muted/30 p-0.5">
                      {sectionData && (['tags', 'endpoints', 'schemas'] as const).map((key) => {
                        const sec = sectionData[key]
                        const count = Object.keys(sec.items).length
                        const Icon = sec.icon
                        return (
                          <button
                            key={key}
                            onClick={() => { setActiveChunkSection(key); setExpandedChunk(null) }}
                            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${
                              activeChunkSection === key
                                ? 'bg-background text-foreground shadow-sm'
                                : 'text-muted-foreground hover:text-foreground'
                            }`}
                          >
                            <Icon className="h-3.5 w-3.5" />
                            {sec.label}
                            <span className="text-[10px] opacity-60">{count}</span>
                          </button>
                        )
                      })}
                    </div>
                  </div>

                  {/* Chunk list */}
                  {sectionData && (() => {
                    const sec = sectionData[activeChunkSection]
                    const filtered = getFilteredItems(sec.items)
                    if (filtered.length === 0) {
                      return (
                        <div className="text-center py-10 text-sm text-muted-foreground">
                          {chunkFilter ? 'No matches found' : 'No items in this section'}
                        </div>
                      )
                    }
                    return (
                      <div className="space-y-1">
                        {filtered.map((key) => {
                          const isExpanded = expandedChunk === `${activeChunkSection}:${key}`
                          const chunkId = `${activeChunkSection}:${key}`
                          return (
                            <div key={chunkId} className="rounded-lg border bg-card overflow-hidden">
                              <button
                                className="w-full flex items-center justify-between p-3 text-left hover:bg-muted/50 transition-colors"
                                onClick={() => setExpandedChunk(isExpanded ? null : chunkId)}
                              >
                                <span className="text-sm font-medium font-mono truncate pr-2">{key}</span>
                                <ChevronRight className={`h-4 w-4 shrink-0 text-muted-foreground transition-transform duration-200 ${isExpanded ? 'rotate-90' : ''}`} />
                              </button>
                              {isExpanded && (
                                <div className="border-t">
                                  <div className="flex justify-end px-3 pt-2">
                                    <Button
                                      variant="ghost"
                                      size="sm"
                                      className="h-7 text-xs gap-1"
                                      onClick={async () => {
                                        await navigator.clipboard.writeText(sec.items[key])
                                        toast.success('Copied to clipboard')
                                      }}
                                    >
                                      <Copy className="h-3 w-3" /> Copy
                                    </Button>
                                  </div>
                                  <pre className="text-xs whitespace-pre-wrap font-mono px-3 pb-3 break-words max-h-[400px] overflow-y-auto">
                                    {sec.items[key]}
                                  </pre>
                                </div>
                              )}
                            </div>
                          )
                        })}
                      </div>
                    )
                  })()}
                </div>
              )}
            </TabsContent>

            {/* ── Tool Schemas Tab ── */}
            <TabsContent value="tools" className="mt-0 pt-4">
              {toolsLoading && (
                <div className="flex items-center justify-center py-20">
                  <Loader2 className="h-6 w-6 animate-spin text-muted-foreground" />
                  <span className="ml-3 text-sm text-muted-foreground">Generating tool schemas...</span>
                </div>
              )}

              {toolsError && (
                <div className="text-center py-20">
                  <p className="text-sm text-destructive">{toolsError}</p>
                  <Button variant="outline" size="sm" className="mt-3" onClick={() => { setTools(null); setToolsError(null) }}>
                    Retry
                  </Button>
                </div>
              )}

              {tools && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <p className="text-sm text-muted-foreground">
                      {tools.length} tool{tools.length !== 1 ? 's' : ''} available for function-calling
                    </p>
                    <Button
                      variant="outline"
                      size="sm"
                      className="h-8 text-xs gap-1.5"
                      onClick={async () => {
                        await navigator.clipboard.writeText(JSON.stringify(tools, null, 2))
                        toast.success('All tool schemas copied')
                      }}
                    >
                      <Copy className="h-3 w-3" /> Copy All
                    </Button>
                  </div>

                  <div className="space-y-1">
                    {tools.map((tool) => {
                      const isExpanded = expandedTool === tool.name
                      const paramCount = Object.keys(tool.parameters.properties || {}).length
                      const requiredCount = tool.parameters.required?.length ?? 0
                      return (
                        <div key={tool.name} className="rounded-lg border bg-card overflow-hidden">
                          <button
                            className="w-full flex items-center gap-3 p-3 text-left hover:bg-muted/50 transition-colors"
                            onClick={() => setExpandedTool(isExpanded ? null : tool.name)}
                          >
                            <Wrench className="h-4 w-4 shrink-0 text-primary" />
                            <div className="flex-1 min-w-0">
                              <div className="flex items-center gap-2">
                                <span className="text-sm font-mono font-medium truncate">{tool.name}</span>
                                <span className="text-[10px] text-muted-foreground shrink-0">
                                  {paramCount} param{paramCount !== 1 ? 's' : ''}
                                  {requiredCount > 0 && ` (${requiredCount} req)`}
                                </span>
                              </div>
                              <p className="text-xs text-muted-foreground truncate mt-0.5">{tool.description}</p>
                            </div>
                            <ChevronRight className={`h-4 w-4 shrink-0 text-muted-foreground transition-transform duration-200 ${isExpanded ? 'rotate-90' : ''}`} />
                          </button>
                          {isExpanded && (
                            <div className="border-t">
                              <div className="flex justify-end px-3 pt-2">
                                <Button
                                  variant="ghost"
                                  size="sm"
                                  className="h-7 text-xs gap-1"
                                  onClick={() => handleCopyTool(tool)}
                                >
                                  {copiedTool === tool.name ? <Check className="h-3 w-3" /> : <Copy className="h-3 w-3" />}
                                  {copiedTool === tool.name ? 'Copied' : 'Copy'}
                                </Button>
                              </div>
                              <pre className="text-xs whitespace-pre-wrap font-mono px-3 pb-3 break-words max-h-[400px] overflow-y-auto text-muted-foreground">
                                {JSON.stringify(tool, null, 2)}
                              </pre>
                            </div>
                          )}
                        </div>
                      )
                    })}
                  </div>
                </div>
              )}
            </TabsContent>

            {/* ── Full Markdown Tab ── */}
            <TabsContent value="markdown" className="mt-0 pt-4">
              <div className="rounded-lg border-2 bg-muted/50 shadow-inner hover:shadow-md transition-shadow h-[600px] overflow-y-auto overflow-x-hidden overscroll-contain w-full min-w-0 scrollbar-stable">
                <pre className="text-xs whitespace-pre-wrap font-mono p-4 w-full break-words">
                  {spec.markdown_content}
                </pre>
              </div>
            </TabsContent>

          </div>
        </Tabs>
      </DialogContent>
    </Dialog>
  )
}

function MetaCard({ icon: Icon, label, value, truncate }: {
  icon: React.ElementType
  label: string
  value: string
  truncate?: boolean
}) {
  return (
    <div className="flex items-center space-x-3 p-3 rounded-lg bg-muted/30 hover:bg-muted/50 transition-colors">
      <div className="p-2 rounded-md bg-primary/10">
        <Icon className="h-4 w-4 text-primary" />
      </div>
      <div className={truncate ? 'min-w-0 flex-1' : ''}>
        <p className="text-xs text-muted-foreground">{label}</p>
        <p className={`text-sm font-medium ${truncate ? 'truncate' : ''}`}>{value}</p>
      </div>
    </div>
  )
}
