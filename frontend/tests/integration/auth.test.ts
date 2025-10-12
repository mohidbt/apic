import { describe, it, expect, beforeEach, afterEach } from "vitest"
import { testDb } from "../setup/database"
import { signUp, signIn, verifyEmail } from "@/libs/auth"

describe("Authentication Integration Tests", () => {
  beforeEach(async () => {
    await testDb.clean()
  })

  afterEach(async () => {
    await testDb.clean()
  })

  describe("User Registration", () => {
    it("should create a new user account", async () => {
      const userData = {
        email: "test@example.com",
        password: "SecurePass123!",
        firstName: "John",
        lastName: "Doe",
      }

      const result = await signUp(userData)

      expect(result.success).toBe(true)
      expect(result.user).toBeDefined()
      expect(result.user.email).toBe(userData.email)
      expect(result.user.firstName).toBe(userData.firstName)
      expect(result.user.lastName).toBe(userData.lastName)
      expect(result.user.emailVerified).toBe(false)
    })

    it("should not allow duplicate email addresses", async () => {
      const userData = {
        email: "duplicate@example.com",
        password: "SecurePass123!",
        firstName: "John",
        lastName: "Doe",
      }

      await signUp(userData)
      const result = await signUp(userData)

      expect(result.success).toBe(false)
      expect(result.error).toContain("email already exists")
    })

    it("should validate password requirements", async () => {
      const userData = {
        email: "test@example.com",
        password: "weak",
        firstName: "John",
        lastName: "Doe",
      }

      const result = await signUp(userData)

      expect(result.success).toBe(false)
      expect(result.error).toContain("password")
    })
  })

  describe("User Authentication", () => {
    beforeEach(async () => {
      await signUp({
        email: "auth@example.com",
        password: "SecurePass123!",
        firstName: "Auth",
        lastName: "User",
      })
    })

    it("should authenticate user with correct credentials", async () => {
      const result = await signIn({
        email: "auth@example.com",
        password: "SecurePass123!",
      })

      expect(result.success).toBe(true)
      expect(result.user).toBeDefined()
      expect(result.session).toBeDefined()
      expect(result.session.accessToken).toBeDefined()
    })

    it("should reject invalid credentials", async () => {
      const result = await signIn({
        email: "auth@example.com",
        password: "WrongPassword",
      })

      expect(result.success).toBe(false)
      expect(result.error).toContain("invalid credentials")
    })

    it("should reject non-existent user", async () => {
      const result = await signIn({
        email: "nonexistent@example.com",
        password: "SecurePass123!",
      })

      expect(result.success).toBe(false)
      expect(result.error).toContain("user not found")
    })
  })

  describe("Email Verification", () => {
    it("should verify email with valid token", async () => {
      const signUpResult = await signUp({
        email: "verify@example.com",
        password: "SecurePass123!",
        firstName: "Verify",
        lastName: "User",
      })

      const verificationToken = signUpResult.verificationToken
      const result = await verifyEmail(verificationToken)

      expect(result.success).toBe(true)
      expect(result.user.emailVerified).toBe(true)
    })

    it("should reject invalid verification token", async () => {
      const result = await verifyEmail("invalid-token")

      expect(result.success).toBe(false)
      expect(result.error).toContain("invalid token")
    })
  })
})
