import { z } from "zod"

// Common validation schemas
export const emailSchema = z.string().min(1, "Email is required").email("Please enter a valid email address")

export const passwordSchema = z
  .string()
  .min(8, "Password must be at least 8 characters")
  .regex(
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/,
    "Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character",
  )

export const phoneSchema = z
  .string()
  .regex(/^\+?[1-9]\d{1,14}$/, "Please enter a valid phone number")
  .optional()

export const urlSchema = z.string().url("Please enter a valid URL").optional().or(z.literal(""))

export const slugSchema = z
  .string()
  .min(1, "Slug is required")
  .max(100, "Slug must be less than 100 characters")
  .regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/, "Slug can only contain lowercase letters, numbers, and hyphens")

// Pagination schema
export const paginationSchema = z.object({
  page: z.coerce.number().min(1).default(1),
  limit: z.coerce.number().min(1).max(100).default(10),
  sortBy: z.string().optional(),
  sortOrder: z.enum(["asc", "desc"]).default("desc"),
})

// Search schema
export const searchSchema = z.object({
  q: z.string().min(1, "Search query is required").max(100),
  category: z.string().optional(),
  tags: z.array(z.string()).optional(),
})

// Contact form schema
export const contactSchema = z.object({
  name: z.string().min(1, "Name is required").max(100, "Name must be less than 100 characters"),
  email: emailSchema,
  subject: z.string().min(1, "Subject is required").max(200, "Subject must be less than 200 characters"),
  message: z
    .string()
    .min(10, "Message must be at least 10 characters")
    .max(1000, "Message must be less than 1000 characters"),
})

// Newsletter subscription schema
export const newsletterSchema = z.object({
  email: emailSchema,
  preferences: z.array(z.string()).optional(),
})

// File upload schema
export const fileUploadSchema = z.object({
  file: z
    .instanceof(File)
    .refine((file) => file.size <= 5 * 1024 * 1024, "File size must be less than 5MB")
    .refine(
      (file) => ["image/jpeg", "image/png", "image/webp", "image/gif"].includes(file.type),
      "File must be an image (JPEG, PNG, WebP, or GIF)",
    ),
})

// Export types
export type PaginationInput = z.infer<typeof paginationSchema>
export type SearchInput = z.infer<typeof searchSchema>
export type ContactInput = z.infer<typeof contactSchema>
export type NewsletterInput = z.infer<typeof newsletterSchema>
export type FileUploadInput = z.infer<typeof fileUploadSchema>
