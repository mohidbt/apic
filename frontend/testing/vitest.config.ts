import { defineConfig } from "vitest/config"
import react from "@vitejs/plugin-react"
import path from "path"

export default defineConfig({
  root: path.resolve(__dirname, ".."),
  plugins: [react()],
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["testing/setup.ts"],
    include: ["testing/tests/**/*.{test,spec}.{ts,tsx}"],
    exclude: ["testing/tests/e2e/**", "testing/playwright-report/**", "testing/test-results/**"],
    coverage: {
      provider: "v8",
      reporter: ["text", "json", "html"],
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "../src"),
    },
  },
})
