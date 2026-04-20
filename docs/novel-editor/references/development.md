# Development / Contributing

Source: <https://novel.mintlify.dev/docs/development>

> Read this file only when running the **Novel repo itself** locally (e.g. to contribute, test the example app, or hack on the package). For *consuming* `novel` from npm in your own app, you don't need any of this — go to `references/quickstart.md`.

## Prerequisite

Node.js **18.10.0 or higher**.

## Repo layout

The repo is a [Turborepo](https://turbo.build/repo) monorepo:

```
apps/
├── docs        # Mintlify docs site (the source of these reference pages)
├── web         # Demo app — uses Tailwind + Shadcn-UI build of Novel
packages/
├── headless          # The published `novel` package
├── tailwind-config   # Shared Tailwind preset
```

## Local setup

```bash
git clone https://github.com/steven-tey/novel
cd novel
pnpm i
pnpm i -g mintlify    # Required only if you want to run the docs server
pnpm dev              # Builds packages + starts the web/docs apps
```

`pnpm dev` runs the Turborepo dev pipeline: it builds `packages/headless` in watch mode and starts the Next.js apps under `apps/`.

## Local generative AI (optional)

The example app has an OpenAI-compatible AI endpoint at `apps/web/api/generate/route.ts`. Point it at any OpenAI-compatible server — including a local **Ollama** instance — by configuring the base URL/model in that file.

See <https://ollama.com/blog/openai-compatibility> for Ollama's OpenAI-compatibility shim.

## Where to look for things

| Looking for… | Path |
|---|---|
| The published `novel` package source | `packages/headless/src/` |
| Reference Tailwind/Shadcn editor implementation | `apps/web/components/tailwind/advanced-editor.tsx` |
| Reference `prosemirror.css` (drag handle, placeholder, task list, etc.) | `apps/web/styles/prosemirror.css` |
| AI route used by the example | `apps/web/api/generate/route.ts` |
| Docs source files (these `.md` pages) | `apps/docs/` |
