'use client'

import { useState } from 'react'
import { CheckCircle2, Download, Share2, Sparkles } from 'lucide-react'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'

interface ContributeDialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  filename: string
  tokenCount: number | null
  provider: string | null
  onDownloadOnly: () => void
  onDownloadAndShare: (providerName?: string) => Promise<void>
  isSharing: boolean
}

function formatTokenCount(tokens: number | null): string {
  if (tokens === null || tokens === undefined) return 'N/A'
  if (tokens >= 1_000_000) return `${(tokens / 1_000_000).toFixed(1)}M`
  if (tokens >= 1000) return `${(tokens / 1000).toFixed(1)}k`
  return tokens.toString()
}

export function ContributeDialog({
  open,
  onOpenChange,
  filename,
  tokenCount,
  provider,
  onDownloadOnly,
  onDownloadAndShare,
  isSharing,
}: ContributeDialogProps) {
  const [manualProvider, setManualProvider] = useState('')
  const needsProvider = !provider
  const resolvedProvider = provider || manualProvider.trim()

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-h-[90dvh] w-[calc(100vw-2rem)] overflow-x-hidden overflow-y-auto sm:max-w-xl">
        <DialogHeader>
          <div className="mb-3 flex items-center gap-2 text-primary">
            <CheckCircle2 className="h-5 w-5" />
            <span className="text-sm font-medium">Conversion complete</span>
          </div>
          <DialogTitle className="text-2xl">Your file is ready!</DialogTitle>
          <DialogDescription>
            Your API document was successfully converted to LLM-ready markdown.
          </DialogDescription>
        </DialogHeader>

        <div className="min-w-0 space-y-4">
          <div className="min-w-0 overflow-hidden rounded-lg border bg-muted/30 p-4">
            <p className="text-sm text-muted-foreground">File</p>
            <p className="block max-w-full truncate text-sm font-medium text-foreground">{filename}</p>
            <p className="mt-2 text-sm text-muted-foreground">
              Estimated tokens: {formatTokenCount(tokenCount)}
            </p>
          </div>

          {needsProvider && (
            <div className="rounded-lg border border-orange-500/40 bg-orange-50/50 p-4 dark:bg-orange-950/20">
              <label htmlFor="provider-name" className="mb-2 block text-sm font-medium text-foreground">
                Provider Name <span className="text-destructive">*</span>
              </label>
              <p className="mb-3 text-xs text-muted-foreground">
                Could not detect a provider from the spec. Please enter the API provider name (e.g. &quot;Stripe&quot;, &quot;Twilio&quot;).
              </p>
              <Input
                id="provider-name"
                placeholder="e.g. Stripe"
                value={manualProvider}
                onChange={(e) => setManualProvider(e.target.value)}
              />
            </div>
          )}

          <div className="rounded-lg border bg-background p-4">
            <p className="mb-2 flex items-center gap-2 text-sm font-medium text-foreground">
              <Sparkles className="h-4 w-4" />
              Help improve the marketplace
            </p>
            <p className="text-sm text-muted-foreground">
              You can optionally contribute this converted file so others can discover and use it.
            </p>
          </div>
        </div>

        <DialogFooter className="min-w-0 flex-col gap-2 sm:flex-row sm:flex-wrap sm:justify-end">
          <Button variant="outline" onClick={onDownloadOnly} disabled={isSharing} className="min-w-0 w-full sm:w-auto">
            <Download className="mr-2 h-4 w-4" />
            Just Download
          </Button>
          <Button
            onClick={() => onDownloadAndShare(needsProvider ? resolvedProvider : undefined)}
            disabled={isSharing || (needsProvider && !resolvedProvider)}
            className="h-auto min-w-0 w-full whitespace-normal break-words py-2 text-left sm:basis-full sm:py-2 sm:text-left md:basis-auto md:w-auto md:text-center"
          >
            <Share2 className="mr-2 h-4 w-4" />
            {isSharing ? 'Sharing...' : 'Download & Share to Marketplace'}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
