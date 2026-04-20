# Default Extensions

Source: <https://novel.mintlify.dev/docs/guides/tailwind/extensions>

> Novel re-exports a curated set of Tiptap extensions from `novel/extensions`. You may also use any third-party Tiptap extension or write your own — Novel adds no constraints there.

## The default kit

Re-exported from `novel/extensions`:

| Extension | Tiptap origin | Purpose |
|---|---|---|
| `StarterKit` | `@tiptap/starter-kit` | Bundle of the core nodes/marks (paragraph, heading, lists, code, blockquote, etc.). |
| `Placeholder` | `@tiptap/extension-placeholder` | Empty-state placeholder text. |
| `TiptapLink` | `@tiptap/extension-link` | Hyperlinks. |
| `TiptapImage` | `@tiptap/extension-image` | Images. |
| `UpdatedImage` | Tiptap-based custom node | Image with extra update behavior. |
| `TaskList` | `@tiptap/extension-task-list` | The `<ul data-type="taskList">` container. |
| `TaskItem` | `@tiptap/extension-task-item` | Individual checkbox items. |
| `HorizontalRule` | `@tiptap/extension-horizontal-rule` | `<hr>` block. |

## Reference `extensions.ts`

This is the recommended default config straight from the Novel example app. Lift it as-is and tweak from there.

```tsx
// extensions.ts
import {
  TiptapImage,
  TiptapLink,
  UpdatedImage,
  TaskList,
  TaskItem,
  HorizontalRule,
  StarterKit,
  Placeholder,
} from "novel/extensions";

import { cx } from "class-variance-authority";

// `cx` is used so Tailwind IntelliSense fires on the strings inside.

const placeholder = Placeholder;

const tiptapLink = TiptapLink.configure({
  HTMLAttributes: {
    class: cx(
      "text-muted-foreground underline underline-offset-[3px] hover:text-primary transition-colors cursor-pointer",
    ),
  },
});

const taskList = TaskList.configure({
  HTMLAttributes: { class: cx("not-prose pl-2") },
});

const taskItem = TaskItem.configure({
  HTMLAttributes: { class: cx("flex items-start my-4") },
  nested: true,
});

const horizontalRule = HorizontalRule.configure({
  HTMLAttributes: { class: cx("mt-4 mb-6 border-t border-muted-foreground") },
});

const starterKit = StarterKit.configure({
  bulletList: {
    HTMLAttributes: { class: cx("list-disc list-outside leading-3 -mt-2") },
  },
  orderedList: {
    HTMLAttributes: { class: cx("list-decimal list-outside leading-3 -mt-2") },
  },
  listItem: {
    HTMLAttributes: { class: cx("leading-normal -mb-2") },
  },
  blockquote: {
    HTMLAttributes: { class: cx("border-l-4 border-primary") },
  },
  codeBlock: {
    HTMLAttributes: {
      class: cx("rounded-sm bg-muted border p-5 font-mono font-medium"),
    },
  },
  code: {
    HTMLAttributes: {
      class: cx("rounded-md bg-muted px-1.5 py-1 font-mono font-medium"),
      spellcheck: "false",
    },
  },
  // The configured `horizontalRule` above replaces StarterKit's version.
  horizontalRule: false,
  dropcursor: { color: "#DBEAFE", width: 4 },
  // `gapcursor` disabled because it interferes with the global drag handle styling.
  gapcursor: false,
});

export const defaultExtensions = [
  starterKit,
  placeholder,
  TiptapLink,        // re-included unconfigured; the `tiptapLink` above is unused in the official kit
  TiptapImage,
  UpdatedImage,
  taskList,
  taskItem,
  horizontalRule,
];
```

> Note: the official kit exports both the configured `tiptapLink` and the bare `TiptapLink`, then ships the bare one in `defaultExtensions`. If you want the styled link, swap `TiptapLink` for `tiptapLink` in the array.

## Adding the slash command and other extras

```tsx
import { defaultExtensions } from "./extensions";
import { slashCommand } from "./slash-command";
import GlobalDragHandle from "tiptap-extension-global-drag-handle";
import AutoJoiner from "tiptap-extension-auto-joiner";

const extensions = [
  ...defaultExtensions,
  slashCommand,
  GlobalDragHandle,
  AutoJoiner,
];
```

## Tailwind IntelliSense inside `cx()`

The official guide recommends adding this regex to your VS Code `settings.json` so Tailwind class autocompletion fires inside `cx(...)`:

```json
{
  "tailwindCSS.experimental.classRegex": [
    ["cx\\(([^)]*)\\)", "(?:'|\"|`)([^']*)(?:'|\"|`)"]
  ]
}
```

## Custom extensions

Novel docs say *"Custom Extension — coming soon."* Until that lands, build any custom node/mark via the standard Tiptap pattern (`Node.create({...})`, `Mark.create({...})`, `Extension.create({...})`) and just add it to the `extensions` array.
