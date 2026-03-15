'use client'

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

export function AppHeader({ starCount = 0 }: AppHeaderProps) {
  const { user, isLoading, login, logout } = useAuth()

  return (
    <header className="border-b border-border bg-card">
      <div className="container mx-auto flex h-16 items-center justify-between px-4">
        <div className="flex items-center space-x-2">
          <Link href="/" className="text-2xl font-bold">
            <span className="text-foreground">API Ingest</span>
          </Link>
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
          {!isLoading && (
            <>
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
                  className="flex items-center space-x-2 rounded-lg px-3 py-2 transition-colors hover:bg-muted"
                >
                  <Github className="h-5 w-5 text-muted-foreground" />
                  <span className="text-sm text-muted-foreground">Sign in</span>
                </button>
              )}
            </>
          )}
          <ThemeToggle />
        </div>
      </div>
    </header>
  )
}
