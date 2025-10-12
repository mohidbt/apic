import type React from "react"
// Authentication related types

export interface AuthUser {
  id: string
  email: string
  firstName?: string
  lastName?: string
  username?: string
  imageUrl?: string
  emailVerified: boolean
  createdAt: Date
  updatedAt: Date
}

export interface SignInCredentials {
  email: string
  password: string
  rememberMe?: boolean
}

export interface SignUpCredentials {
  email: string
  password: string
  firstName?: string
  lastName?: string
  username?: string
}

export interface AuthSession {
  user: AuthUser
  accessToken: string
  refreshToken?: string
  expiresAt: Date
}

export interface AuthState {
  user: AuthUser | null
  isLoading: boolean
  isAuthenticated: boolean
  error: string | null
}

export interface PasswordResetRequest {
  email: string
}

export interface PasswordResetConfirm {
  token: string
  password: string
  confirmPassword: string
}

export interface EmailVerificationRequest {
  email: string
}

export interface EmailVerificationConfirm {
  token: string
}

export interface UpdateProfileRequest {
  firstName?: string
  lastName?: string
  username?: string
  bio?: string
  website?: string
  location?: string
}

export interface ChangePasswordRequest {
  currentPassword: string
  newPassword: string
  confirmPassword: string
}

export interface SocialAuthProvider {
  id: string
  name: string
  icon: React.ComponentType<{ className?: string }>
  color: string
}
