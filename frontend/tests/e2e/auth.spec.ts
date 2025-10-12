import { test, expect } from "@playwright/test"

test.describe("Authentication Flow", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/")
  })

  test("should allow user to sign up", async ({ page }) => {
    // Navigate to sign up page
    await page.click("text=Sign in")
    await page.click("text=Sign up")

    // Fill out sign up form
    await page.fill('[name="firstName"]', "John")
    await page.fill('[name="lastName"]', "Doe")
    await page.fill('[name="email"]', "john.doe@example.com")
    await page.fill('[name="password"]', "SecurePass123!")
    await page.fill('[name="confirmPassword"]', "SecurePass123!")
    await page.check('[name="terms"]')

    // Submit form
    await page.click('button[type="submit"]')

    // Should redirect to verification page
    await expect(page).toHaveURL(/verify-email/)
    await expect(page.locator("text=Check your email")).toBeVisible()
  })

  test("should allow user to sign in", async ({ page }) => {
    // Navigate to sign in page
    await page.click("text=Sign in")

    // Fill out sign in form
    await page.fill('[name="email"]', "existing@example.com")
    await page.fill('[name="password"]', "SecurePass123!")

    // Submit form
    await page.click('button[type="submit"]')

    // Should redirect to dashboard
    await expect(page).toHaveURL(/dashboard/)
    await expect(page.locator("text=Welcome back")).toBeVisible()
  })

  test("should show validation errors for invalid input", async ({ page }) => {
    // Navigate to sign up page
    await page.click("text=Sign in")
    await page.click("text=Sign up")

    // Submit form without filling required fields
    await page.click('button[type="submit"]')

    // Should show validation errors
    await expect(page.locator("text=First name is required")).toBeVisible()
    await expect(page.locator("text=Last name is required")).toBeVisible()
    await expect(page.locator("text=Email is required")).toBeVisible()
    await expect(page.locator("text=Password is required")).toBeVisible()
  })

  test("should handle password reset flow", async ({ page }) => {
    // Navigate to sign in page
    await page.click("text=Sign in")
    await page.click("text=Forgot Password")

    // Fill out forgot password form
    await page.fill('[name="email"]', "reset@example.com")
    await page.click('button[type="submit"]')

    // Should show success message
    await expect(page.locator("text=Check your email")).toBeVisible()
  })

  test("should allow user to sign out", async ({ page }) => {
    // Sign in first
    await page.goto("/sign-in")
    await page.fill('[name="email"]', "existing@example.com")
    await page.fill('[name="password"]', "SecurePass123!")
    await page.click('button[type="submit"]')

    // Wait for dashboard to load
    await expect(page).toHaveURL(/dashboard/)

    // Sign out
    await page.click('[data-testid="user-menu"]')
    await page.click("text=Sign out")

    // Should redirect to home page
    await expect(page).toHaveURL("/")
    await expect(page.locator("text=Sign in")).toBeVisible()
  })
})
