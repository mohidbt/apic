import { test, expect } from "@playwright/test"

test.describe("Authentication Flow", () => {
  test("home page exposes auth entrypoint", async ({ page }) => {
    await page.goto("/")
    await expect(page.getByRole("button", { name: "Get MCP Token" }).first()).toBeVisible()
  })

  test("tokens route prompts unauthenticated users to sign in", async ({ page }) => {
    await page.goto("/tokens")
    await expect(page.getByRole("heading", { name: "Sign in to manage API tokens" })).toBeVisible()
    await expect(page.getByRole("button", { name: "Get MCP Token" }).nth(1)).toBeVisible()
  })
})
