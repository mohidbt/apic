import { expect, test } from "@playwright/test"

async function expectNoHorizontalOverflow(page: import("@playwright/test").Page) {
  const dimensions = await page.evaluate(() => {
    const doc = document.documentElement
    return {
      viewportWidth: window.innerWidth,
      scrollWidth: doc.scrollWidth,
    }
  })

  expect(
    dimensions.scrollWidth,
    `Expected no horizontal overflow; scrollWidth=${dimensions.scrollWidth}, viewportWidth=${dimensions.viewportWidth}`
  ).toBeLessThanOrEqual(dimensions.viewportWidth)
}

test.describe("Mobile core flow UX", () => {
  test.beforeEach(async ({ page }) => {
    await page.addStyleTag({
      content: `
        *, *::before, *::after {
          animation: none !important;
          transition: none !important;
          caret-color: transparent !important;
        }
      `,
    })
  })

  test("home page stays within mobile viewport", async ({ page }) => {
    await page.goto("/")
    await expect(page.getByRole("heading", { level: 1, name: /API Docs/i })).toBeVisible()
    await expect(page.getByRole("button", { name: "Convert" })).toBeVisible()
    await expect(page.getByRole("button", { name: "Get MCP Token" }).first()).toBeVisible()
    await expectNoHorizontalOverflow(page)
  })

  test("home visual layout remains stable on mobile", async ({ page }) => {
    await page.goto("/")
    await expect(page.getByRole("heading", { level: 1, name: /API Docs/i })).toBeVisible()
    await expect(page).toHaveScreenshot("mobile-home.png", {
      maxDiffPixelRatio: 0.02,
      mask: [page.locator('a[href="https://github.com/mohidbt/apic"]')],
    })
  })

  test("marketplace is usable on mobile and avoids page overflow", async ({ page }) => {
    await page.goto("/marketplace")
    await expect(page.getByRole("heading", { name: "Specs Marketplace" })).toBeVisible()
    await expect(page.getByPlaceholder("Search APIs...")).toBeVisible()
    await expectNoHorizontalOverflow(page)

    const rows = page.locator('tr[role="button"]')
    const rowCount = await rows.count()
    if (rowCount > 0) {
      await rows.first().click()
      await expect(page.getByRole("tab", { name: "Overview" })).toBeVisible()
      await expect(page.getByRole("tab", { name: "Chunks" })).toBeVisible()
      await expect(page.getByRole("tab", { name: "Tool Schemas" })).toBeVisible()
      await expect(page.getByRole("tab", { name: "Full Markdown" })).toBeVisible()
      await expectNoHorizontalOverflow(page)
    } else {
      await expect(page.getByText("No specs found")).toBeVisible()
    }
  })

  test("marketplace visual layout remains stable on mobile", async ({ page }) => {
    await page.goto("/marketplace")
    await expect(page.getByRole("heading", { name: "Specs Marketplace" })).toBeVisible()
    await expect(page).toHaveScreenshot("mobile-marketplace.png", {
      maxDiffPixelRatio: 0.02,
      mask: [
        page.locator("tbody"),
        page.locator('a[href="https://github.com/mohidbt/apic"]'),
      ],
    })
  })

  test("tokens auth entry point works on mobile", async ({ page }) => {
    await page.goto("/tokens")
    await expect(page.getByRole("heading", { name: "Sign in to manage API tokens" })).toBeVisible()
    await expect(page.getByRole("button", { name: "Get MCP Token" }).nth(1)).toBeVisible()
    await expectNoHorizontalOverflow(page)
  })

  test("tokens auth entry visual layout remains stable on mobile", async ({ page }) => {
    await page.goto("/tokens")
    await expect(page.getByRole("heading", { name: "Sign in to manage API tokens" })).toBeVisible()
    await expect(page).toHaveScreenshot("mobile-tokens-auth.png", {
      maxDiffPixelRatio: 0.02,
      mask: [page.locator('a[href="https://github.com/mohidbt/apic"]')],
    })
  })
})
