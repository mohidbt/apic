/**
 * Navigate to marketplace to trigger post-fix agent logs, wait 2s for logs to be written.
 */
import { chromium } from '@playwright/test'

async function main() {
  const browser = await chromium.launch()
  const page = await browser.newPage()

  await page.goto('http://localhost:3000/marketplace', {
    waitUntil: 'networkidle',
  })

  await page.waitForTimeout(2000)

  await browser.close()
  console.log('Done - post-fix logs should have been written')
}

main().catch(console.error)
