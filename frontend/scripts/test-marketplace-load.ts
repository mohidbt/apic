/**
 * Test marketplace: hard refresh, initial load, pagination, and filter changes.
 */
import { chromium } from '@playwright/test'
import path from 'path'

async function main() {
  const browser = await chromium.launch()
  // Fresh context = no cache (simulates hard refresh / new user)
  const context = await browser.newContext()
  const page = await context.newPage()

  const captures: { name: string; path: string }[] = []
  async function capture(name: string) {
    const p = path.join(process.cwd(), `test-${name}.png`)
    await page.screenshot({ path: p, fullPage: true })
    captures.push({ name, path: p })
  }

  console.log('=== 1. Hard refresh / initial load ===')
  await page.goto('http://localhost:3000/marketplace', {
    waitUntil: 'domcontentloaded',
  })
  await capture('1-initial-domcontentloaded')

  await page.waitForLoadState('load')
  await capture('2-after-load-event')

  await page.waitForLoadState('networkidle')
  await capture('3-initial-load-final')

  console.log('\n=== 4. Click page 2 (pagination) ===')
  const nextBtn = page.locator('main').getByRole('button', { name: 'Next', exact: true })
  if (await nextBtn.isEnabled()) {
    await nextBtn.click()
    await capture('4a-page2-clicked-instant')
    await page.waitForTimeout(200)
    await capture('4b-page2-after-200ms')
    await page.waitForTimeout(400)
    await capture('4c-page2-loaded')
  } else {
    console.log('(Only 1 page - pagination disabled)')
    await capture('4-no-pagination')
  }

  console.log('\n=== 5. Change filter ===')
  const prevBtn = page.locator('main').getByRole('button', { name: 'Previous', exact: true })
  if (await prevBtn.isEnabled()) {
    await prevBtn.click()
    await page.waitForTimeout(400)
  }

  const filterTrigger = page.getByRole('combobox').first()
  await filterTrigger.click()
  await page.waitForTimeout(150)
  const options = page.locator('[role="option"]')
  const otherOption = options.filter({ hasNotText: 'All Tags' }).first()
  if (await options.count() > 1) {
    await otherOption.click()
    await capture('5a-filter-changed-instant')
    await page.waitForTimeout(200)
    await capture('5b-filter-after-200ms')
    await page.waitForTimeout(400)
    await capture('5c-filter-loaded')
  } else {
    await page.keyboard.press('Escape')
    await capture('5-no-other-filters')
  }

  await browser.close()

  console.log('\nCaptures:')
  captures.forEach((c) => console.log(`  ${c.path}`))
}

main().catch(console.error)
