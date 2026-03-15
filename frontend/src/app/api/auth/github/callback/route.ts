import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const code = request.nextUrl.searchParams.get('code')
  if (!code) {
    return NextResponse.redirect(new URL('/?error=missing_code', request.url))
  }

  const backendUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

  try {
    const res = await fetch(`${backendUrl}/api/auth/github`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code }),
    })

    if (!res.ok) {
      const data = await res.json().catch(() => ({}))
      const msg = data.detail || 'OAuth failed'
      return NextResponse.redirect(new URL(`/?error=${encodeURIComponent(msg)}`, request.url))
    }

    const setCookie = res.headers.get('set-cookie')
    const redirect = NextResponse.redirect(new URL('/tokens', request.url))
    if (setCookie) {
      redirect.headers.set('set-cookie', setCookie)
    }
    return redirect
  } catch {
    return NextResponse.redirect(new URL('/?error=oauth_error', request.url))
  }
}
