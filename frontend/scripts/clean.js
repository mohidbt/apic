#!/usr/bin/env node

/**
 * Clean Script
 *
 * This script cleans build artifacts and temporary files
 * Run with: node scripts/clean.js
 */

const fs = require('fs')
const path = require('path')

const foldersToClean = [
  '.next',
  'dist',
  'build',
  'coverage',
  'storybook-static',
  'playwright-report',
  'test-results',
]

const filesToClean = ['.tsbuildinfo']

console.log('🧹 Cleaning build artifacts...\n')

// Clean folders
foldersToClean.forEach((folder) => {
  if (fs.existsSync(folder)) {
    console.log(`🗑️  Removing ${folder}/`)
    try {
      fs.rmSync(folder, { recursive: true, force: true })
      console.log(`✅ Removed ${folder}/`)
    } catch (error) {
      console.log(`❌ Failed to remove ${folder}/: ${error.message}`)
    }
  }
})

// Clean files
filesToClean.forEach((file) => {
  if (fs.existsSync(file)) {
    console.log(`🗑️  Removing ${file}`)
    try {
      fs.unlinkSync(file)
      console.log(`✅ Removed ${file}`)
    } catch (error) {
      console.log(`❌ Failed to remove ${file}: ${error.message}`)
    }
  }
})

console.log('\n✨ Cleanup complete!')
console.log('You can now run a fresh build with: npm run build')
