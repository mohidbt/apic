/**
 * Verify marketplace load behavior:
 * 1. Initial load - data immediately (no skeleton)?
 * 2. Filters/pagination - skeleton appears briefly?
 * Uses fresh context (no cache) to simulate hard refresh.
 */
import { chromium } from '@playwright/test'
import path from 'path'

async function main() {
  const browser = await chromium.launch()
  const context = await browser.newContext()
  const page = await context.newPage()

  const captures: { name: string; path: string }[] = []
  const baseDir = process.cwd()

  async function capture(name: string) {
    const p = path.join(baseDir, `verify-${name}.png`)
    await page.screenshot({ path: p, fullPage: true })
    captures.push({ name, path: p })
    console.log(`Captured: ${name}`)
  }

  console.log('=== Part 1: Initial load (fresh context = no cache) ===')
  await page.goto('http://localhost:3000/marketplace', {
    waitUntil: 'domcontentloaded',
  })
  await capture('1-initial-domcontentloaded')

  await page.waitForTimeout(500)
  await capture('2-initial-after-500ms')

  await page.waitForTimeout(1500)
  await capture('3-initial-after-2s')

  console.log('=== Part 2: Change filter (tag) ===')
  await page.click('[role="combobox"]')
  await page.waitForTimeout(200)
  const options = await page.locator('[role="option"]').all()
  if (options.length > 1) {
    await options[1].click()
    await capture('4-filter-click-instant')
    await page.waitForTimeout(300)
    await capture('5-filter-after-300ms')
    await page.waitForTimeout(1500)
    await capture('6-filter-after-2s')
  }

  console.log('=== Part 3: Pagination (if available) ===')
  const nextBtn = page.locator('button:has-text("Next")')
  if ((await nextBtn.count()) > 0 && !(await nextBtn.isDisabled())) {
    await nextBtn.click()
    await capture('7-pagination-click-instant')
    await page.waitForTimeout(300)
    await capture('8-pagination-after-300ms')
  } else {
    const prevBtn = page.locator('button:has-text("Previous")')
    if ((await prevBtn.count()) > 0 && !(await prevBtn.isDisabled())) {
      await prevBtn.click()
      await capture('7-pagination-prev-instant')
      await page.waitForTimeout(300)
      await capture('8-pagination-after-300ms')
    } else {
      await capture('7-pagination-not-available')
    }
  }

  await browser.close()

  console.log('\n=== Screenshots ===')
  captures.forEach((c) => console.log(`  ${c.path}`))
}

main().catch(console.error)
