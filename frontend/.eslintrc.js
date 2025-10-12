/** @type {import('eslint').Linter.Config} */
module.exports = {
  extends: [
    'next/core-web-vitals',
    'prettier',
    '@typescript-eslint/recommended',
    'eslint:recommended',
  ],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint', 'import/recommended', 'storybook/recommended'],
  rules: {
    '@typescript-eslint/no-unused-vars': 'error',
    '@typescript-eslint/no-explicit-any': 'warn',
    'prefer-const': 'error',
    'no-var': 'error',
  },
  overrides: [
    {
      files: ['**/*.stories.*'],
      extends: ['plugin:storybook/recommended'],
    },
  ],
}
