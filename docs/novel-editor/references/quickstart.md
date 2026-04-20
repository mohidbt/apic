# Quickstart

Source: <https://novel.mintlify.dev/docs/quickstart>

## Install

The `novel` package ships **no styles** — it is a collection of custom Tiptap configs and React components.

```bash
npm i novel
# or
yarn add novel
# or
pnpm add novel
```

## Anatomy

Novel exports a Radix-Primitives-style component set. You compose them yourself:

```tsx
import {
  EditorBubble,
  EditorBubbleItem,
  EditorCommand,
  EditorCommandItem,
  EditorContent,
  EditorRoot,
} from "novel";

export default () => (
  <EditorRoot>
    <EditorContent>
      <EditorCommand>
        <EditorCommandItem />
        <EditorCommandItem />
        <EditorCommandItem />
      </EditorCommand>
      <EditorBubble>
        <EditorBubbleItem />
        <EditorBubbleItem />
        <EditorBubbleItem />
      </EditorBubble>
    </EditorContent>
  </EditorRoot>
);
```

## Two paths from here

1. **Tailwind + Shadcn-UI** — see `references/tailwind-setup.md`. The Novel example app uses this stack and it is the most documented path. Reference implementation: <https://github.com/steven-tey/novel/blob/main/apps/web/components/tailwind/advanced-editor.tsx>
2. **Custom styling** — use any styling system. The components are headless; you bring the CSS.

## Sub-paths exposed by the package

The `novel` package exposes additional sub-paths beyond the root export:

| Import path | Contains |
|---|---|
| `novel` | The React components (`EditorRoot`, `EditorContent`, `EditorBubble`, `EditorBubbleItem`, `EditorCommand`, `EditorCommandItem`, `EditorCommandEmpty`, `EditorCommandList`) and the `useEditor` hook. Also the `EditorInstance` type and `defaultEditorProps`. |
| `novel/extensions` | Re-exports of pre-configured Tiptap extensions: `StarterKit`, `Placeholder`, `TiptapLink`, `TiptapImage`, `UpdatedImage`, `TaskList`, `TaskItem`, `HorizontalRule`. Also helpers: `Command`, `createSuggestionItems`, `renderItems`, `handleCommandNavigation`. |
| `novel/plugins` | Plugin helpers for image handling: `UploadImagesPlugin`, `createImageUpload`, `handleImagePaste`, `handleImageDrop`, `startImageUpload`. |

## Minimum viable editor (no extensions, no menus)

```tsx
"use client";
import { EditorContent, EditorRoot } from "novel";

export default function MinimalEditor() {
  return (
    <EditorRoot>
      <EditorContent extensions={[]} />
    </EditorRoot>
  );
}
```

This renders a contenteditable Tiptap surface with zero behavior. You almost always want `defaultExtensions` from your own `extensions.ts` (see `references/extensions.md`) or at minimum Tiptap's `StarterKit`.
