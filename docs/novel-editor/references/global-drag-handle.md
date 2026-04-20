# Global Drag Handle

Source: <https://novel.mintlify.dev/docs/guides/global-drag-handle>

Adds the Notion-style left-margin **⋮⋮ drag handle** that lets users drag any block (paragraph, heading, list, image, etc.) to a new position.

This is **not** part of the `novel` package — it's a standalone third-party Tiptap extension. Novel just integrates with it (its CSS and the dialog-detection logic live in Novel's example app).

## Install

```bash
npm i tiptap-extension-global-drag-handle
# Optional companion: auto-merges adjacent same-type lists after a drag.
npm i tiptap-extension-auto-joiner
```

## Add to extensions

```tsx
// extensions.ts
import GlobalDragHandle from "tiptap-extension-global-drag-handle";
import AutoJoiner from "tiptap-extension-auto-joiner"; // optional

export const defaultExtensions = [
  GlobalDragHandle,
  AutoJoiner, // optional
  // other extensions
];
```

## Configure

```tsx
import GlobalDragHandle from "tiptap-extension-global-drag-handle";
import AutoJoiner from "tiptap-extension-auto-joiner";

export const defaultExtensions = [
  GlobalDragHandle.configure({
    dragHandleWidth: 20, // default
    // How close (px) the user must drag a block to the screen edge before
    // auto-scrolling kicks in. 100 = scroll when within 100px of the edge.
    // Set to 0 to disable this extension's auto-scroll entirely.
    scrollTreshold: 100, // default; note: typo "Treshold" is the real option name
  }),
  AutoJoiner.configure({
    elementsToJoin: ["bulletList", "orderedList"], // default
  }),
  // other extensions
];
```

> The option is spelled **`scrollTreshold`** (missing "h") in the upstream extension. Don't "correct" it.

## Style it

The extension is headless — no CSS shipped. Style via the `.drag-handle` class. The full reference style (with light/dark SVG, hover/active states, mobile hide) is in `prosemirror.css` from `references/tailwind-setup.md`.

Minimal example:

```css
.drag-handle {
  position: fixed;
  width: 1.2rem;
  height: 1.5rem;
  cursor: grab;
  border-radius: 0.25rem;
  background: url("...your dots SVG...") center / contain no-repeat;
}

.drag-handle:active { cursor: grabbing; }
.drag-handle.hide   { opacity: 0; pointer-events: none; }
```

The class `.hide` is toggled by the extension when the handle should disappear (e.g. between blocks, on mobile).

## Working inside dialogs/popovers

The drag handle calculates its position relative to the closest ancestor with `[role="dialog"]` (this is what makes it work seamlessly inside Radix Dialogs). If you mount the editor inside a *non-Radix* dialog, **add `role="dialog"` to the dialog wrapper** so the handle aligns correctly. (See the Tailwind setup guide for the full note.)

## Pairing with the StarterKit gapcursor

The Novel example disables `gapcursor` in StarterKit:

```tsx
StarterKit.configure({
  gapcursor: false,
});
```

This avoids visual conflict with the drag-handle's own block boundaries. If you re-enable `gapcursor`, expect some overlap.
