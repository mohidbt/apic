# API Ingest Frontend

Modern Next.js frontend for the API Ingest application - converting OpenAPI specifications to LLM-ready markdown.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to see the application.

## ✨ Features

### 🏗️ **Core Framework**
- ⚡ **Next.js 15** with App Router & Server Components
- 🔷 **TypeScript 5.8** with strict configuration
- ⚛️ **React 19** with latest features

### 🎨 **UI & Styling**
- 🎯 **Tailwind CSS** with custom design system
- 🧩 **shadcn/ui** components with Radix UI primitives
- 🌙 **Dark mode** support with next-themes
- 🎭 **Lucide React** icons

### 🗄️ **Database & ORM**
- 🐘 **Drizzle ORM** with PostgreSQL support
- 🌐 **Multi-provider** support (Neon, PlanetScale, Turso, Xata)
- 🔄 **Database migrations** and seeding
- 🎛️ **Drizzle Studio** for database management

### 🌍 **Internationalization**
- 🗣️ **next-intl** for i18n support
- 🌐 **Locale routing** and translations

### 🧪 **Testing Suite**
- ⚡ **Vitest** for unit testing with jsdom
- 🎭 **Playwright** for E2E testing
- 🧪 **Testing Library** for React components
- 📚 **Storybook** for component development
- 📊 **Coverage reports** with v8

### 🔧 **Development Tools**
- 🎯 **ESLint** with Next.js & TypeScript configs
- 💅 **Prettier** with Tailwind plugin
- 🔍 **Knip** for unused code detection
- 🦅 **Codehawk** for code analysis
- 📦 **Bundle Analyzer** for optimization

## 📜 Available Scripts

### 🔧 **Development**
```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run start        # Start production server
npm run type-check   # TypeScript type checking
npm run clean        # Clean build artifacts
```

### 🗄️ **Database**
```bash
npm run db:generate  # Generate database migrations
npm run db:migrate   # Apply database migrations
npm run db:studio    # Open Drizzle Studio
npm run db:seed      # Seed database with sample data
```

### 🧪 **Testing**
```bash
npm run test         # Run unit tests
npm run test:watch   # Run tests in watch mode
npm run test:coverage # Run tests with coverage report
npm run test:e2e     # Run E2E tests
npm run test:e2e:ui  # Run E2E tests with UI
```

### 💅 **Code Quality**
```bash
npm run lint         # Run ESLint
npm run lint:fix     # Fix ESLint issues automatically
npm run format       # Format code with Prettier
npm run format:check # Check code formatting
npm run knip         # Check for unused code
npm run codehawk     # Analyze code quality
```

### 📚 **Storybook**
```bash
npm run storybook       # Start Storybook dev server
npm run build-storybook # Build Storybook for production
```

### 📊 **Analysis**
```bash
npm run analyze      # Analyze bundle size
```

## 📁 Project Structure

```
src/
├── app/            # Next.js App Router pages
├── components/     # Reusable React components
│   └── ui/         # shadcn/ui components
├── db/             # Database configuration & schema
├── hooks/          # Custom React hooks
├── i18n/           # Internationalization
├── lib/            # Utility libraries
├── styles/         # Global CSS
├── types/          # TypeScript definitions
└── utils/          # Helper functions
```

## 🔧 Configuration

### Environment Variables
Create a `.env.local` file:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

For production:
```env
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

## 🚀 Deployment

### Vercel Deployment
1. Connect your repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy automatically on push to main branch

### Koyeb Deployment
See the main [docs/DEPLOYMENT.md](../docs/DEPLOYMENT.md) for detailed instructions.

## 🤝 Contributing

Contributions are welcome! Please follow the project's code style and testing practices.

## 📄 License

MIT License - see [LICENSE](../LICENSE) file for details.

## 🙏 Acknowledgments

Built with modern web technologies:
- [Next.js](https://nextjs.org/) - The React framework
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [shadcn/ui](https://ui.shadcn.com/) - Beautiful UI components
- [Drizzle ORM](https://orm.drizzle.team/) - TypeScript ORM

---

**Made with ❤️ by Mohid Butt for API Ingest**
