import { NextResponse } from 'next/server'

export async function GET() {
  const clientId = process.env.NEXT_PUBLIC_GITHUB_CLIENT_ID || process.env.GITHUB_CLIENT_ID
  if (!clientId) {
    return NextResponse.json({ error: 'GitHub OAuth not configured' }, { status: 500 })
  }

  const redirectUri = `${process.env.NEXT_PUBLIC_APP_URL || process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000'}/api/auth/github/callback`
  const params = new URLSearchParams({
    client_id: clientId,
    redirect_uri: redirectUri,
    scope: 'read:user',
  })

  return NextResponse.redirect(`https://github.com/login/oauth/authorize?${params}`)
}
