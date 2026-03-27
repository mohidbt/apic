'use client'

import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'
import {
import { Skeleton } from '@/components/ui/skeleton'
import { AppHeader } from '@/components/app-header'
import { SpecDetailModal } from '@/components/spec-detail-modal'
import { Search, ChevronLeft, ChevronRight, Package, Trash2 } from 'lucide-react'
import { ApiSpec, SpecDetail } from '@/types/api-spec'
import { fetchSpecs, fetchSpecDetail, formatFileSize, formatDate, formatTokenCount, deleteSpec } from '@/lib/api'
import { toast } from 'sonner'
import { Link } from '@/i18n/navigation'
import { useAuth } from '@/lib/auth-context'

type TabType = 'recent' | 'trending' | 'popular'

interface MarketplaceClientProps {
  initialSpecs: ApiSpec[]
  initialTotal: number
  starCount: number
}

export function MarketplaceClient({ initialSpecs, initialTotal, starCount }: MarketplaceClientProps) {
  const { user } = useAuth()
  const [specs, setSpecs] = useState<ApiSpec[]>(initialSpecs)
  const [searchQuery, setSearchQuery] = useState('')
  const [currentPage, setCurrentPage] = useState(1)
  const [totalPages, setTotalPages] = useState(Math.ceil(initialTotal / 20))
  const [totalSpecs, setTotalSpecs] = useState(initialTotal)
  const [loading, setLoading] = useState(false)
  const [activeTab, setActiveTab] = useState<TabType>('recent')
  const [selectedSpec, setSelectedSpec] = useState<SpecDetail | null>(null)
  const [modalOpen, setModalOpen] = useState(false)
  const isAdmin = !!user?.is_admin
  
  const pageSize = 20

  // Fetch specs when filters change (skip initial load since we have server data)
  useEffect(() => {
    // Skip the initial load - we already have data from the server
    if (currentPage === 1 && searchQuery === '') {
      return
    }

    const loadSpecs = async () => {
      setLoading(true)
      
      try {
        const search = searchQuery.trim() || undefined
        
        const data = await fetchSpecs(currentPage, pageSize, search)
        setSpecs(data.specs)
        setTotalSpecs(data.total)
        setTotalPages(Math.ceil(data.total / pageSize))
      } catch (error) {
        console.error('Failed to fetch specs:', error)
        toast.error('Failed to load specs')
      } finally {
        setLoading(false)
      }
    }
    loadSpecs()
  }, [currentPage, searchQuery, activeTab])

  // Handle search input with debounce
  const handleSearchChange = (value: string) => {
    setSearchQuery(value)
    setCurrentPage(1) // Reset to first page
  }

  // Handle row click to open detail modal
  const handleRowClick = async (spec: ApiSpec) => {
    try {
      const detail = await fetchSpecDetail(spec.id)
      setSelectedSpec(detail)
      setModalOpen(true)
    } catch (error) {
      console.error('Failed to fetch spec detail:', error)
      toast.error('Failed to load spec details')
    }
  }

  const handleDeleteSpec = async (spec: ApiSpec) => {
    if (!isAdmin) {
      toast.error('Admin access required')
      return
    }
    const confirmed = window.confirm(`Delete "${spec.name} v${spec.version}" from the marketplace?`)
    if (!confirmed) return

    try {
      await deleteSpec(spec.id)
      setSpecs((prev) => prev.filter((s) => s.id !== spec.id))
      setTotalSpecs((prev) => Math.max(0, prev - 1))
      toast.success('Spec deleted')
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to delete spec'
      toast.error(message)
    }
  }

  // Pagination handlers
  const handlePreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1)
    }
  }

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1)
    }
  }

  return (
    <div className="min-h-screen bg-background">
      <AppHeader starCount={starCount} />

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {/* Title Section */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold mb-2">Specs Marketplace</h1>
          <p className="text-lg text-muted-foreground">
            Browse and download LLM-ready API documentation
          </p>
        </div>

        {/* Search Bar */}
        <div className="mb-6 flex flex-col sm:flex-row gap-4">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-muted-foreground" />
            <Input
              type="text"
              placeholder="Search APIs..."
              value={searchQuery}
              onChange={(e) => handleSearchChange(e.target.value)}
              className="pl-10"
            />
          </div>
        </div>

        {/* Tabs */}
        <Tabs value={activeTab} onValueChange={(v) => setActiveTab(v as TabType)} className="mb-6">
          <TabsList className="w-full max-w-full justify-start overflow-x-auto">
            <TabsTrigger value="recent">Recent</TabsTrigger>
            <TabsTrigger value="trending">Trending</TabsTrigger>
            <TabsTrigger value="popular">Popular</TabsTrigger>
          </TabsList>

          <TabsContent value="recent" className="mt-6">
            <SpecsTable
              specs={specs}
              loading={loading}
              onRowClick={handleRowClick}
              isAdmin={isAdmin}
              onDeleteSpec={handleDeleteSpec}
            />
          </TabsContent>

          <TabsContent value="trending" className="mt-6">
            <SpecsTable
              specs={specs}
              loading={loading}
              onRowClick={handleRowClick}
              isAdmin={isAdmin}
              onDeleteSpec={handleDeleteSpec}
            />
          </TabsContent>

          <TabsContent value="popular" className="mt-6">
            <SpecsTable
              specs={specs}
              loading={loading}
              onRowClick={handleRowClick}
              isAdmin={isAdmin}
              onDeleteSpec={handleDeleteSpec}
            />
          </TabsContent>
        </Tabs>

        {/* Pagination */}
        {!loading && totalSpecs > 0 && (
          <div className="flex flex-col sm:flex-row items-center justify-between mt-6 gap-4">
            <p className="text-sm text-muted-foreground">
              Showing {(currentPage - 1) * pageSize + 1} to{' '}
              {Math.min(currentPage * pageSize, totalSpecs)} of {totalSpecs} specs
            </p>
            <div className="flex items-center space-x-2">
              <Button
                variant="outline"
                size="sm"
                onClick={handlePreviousPage}
                disabled={currentPage === 1}
              >
                <ChevronLeft className="h-4 w-4 sm:mr-1" />
                <span className="hidden sm:inline">Previous</span>
              </Button>
              <span className="text-sm px-2">
                {currentPage} / {totalPages}
              </span>
              <Button
                variant="outline"
                size="sm"
                onClick={handleNextPage}
                disabled={currentPage === totalPages}
              >
                <span className="hidden sm:inline">Next</span>
                <ChevronRight className="h-4 w-4 sm:ml-1" />
              </Button>
            </div>
          </div>
        )}

        {/* Empty State */}
        {!loading && specs.length === 0 && (
          <div className="text-center py-12">
            <Package className="h-12 w-12 mx-auto mb-4 text-muted-foreground" />
            <h3 className="text-lg font-medium mb-2">No specs found</h3>
            <p className="text-muted-foreground mb-4">
              {searchQuery
                ? 'Try adjusting your search or filters'
                : 'No API specs have been uploaded yet'}
            </p>
            <Link href="/">
              <Button>Upload Your First Spec</Button>
            </Link>
          </div>
        )}
      </main>

      {/* Detail Modal */}
      <SpecDetailModal
        spec={selectedSpec}
        open={modalOpen}
        onClose={() => setModalOpen(false)}
      />
    </div>
  )
}

