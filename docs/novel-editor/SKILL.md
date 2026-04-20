---
name: novel-editor
description: Use when working with the Novel editor library (the headless Notion-style WYSIWYG editor by steven-tey, npm package `novel`). Triggers include any mention of Novel, building a Notion-style block editor in React/Next.js, slash-command menus, bubble menus, headless rich text editor with Tiptap+cmdk+RadixUI, EditorRoot/EditorContent/EditorBubble/EditorCommand components, `useEditor` hook from novel, `createSuggestionItems`, `UploadImagesPlugin`, novel/extensions, novel/plugins, or wiring image upload, drag handles, and prose styling for the Novel editor.
---

# Novel Editor

## Overview

[Novel](https://github.com/steven-tey/novel) is a **headless Notion-style WYSIWYG editor** for React, distributed as the `novel` npm package. It is a thin set of composable wrapper components and helpers built on top of:

- **Tiptap** — the underlying editor framework (most editor behavior comes from Tiptap)
- **cmdk** — powers the slash-command palette
- **RadixUI** — primitive components for popovers/menus
- **TypeScript** — fully typed

Novel ships **no styles**. It is a Radix-Primitives-style component kit you assemble into your own editor — typically with Tiptap extensions for behavior and Tailwind/Shadcn-UI for visuals.

## When to use this skill

Use whenever you are:

- Adding the `novel` package to a project, or reading/editing code that imports from `novel`, `novel/extensions`, or `novel/plugins`.
- Building a Notion-style block editor in React/Next.js with slash menus, bubble menus, drag handles, image uploads, or task lists.
- Wiring `EditorRoot`, `EditorContent`, `EditorBubble`, `EditorBubbleItem`, `EditorCommand`, `EditorCommandItem`, or the `useEditor` hook.
- Configuring Tiptap extensions for use inside Novel (StarterKit, TiptapLink, TiptapImage, TaskList, Placeholder, etc. re-exported from `novel/extensions`).

Do **not** use this skill for:
- Plain Tiptap projects that don't import `novel` — go straight to Tiptap docs.
- Other Notion clones (BlockNote, Plate, Lexical, etc.).
- The Svelte port (`novel-svelte`) — different API surface.

## Critical mental model

> Novel ≠ Editor framework. Novel = **wrappers + sensible defaults + cmdk integration** on top of Tiptap.

Implications:

1. **Most "editor" behavior is Tiptap.** Commands like `editor.chain().focus().toggleBold().run()`, `editor.isActive('heading', { level: 1 })`, `editor.getJSON()` are all Tiptap. When in doubt about an editor method, look at Tiptap's [Editor API](https://tiptap.dev/docs/editor/api/editor), not Novel.
2. **`EditorContent` props extend Tiptap settings.** See [Tiptap Settings](https://tiptap.dev/docs/editor/api/editor#settings) for the full prop surface beyond what Novel documents.
3. **`EditorBubble` is a Tiptap BubbleMenu wrapper.** `tippyOptions` are the Tippy.js options.
4. **`EditorCommand` / `EditorCommandItem` wrap [cmdk](https://github.com/pacocoursey/cmdk).** Filter, search, and aria-selected behavior come from cmdk.
5. **Headless = you own the styling.** Even the "Tailwind" guide is just *one* convention; you may use any styling solution.

## Live documentation via Context7

For the freshest API details and code snippets beyond what is captured in this skill, query Context7:

```
Context7 Library ID: /websites/novel_sh
```

Use it for: latest snippet patterns, version-specific changes, anything that may have evolved after this skill was written.

## Reference map

This skill keeps the deep details in topic-specific reference files. Read the one that matches the task. **Do not read all of them up front.**

| Reference | Read when you are… |
|---|---|
| [`references/quickstart.md`](references/quickstart.md) | Installing `novel` for the first time, or need the minimal anatomy. |
| [`references/components-api.md`](references/components-api.md) | Looking up props/types for any Novel component or the `useEditor` hook. |
| [`references/tailwind-setup.md`](references/tailwind-setup.md) | Setting up Novel with Tailwind + Shadcn-UI, including all required CSS (ProseMirror styles, highlight CSS variables, prose typography). |
| [`references/extensions.md`](references/extensions.md) | Configuring the default Tiptap extensions (StarterKit, TiptapLink, TiptapImage, TaskList, Placeholder, etc.) with the `cx()` Tailwind helper. |
| [`references/slash-command.md`](references/slash-command.md) | Building the `/`-triggered command palette via `createSuggestionItems`, `Command`, `renderItems`, and the `EditorCommand*` UI. |
| [`references/bubble-menu.md`](references/bubble-menu.md) | Building the floating selection toolbar — Node selector, Link selector, Text-formatting buttons, Color/Highlight selector. |
| [`references/image-upload.md`](references/image-upload.md) | Implementing image upload with `UploadImagesPlugin`, `createImageUpload`, `handleImagePaste`, `handleImageDrop`, and the slash-command image entry. |
| [`references/global-drag-handle.md`](references/global-drag-handle.md) | Adding the block drag handle (`tiptap-extension-global-drag-handle` + optional `tiptap-extension-auto-joiner`) and styling the `.drag-handle` class. |
| [`references/development.md`](references/development.md) | Contributing to the Novel monorepo or running it locally. |

## Common gotchas

- **Forgot `handleCommandNavigation`** → arrow keys don't navigate the slash menu. It must be wired into `editorProps.handleDOMEvents.keydown` (see `tailwind-setup.md`).
- **Slash menu drag-handle position is wrong inside a custom dialog** → Novel auto-detects Radix dialogs via `[role="dialog"]`; non-Radix popups need that attribute on the closest ancestor.
- **`onUpdate` runs on every keystroke** → debounce it (e.g. with `use-debounce`'s `useDebouncedCallback`) before persisting state.
- **`useEditor()` returns `{ editor: null }` outside `EditorRoot`** → always render the consumer as a descendant of `EditorRoot`.
- **`@tailwindcss/typography` plugin is mandatory** for the prose styling shown in the Tailwind guide.
- **`EditorCommandEmpty` and `EditorCommandList`** are exported but not separately documented — they appear in the slash-command UI example. They are cmdk wrappers; treat them like `Command.Empty` / `Command.List`.
- **The AI Command guide is "coming soon"** — Novel's example app uses an OpenAI-compatible endpoint at `/api/generate/route.ts` (Ollama works locally). No first-class `novel/ai` API exists yet.
