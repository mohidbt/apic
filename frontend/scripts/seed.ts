#!/usr/bin/env tsx

/**
 * Database Seeding Script
 *
 * This script seeds the database with initial data for development and testing.
 * Run with: npm run db:seed
 */

import * as dotenv from 'dotenv'
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

// Load environment variables
dotenv.config()

const DATABASE_URL = process.env.DATABASE_URL

if (!DATABASE_URL) {
  console.error('❌ DATABASE_URL is not defined in environment variables')
  process.exit(1)
}

// Create database connection
const client = postgres(DATABASE_URL)
const db = drizzle(client)

async function seed() {
  try {
    console.log('🌱 Starting database seeding...')

    // Add your seeding logic here
    // Example:
    // await db.insert(users).values([
    //   {
    //     id: '1',
    //     email: 'admin@example.com',
    //     name: 'Admin User',
    //     createdAt: new Date(),
    //   },
    // ]);

    console.log('✅ Database seeding completed successfully!')
  } catch (error) {
    console.error('❌ Error seeding database:', error)
    process.exit(1)
  } finally {
    await client.end()
  }
}

// Run the seeding function
seed().catch((error) => {
  console.error('❌ Seeding failed:', error)
  process.exit(1)
})
