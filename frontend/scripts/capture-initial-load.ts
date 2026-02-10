/**
 * Captures a screenshot of the marketplace page to check for empty table flash
 * before data loads. Uses slow 3G to prolong the empty state for capture.
 */
import { chromium } from '@playwright/test'
import path from 'path'

async function main() {
  const browser = await chromium.launch()
  const context = await browser.newContext({
    // Slow 3G to prolong empty table state before API responds
    recordVideo: undefined,
  })
  const page = await context.newPage()

  // Throttle API calls to prolong the empty-table state
  await page.route(/\/api\/(specs|tags)/, async (route) => {
    await new Promise((r) => setTimeout(r, 2000)) // 2s delay on API
    await route.continue()
  })

  // Navigate and capture as soon as DOM is ready
  await page.goto('http://localhost:3000/marketplace', {
    waitUntil: 'domcontentloaded',
  })

  // Wait for React to hydrate and render (empty table shows before skeleton)
  await page.waitForTimeout(150) // ~150ms is before 200ms skeleton delay

  const screenshotPath = path.join(
    process.cwd(),
    'marketplace-initial-load.png'
  )
  await page.screenshot({ path: screenshotPath, fullPage: true })
  console.log(`Screenshot saved to: ${screenshotPath}`)

  await browser.close()
}

main().catch(console.error)
