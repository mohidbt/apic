'use client'

import { useEffect, useState } from 'react'
import { useAuth } from '@/lib/auth-context'
import { Link } from '@/i18n/navigation'
import { ThemeToggle } from '@/components/theme-toggle'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { Button } from '@/components/ui/button'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { Github, Key, LogOut, Package, Star } from 'lucide-react'

interface AppHeaderProps {
  starCount?: number
}

export function AppHeader({ starCount }: AppHeaderProps) {
  const { user, isLoading, login, logout } = useAuth()
  const [resolvedStarCount, setResolvedStarCount] = useState<number | null>(
    typeof starCount === 'number' ? starCount : null
  )

  useEffect(() => {
    if (typeof starCount === 'number') {
      setResolvedStarCount(starCount)
      return
    }

    let isCancelled = false
    const apiBase = process.env.NEXT_PUBLIC_API_URL || ''

    fetch(`${apiBase}/api/github/stats`)
      .then(async (res) => {
        if (!res.ok) return
        const data = await res.json()
        const nextCount =
          typeof data?.stargazers_count === 'number' ? data.stargazers_count : null
        if (!isCancelled) {
          setResolvedStarCount(nextCount)
        }
      })
      .catch(() => {})

    return () => {
      isCancelled = true
    }
  }, [starCount])

  return (
    <header className="border-b border-border bg-card">
      <div className="container mx-auto flex h-16 items-center justify-between gap-3 px-4">
        <div className="min-w-0 shrink-0">
          <Link href="/" className="text-xl font-bold sm:text-2xl">
            <span className="text-foreground">API Ingest</span>
          </Link>
        </div>
        <div className="flex min-w-0 items-center gap-1 sm:gap-2 md:gap-3">
          <Link
            href="/marketplace"
            aria-label="Specs Marketplace"
            className="flex items-center gap-2 whitespace-nowrap rounded-lg px-2 py-2 transition-colors hover:bg-muted sm:px-3"
          >
            <Package className="h-5 w-5 shrink-0 text-muted-foreground" />
            <span className="hidden text-sm text-muted-foreground lg:inline">Specs Marketplace</span>
          </Link>
          <a
            href="https://github.com/mohidbt/api-ingest"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="GitHub"
            className="flex items-center gap-2 whitespace-nowrap rounded-lg px-2 py-2 transition-colors hover:bg-muted sm:px-3"
          >
            <Github className="h-5 w-5 shrink-0 text-muted-foreground" />
            <span className="hidden text-sm text-muted-foreground lg:inline">GitHub</span>
            {resolvedStarCount !== null && (
              <div className="flex items-center">
                <Star className="h-4 w-4 fill-primary text-primary" />
                <span className="ml-1 hidden text-sm text-muted-foreground md:inline">{resolvedStarCount}</span>
              </div>
            )}
          </a>
          {user ? (
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" className="relative h-8 w-8 rounded-full">
                  <Avatar className="h-8 w-8">
                    <AvatarImage src={user.avatar_url ?? undefined} alt={user.github_login} />
                    <AvatarFallback>{user.github_login.slice(0, 2).toUpperCase()}</AvatarFallback>
                  </Avatar>
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end" className="w-48">
                <div className="px-2 py-1.5 text-sm font-medium">{user.github_login}</div>
                <DropdownMenuSeparator />
                <DropdownMenuItem asChild>
                  <Link href="/tokens" className="flex items-center">
                    <Key className="mr-2 h-4 w-4" />
                    API Tokens
                  </Link>
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={logout}>
                  <LogOut className="mr-2 h-4 w-4" />
                  Sign out
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          ) : (
            <button
              onClick={login}
              disabled={isLoading}
              aria-label="Get MCP Token"
              className="flex items-center gap-2 whitespace-nowrap rounded-lg px-2 py-2 transition-colors hover:bg-muted disabled:cursor-not-allowed disabled:opacity-60 sm:px-3"
            >
              <Key className="h-5 w-5 shrink-0 text-muted-foreground" />
              <span className="hidden text-sm text-muted-foreground lg:inline">Get MCP Token</span>
            </button>
          )}
          <ThemeToggle />
        </div>
      </div>
    </header>
  )
}
