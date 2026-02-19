'use client'

import { CheckCircle2, Download, Share2, Sparkles } from 'lucide-react'

import { Button } from '@/components/ui/button'
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
  onDownloadOnly: () => void
  onDownloadAndShare: () => Promise<void>
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
  onDownloadOnly,
  onDownloadAndShare,
  isSharing,
}: ContributeDialogProps) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-h-[90dvh] w-[calc(100vw-2rem)] overflow-x-hidden overflow-y-auto sm:max-w-xl">
        <DialogHeader>
          <div className="mb-3 flex items-center gap-2 text-green-600">
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
            onClick={onDownloadAndShare}
            disabled={isSharing}
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
