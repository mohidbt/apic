'use client'

import { useEffect, useState } from 'react'
import { useAuth } from '@/lib/auth-context'
import { AppHeader } from '@/components/app-header'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'
import { Check, Copy, Key, Loader2, Plus, Trash2 } from 'lucide-react'
import { toast } from 'sonner'
import { formatDate } from '@/lib/api'

interface TokenInfo {
  id: number
  label: string
  created_at: string
  last_used_at: string | null
  is_revoked: boolean
}

export default function TokensPage() {
  const { user, isLoading: authLoading, login } = useAuth()
  const [tokens, setTokens] = useState<TokenInfo[]>([])
  const [loading, setLoading] = useState(true)
  const [creating, setCreating] = useState(false)
  const [newLabel, setNewLabel] = useState('')
  const [rawToken, setRawToken] = useState<string | null>(null)
  const [copied, setCopied] = useState(false)
  const [configCopied, setConfigCopied] = useState(false)
  const [dialogOpen, setDialogOpen] = useState(false)
  const [mcpUrl, setMcpUrl] = useState('https://api-ingest.com/mcp')

  const apiBase = process.env.NEXT_PUBLIC_API_URL || ''

  async function fetchTokens() {
    try {
      const res = await fetch(`${apiBase}/api/tokens`, { credentials: 'include' })
      if (res.ok) {
        const data = await res.json()
        setTokens(data.tokens)
      }
    } catch {
      toast.error('Failed to load tokens')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    if (user) fetchTokens()
    else if (!authLoading) setLoading(false)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [user, authLoading])

  useEffect(() => {
    if (typeof window === 'undefined') return
    const { protocol, hostname } = window.location
    setMcpUrl(`${protocol}//${hostname}/mcp`)
  }, [])

  async function handleCreate() {
    if (!newLabel.trim()) return
    setCreating(true)
    try {
      const res = await fetch(`${apiBase}/api/tokens`, {
        method: 'POST',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ label: newLabel.trim() }),
      })
      if (!res.ok) throw new Error('Failed to create token')
      const data = await res.json()
      setRawToken(data.token)
      setNewLabel('')
      fetchTokens()
    } catch {
      toast.error('Failed to create token')
    } finally {
      setCreating(false)
    }
  }

  async function handleRevoke(tokenId: number) {
    try {
      const res = await fetch(`${apiBase}/api/tokens/${tokenId}`, {
        method: 'DELETE',
        credentials: 'include',
      })
      if (!res.ok) throw new Error('Failed to revoke token')
      toast.success('Token revoked')
      fetchTokens()
    } catch {
      toast.error('Failed to revoke token')
    }
  }

  function handleCopy() {
    if (!rawToken) return
    navigator.clipboard.writeText(rawToken)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  function handleDialogClose(open: boolean) {
    setDialogOpen(open)
    if (!open) {
      setRawToken(null)
      setNewLabel('')
    }
  }

  const mcpConfigJson = JSON.stringify(
    {
      mcpServers: {
        APIIngest: {
          url: mcpUrl,
          headers: {
            Authorization: `Bearer ${rawToken ?? '<PASTE_MCP_TOKEN_HERE>'}`,
          },
        },
      },
    },
    null,
    2
  )

  function handleCopyConfig() {
    navigator.clipboard.writeText(mcpConfigJson)
    setConfigCopied(true)
    setTimeout(() => setConfigCopied(false), 2000)
  }

  if (authLoading || loading) {
    return (
      <div className="min-h-screen bg-background">
        <AppHeader />
        <div className="flex items-center justify-center py-32">
          <Loader2 className="h-6 w-6 animate-spin text-muted-foreground" />
        </div>
      </div>
    )
  }

  if (!user) {
    return (
      <div className="min-h-screen bg-background">
        <AppHeader />
        <div className="flex flex-col items-center justify-center gap-4 py-32">
          <Key className="h-12 w-12 text-muted-foreground" />
          <h2 className="text-xl font-semibold">Sign in to manage API tokens</h2>
          <p className="text-sm text-muted-foreground">
            Create personal tokens to authenticate with the MCP server.
          </p>
          <Button onClick={login}>
            <Key className="mr-2 h-4 w-4" />
            Get MCP Token
          </Button>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-background">
      <AppHeader />
      <main className="container mx-auto max-w-3xl px-4 py-8">
        <div className="mb-6 flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
          <div>
            <h1 className="text-2xl font-bold">API Tokens</h1>
            <p className="text-sm text-muted-foreground">
              Use these tokens to authenticate MCP clients like Cursor or Claude Code.
            </p>
          </div>

          <Dialog open={dialogOpen} onOpenChange={handleDialogClose}>
            <DialogTrigger asChild>
              <Button size="sm" className="w-full sm:w-auto">
                <Plus className="mr-2 h-4 w-4" />
                Create Token
              </Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-xl">
              <DialogHeader>
                <DialogTitle>{rawToken ? 'Token Created' : 'Create API Token'}</DialogTitle>
                <DialogDescription>
                  {rawToken
                    ? 'Copy this token now. It will not be shown again.'
                    : 'Give your token a descriptive label so you can identify it later.'}
                </DialogDescription>
              </DialogHeader>

              {rawToken ? (
                <div className="space-y-4">
                  <div className="grid grid-cols-[1fr_auto] items-center gap-2">
                    <code className="block min-w-0 overflow-x-auto whitespace-nowrap rounded-md border bg-muted px-3 py-2 text-sm">
                      {rawToken}
                    </code>
                    <Button variant="outline" size="icon" onClick={handleCopy}>
                      {copied ? <Check className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
                    </Button>
                  </div>
                  <DialogFooter>
                    <Button onClick={() => handleDialogClose(false)}>Done</Button>
                  </DialogFooter>
                </div>
              ) : (
                <div className="space-y-4">
                  <div className="space-y-2">
                    <Label htmlFor="label">Label</Label>
                    <Input
                      id="label"
                      placeholder='e.g. "Cursor on MacBook"'
                      value={newLabel}
                      onChange={(e) => setNewLabel(e.target.value)}
                      onKeyDown={(e) => e.key === 'Enter' && handleCreate()}
                    />
                  </div>
                  <DialogFooter>
                    <Button onClick={handleCreate} disabled={creating || !newLabel.trim()}>
                      {creating && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
                      Create
                    </Button>
                  </DialogFooter>
                </div>
              )}
            </DialogContent>
          </Dialog>
        </div>

        {tokens.length === 0 ? (
          <div className="rounded-lg border border-dashed p-8 text-center">
            <Key className="mx-auto mb-3 h-8 w-8 text-muted-foreground" />
            <p className="text-muted-foreground">No tokens yet. Create one to get started.</p>
          </div>
        ) : (
          <div className="rounded-lg border">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Label</TableHead>
                  <TableHead>Created</TableHead>
                  <TableHead>Last Used</TableHead>
                  <TableHead className="w-16" />
                </TableRow>
              </TableHeader>
              <TableBody>
                {tokens.map((t) => (
                  <TableRow key={t.id}>
                    <TableCell className="font-medium">{t.label}</TableCell>
                    <TableCell className="text-muted-foreground">
                      {formatDate(t.created_at)}
                    </TableCell>
                    <TableCell className="text-muted-foreground">
                      {t.last_used_at ? formatDate(t.last_used_at) : 'Never'}
                    </TableCell>
                    <TableCell>
                      <Button
                        variant="ghost"
                        size="icon"
                        className="text-destructive hover:text-destructive"
                        onClick={() => handleRevoke(t.id)}
                      >
                        <Trash2 className="h-4 w-4" />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        <section className="mt-8 rounded-lg border p-4 sm:p-6">
          <h2 className="text-lg font-semibold">Connect an MCP client</h2>
          <p className="mt-1 text-sm text-muted-foreground">
            Add this JSON schema to your <code>.cursor/mcp.json</code>. It defines one MCP server
            with URL + Bearer auth header.
          </p>

          <div className="mt-4 rounded-md border bg-muted/40 p-3">
            <pre className="overflow-x-auto text-xs sm:text-sm">
              <code>{mcpConfigJson}</code>
            </pre>
          </div>

          <div className="mt-4 flex flex-wrap items-center gap-2">
            <Button variant="outline" onClick={handleCopyConfig}>
              {configCopied ? <Check className="mr-2 h-4 w-4" /> : <Copy className="mr-2 h-4 w-4" />}
              {configCopied ? 'Copied JSON' : 'Copy MCP JSON'}
            </Button>
            <p className="text-xs text-muted-foreground">
              If your deployment exposes MCP directly on port <code>8080</code>, replace{' '}
              <code>url</code> with <code>http://your-domain:8080/</code> instead.
            </p>
          </div>
        </section>
      </main>
    </div>
  )
}
