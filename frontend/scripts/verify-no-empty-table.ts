/**
 * Navigate to marketplace, refresh 2-3 times, and capture screenshots
 * to verify table never shows empty state (headers only).
 */
import { chromium } from '@playwright/test'
import path from 'path'

async function main() {
  const browser = await chromium.launch()
  const page = await browser.newPage()

  const captures: { name: string; path: string }[] = []

  async function capture(name: string) {
    const p = path.join(process.cwd(), `verify-${name}.png`)
    await page.screenshot({ path: p, fullPage: true })
    captures.push({ name, path: p })
  }

  // Throttle API to prolong loading state and increase chance of catching transitions
  await page.route(/\/api\/(specs|tags)/, async (route) => {
    await new Promise((r) => setTimeout(r, 800))
    await route.continue()
  })

  for (let i = 0; i < 3; i++) {
    const url = i === 0 ? 'http://localhost:3000/marketplace' : undefined
    if (url) {
      await page.goto(url, { waitUntil: 'domcontentloaded' })
    } else {
      await page.reload({ waitUntil: 'domcontentloaded' })
    }
    // Capture immediately - before API responds
    await capture(`refresh-${i + 1}-instant`)
    // Brief wait then capture again (might catch skeleton or loaded state)
    await page.waitForTimeout(300)
    await capture(`refresh-${i + 1}-after-300ms`)
  }

  // Wait for final load and capture loaded state
  await page.waitForTimeout(1500)
  await capture('final-loaded')

  await browser.close()

  console.log('Captures:')
  captures.forEach((c) => console.log(`  - ${c.name}: ${c.path}`))
  console.log('\nCheck screenshots - table should show skeleton or data, never empty headers only.')
}

main().catch(console.error)
