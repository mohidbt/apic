/**
 * Captures marketplace IMMEDIATELY on load - no delay, no API throttling.
 * Best chance to catch the raw initial render before any async updates.
 */
import { chromium } from '@playwright/test'
import path from 'path'

async function main() {
  const browser = await chromium.launch()
  const page = await browser.newPage()

  // Navigate and screenshot as soon as DOM is ready - no delays
  await page.goto('http://localhost:3000/marketplace', {
    waitUntil: 'domcontentloaded',
  })

  const screenshotPath = path.join(
    process.cwd(),
    'marketplace-instant-load.png'
  )
  await page.screenshot({ path: screenshotPath, fullPage: true })
  console.log(`Screenshot saved to: ${screenshotPath}`)

  await browser.close()
}

main().catch(console.error)