// Specs Table Component
interface SpecsTableProps {
  specs: ApiSpec[]
  loading: boolean
  onRowClick: (spec: ApiSpec) => void
  isAdmin: boolean
  onDeleteSpec: (spec: ApiSpec) => void
}

function SpecsTable({ specs, loading, onRowClick, isAdmin, onDeleteSpec }: SpecsTableProps) {
  if (loading) {
    return (
      <div className="rounded-lg border">
        <div className="overflow-x-auto">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>NAME</TableHead>
                <TableHead className="hidden md:table-cell">PROVIDER</TableHead>
                <TableHead>VERSION</TableHead>
                <TableHead className="hidden lg:table-cell">UPLOADED</TableHead>
                <TableHead className="hidden sm:table-cell">SIZE</TableHead>
                <TableHead className="hidden lg:table-cell">TOKENS</TableHead>
                {isAdmin && <TableHead className="w-16">ACTIONS</TableHead>}
              </TableRow>
            </TableHeader>
            <TableBody>
              {[...Array(5)].map((_, i) => (
                <TableRow key={i}>
                  <TableCell><Skeleton className="h-4 w-32" /></TableCell>
                  <TableCell className="hidden md:table-cell"><Skeleton className="h-4 w-24" /></TableCell>
                  <TableCell><Skeleton className="h-4 w-16" /></TableCell>
                  <TableCell className="hidden lg:table-cell"><Skeleton className="h-4 w-20" /></TableCell>
                  <TableCell className="hidden sm:table-cell"><Skeleton className="h-4 w-16" /></TableCell>
                  <TableCell className="hidden lg:table-cell"><Skeleton className="h-4 w-14" /></TableCell>
                  {isAdmin && <TableCell><Skeleton className="h-8 w-8" /></TableCell>}
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </div>
    )
  }

  // Never show empty table with just headers - parent renders Empty State
  if (specs.length === 0) {
    return null
  }

  return (
    <div className="rounded-lg border overflow-hidden">
      <div className="overflow-x-auto">
        <Table>
          <TableHeader>
            <TableRow className="bg-muted/50">
              <TableHead className="font-semibold">NAME</TableHead>
              <TableHead className="font-semibold hidden md:table-cell">PROVIDER</TableHead>
              <TableHead className="font-semibold">VERSION</TableHead>
              <TableHead className="font-semibold hidden lg:table-cell">UPLOADED</TableHead>
              <TableHead className="font-semibold hidden sm:table-cell">SIZE</TableHead>
              <TableHead className="font-semibold hidden lg:table-cell">TOKENS</TableHead>
              {isAdmin && <TableHead className="font-semibold w-16">ACTIONS</TableHead>}
            </TableRow>
          </TableHeader>
          <TableBody>
            {specs.map((spec) => (
              <TableRow
                key={spec.id}
                tabIndex={0}
                role="button"
                className="cursor-pointer hover:bg-muted/50 transition-colors"
                onClick={() => onRowClick(spec)}
                onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onRowClick(spec) } }}
              >
                <TableCell className="font-medium">
                  <div className="flex flex-col">
                    <span>{spec.name}</span>
                    <span className="text-xs text-muted-foreground md:hidden">
                      {spec.provider || 'N/A'}
                    </span>
                  </div>
                </TableCell>
                <TableCell className="text-muted-foreground hidden md:table-cell">
                  {spec.provider || 'N/A'}
                </TableCell>
                <TableCell>{spec.version}</TableCell>
                <TableCell className="text-muted-foreground hidden lg:table-cell">
                  {formatDate(spec.uploaded_at)}
                </TableCell>
                <TableCell className="text-muted-foreground hidden sm:table-cell">
                  {formatFileSize(spec.file_size_bytes)}
                </TableCell>
                <TableCell className="text-muted-foreground hidden lg:table-cell">
                  {formatTokenCount(spec.token_count)}
                </TableCell>
                {isAdmin && (
                  <TableCell>
                    <Button
                      variant="ghost"
                      size="icon"
                      className="text-destructive hover:text-destructive"
                      onClick={(e) => {
                        e.stopPropagation()
                        onDeleteSpec(spec)
                      }}
                    >
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  </TableCell>
                )}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  )
}
