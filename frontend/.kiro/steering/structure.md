# Project Structure & Organization

## Root Directory Structure
```
├── .kiro/              # Kiro AI assistant configuration
├── .storybook/         # Storybook configuration
├── config/             # Application configuration files
├── public/             # Static assets (images, icons, etc.)
├── src/                # Source code (main application)
├── tests/              # Test files (E2E and integration)
└── scripts/            # Build and deployment scripts
```

## Source Directory (`src/`)
The main application code follows a feature-based organization:

```
src/
├── app/                # Next.js App Router pages and layouts
│   ├── [locale]/       # Internationalized routes
│   └── api/            # API routes
├── components/         # Reusable React components
│   └── ui/             # shadcn/ui components
├── db/                 # Database configuration and schema
│   └── schema/         # Drizzle ORM schema definitions
├── hooks/              # Custom React hooks
├── i18n/               # Internationalization configuration
│   └── locales/        # Translation files
├── lib/                # Utility libraries and configurations
├── models/             # Data models and types
├── stories/            # Storybook stories
├── styles/             # Global CSS and styling
├── templates/          # Email and other templates
│   └── email/          # Email templates
├── test/               # Test utilities and setup
├── types/              # TypeScript type definitions
├── utils/              # Helper functions and constants
├── validations/        # Zod validation schemas
├── env.ts              # Environment variable validation
└── middleware.ts       # Next.js middleware
```

## Key Conventions

### File Naming
- Use kebab-case for files and directories
- React components use PascalCase for the component name
- Use `.tsx` for React components, `.ts` for utilities
- Test files use `.test.ts` or `.test.tsx` suffix
- Story files use `.stories.ts` suffix

### Import Aliases
- `@/*` maps to `src/*` for internal imports
- `#/*` maps to project root for config files
- Use absolute imports with aliases instead of relative paths

### Component Organization
- UI components go in `src/components/ui/` (shadcn/ui)
- Feature-specific components in `src/components/`
- Each component should have its own file
- Export components as default exports

### Database Schema
- Schema files in `src/db/schema/`
- Use Drizzle ORM conventions
- Migrations generated in `./drizzle/` directory

### API Routes
- API routes in `src/app/api/`
- Follow RESTful conventions
- Use route handlers for different HTTP methods

### Styling
- Global styles in `src/styles/globals.css`
- Use Tailwind CSS classes
- CSS variables for theming in HSL format
- Component-specific styles using Tailwind

### Testing
- Unit tests alongside source files or in `src/test/`
- E2E tests in `tests/e2e/`
- Integration tests in `tests/integration/`
- Test setup in `src/test/setup.ts`

### Internationalization
- Locale files in `src/i18n/locales/`
- Route configuration in `src/i18n/routing.ts`
- Use `[locale]` dynamic route for i18n pages

### Environment & Configuration
- Environment variables validated in `src/env.ts`
- Use `.env.example` as template
- Configuration files in `config/` directory