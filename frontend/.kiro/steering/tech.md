# Tech Stack & Build System

## Core Framework
- **Next.js 15** with App Router and TypeScript
- **React 19** with Server Components (RSC)
- **TypeScript 5.8** with strict mode enabled

## UI & Styling
- **Tailwind CSS** with custom design system
- **shadcn/ui** components with Radix UI primitives
- **Lucide React** for icons
- **next-themes** for dark mode support
- CSS variables for theming with HSL color system

## Database & ORM
- **Drizzle ORM** with PostgreSQL dialect
- Multiple database provider support (Neon, PlanetScale, Turso, Xata, etc.)
- Database migrations via `drizzle-kit`

## Authentication
- **better-auth** for user authentication and management

## Internationalization
- **next-intl** for i18n support with locale routing

## Testing
- **Vitest** for unit testing with jsdom environment
- **Playwright** for E2E testing
- **Testing Library** for React component testing
- **Storybook** for component development and testing

## Code Quality
- **ESLint** with Next.js, TypeScript, and Prettier configs
- **Prettier** with Tailwind plugin for code formatting
- **TypeScript** strict mode with path aliases (`@/*` for src)

## Development Tools
- **Bun** as package manager (bun.lock present)
- **Docker** with multi-stage builds for development and production
- **Bundle Analyzer** for build analysis
- **Knip** for unused code detection
- **Codehawk** for code analysis

## Common Commands

### Development
```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run start        # Start production server
npm run type-check   # TypeScript type checking
```

### Database
```bash
npm run db:generate  # Generate database migrations
npm run db:migrate   # Apply database migrations
npm run db:studio    # Open Drizzle Studio
npm run db:seed      # Seed database
```

### Testing
```bash
npm run test         # Run unit tests
npm run test:watch   # Run tests in watch mode
npm run test:coverage # Run tests with coverage
npm run test:e2e     # Run E2E tests
npm run test:e2e:ui  # Run E2E tests with UI
```

### Code Quality
```bash
npm run lint         # Run ESLint
npm run lint:fix     # Fix ESLint issues
npm run format       # Format code with Prettier
npm run format:check # Check code formatting
npm run knip         # Check for unused code
```

### Docker
```bash
npm run docker:build # Build Docker image
npm run docker:dev   # Run development container
npm run docker:prod  # Run production container
npm run docker:test  # Run test container
```

### Storybook
```bash
npm run storybook       # Start Storybook dev server
npm run build-storybook # Build Storybook
```