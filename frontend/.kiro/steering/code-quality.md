# Code Quality & Standards

## Core Philosophy
Kiro prioritizes developer experience through intelligent code generation that emphasizes clarity, maintainability, and performance. These rules ensure consistent, production-ready code that follows modern best practices.

## Key Principles
- **Developer-First**: Code should be readable and maintainable by humans
- **Type Safety**: Leverage TypeScript's full potential for error prevention
- **Performance**: Write efficient code that scales
- **Accessibility**: Ensure inclusive user experiences
- **Consistency**: Follow established patterns and conventions

## Before Writing Code
1. Analyze existing codebase patterns and conventions
2. Consider edge cases, error scenarios, and user accessibility
3. Validate against project-specific requirements
4. Ensure code is immediately runnable and testable

## Accessibility Standards

### Interactive Elements
- Always include `type` attribute for button elements
- Accompany `onClick` with keyboard handlers (`onKeyUp`, `onKeyDown`, or `onKeyPress`)
- Accompany `onMouseOver`/`onMouseOut` with `onFocus`/`onBlur`
- Make elements with interactive roles focusable
- Don't assign `tabIndex` to non-interactive elements
- Don't use positive integers for `tabIndex`

### ARIA and Semantic HTML
- Use semantic HTML elements instead of ARIA roles when possible
- Don't add ARIA roles to elements that don't support them
- Include all required ARIA attributes for elements with ARIA roles
- Don't set `aria-hidden="true"` on focusable elements
- Ensure label elements have text content and are associated with inputs
- Always include `lang` attribute on html element

### Content and Media
- Provide meaningful alt text for images (avoid "image", "picture", "photo")
- Always include `title` element for SVG elements
- Include caption tracks for audio and video elements
- Ensure anchors have accessible content
- Don't use distracting elements like `<marquee>` or `<blink>`

## TypeScript Best Practices

### Type Safety
- Use strict TypeScript configuration
- Prefer `unknown` over `any` when type is uncertain
- Use `as const` for literal types instead of type annotations
- Export types with `export type`, import with `import type`
- Don't use non-null assertions (`!`) unless absolutely necessary

### Modern TypeScript
- Use `T[]` or `Array<T>` consistently (prefer `T[]`)
- Don't use TypeScript enums (prefer const objects or union types)
- Don't use TypeScript namespaces
- Avoid parameter properties in class constructors
- Don't declare empty interfaces

## React & Next.js Patterns

### Component Design
- Don't define components inside other components
- Use default exports for components
- Don't pass children as props (use React children pattern)
- Don't use Array index as keys in lists
- Use `<>...</>` instead of `<Fragment>...</Fragment>`

### Hooks and State
- Call hooks only at the top level of components
- Include all dependencies in hook dependency arrays
- Don't use the return value of `React.render`
- Don't destructure props inside JSX components

### Next.js Specific
- Use `next/image` instead of `<img>` elements
- Use `next/head` for metadata (not in `_document.js`)
- Don't import `next/document` outside of `pages/_document.jsx`
- Leverage App Router patterns for new projects

## Code Quality & Performance

### Function Design
- Use arrow functions for inline functions and callbacks
- Keep functions focused and under reasonable complexity
- Use early returns to reduce nesting
- Don't use unnecessary constructors or empty functions

### Data Handling
- Use `for...of` instead of `Array.forEach` for better performance
- Use `.flatMap()` instead of `.map().flat()`
- Use object spread instead of `Object.assign()` for new objects
- Use optional chaining (`?.`) instead of chained logical expressions

### Error Handling
- Always handle Promise rejections appropriately
- Use proper error boundaries in React applications
- Don't swallow errors silently
- Provide meaningful error messages

```typescript
// ✅ Good: Comprehensive error handling
const fetchUserData = async (id: string) => {
  try {
    const response = await api.getUser(id);
    return { success: true, data: response };
  } catch (error) {
    console.error('Failed to fetch user:', error);
    return { 
      success: false, 
      error: error instanceof Error ? error.message : 'Unknown error' 
    };
  }
};

// ❌ Bad: Swallowing errors
const fetchUserData = async (id: string) => {
  try {
    return await api.getUser(id);
  } catch (e) {
    console.log(e);
  }
};
```

## Modern JavaScript Practices

### Syntax and Style
- Use `const` for variables that don't change, `let` for those that do
- Never use `var`
- Use template literals for string interpolation
- Use destructuring for object and array access
- Use shorthand property syntax in objects

### Built-in Methods
- Use `Date.now()` instead of `new Date().getTime()`
- Use `Number.isNaN()` instead of global `isNaN()`
- Use `Array.isArray()` instead of `instanceof Array`
- Use `String.startsWith()`/`endsWith()` instead of regex when appropriate

### Async/Await
- Don't use `await` inside loops (use `Promise.all()` for parallel execution)
- Don't use async functions as Promise executors
- Always handle async errors appropriately

## Security & Safety

### Data Protection
- Don't hardcode sensitive data (API keys, tokens, passwords)
- Validate and sanitize user inputs
- Use environment variables for configuration
- Don't use `eval()` or similar dynamic code execution

### Safe Practices
- Don't use `target="_blank"` without `rel="noopener"`
- Validate external data before processing
- Use HTTPS for all external requests
- Implement proper CORS policies

## Testing Standards

### Test Structure
- Place assertion functions inside `it()` blocks
- Don't use focused tests (`fit`, `fdescribe`) in committed code
- Don't use disabled tests without good reason
- Write descriptive test names that explain the expected behavior

### Test Quality
- Test both happy path and error scenarios
- Mock external dependencies appropriately
- Use proper setup and teardown
- Maintain test isolation

## Database & API Patterns

### Drizzle ORM
- Use schema files in `src/db/schema/`
- Follow Drizzle naming conventions
- Use migrations for schema changes
- Implement proper connection pooling

### API Design
- Follow RESTful conventions
- Use proper HTTP status codes
- Implement consistent error response format
- Use route handlers for different HTTP methods
- Validate request data with Zod schemas

## Performance Optimization

### Bundle Size
- Use dynamic imports for code splitting
- Avoid importing entire libraries when only specific functions are needed
- Use tree-shaking friendly imports
- Optimize images and assets

### Runtime Performance
- Minimize re-renders in React components
- Use React.memo() and useMemo() judiciously
- Implement proper loading states
- Use efficient data structures

## Common Anti-Patterns to Avoid

### Code Smells
- Don't use magic numbers or strings
- Avoid deeply nested code
- Don't create overly complex functions
- Avoid duplicate code

### React Anti-Patterns
- Don't mutate props or state directly
- Don't use array indices as keys
- Don't call hooks conditionally
- Don't use refs for everything

### TypeScript Anti-Patterns
- Don't use `any` type
- Don't ignore TypeScript errors with `@ts-ignore`
- Don't use function overloads unnecessarily
- Don't create overly complex type definitions