# Slash Command

Source: <https://novel.mintlify.dev/docs/guides/tailwind/slash-command>

The slash command is the `/` palette that lets users insert blocks (paragraph, heading, list, image, quote, code, etc.).

It is built from three parts:

1. **Suggestion items** — the data: title, description, search terms, icon, and a `command` callback.
2. **The `slashCommand` extension** — wraps Novel's `Command` extension with your suggestion items + the `renderItems` renderer.
3. **The UI** — `EditorCommand`, `EditorCommandEmpty`, `EditorCommandList`, `EditorCommandItem` (cmdk wrappers).

## 1. Define the suggestion items

Use the `createSuggestionItems` helper — it is just a typed identity function so TypeScript infers the right shape.

```tsx
// slash-command.tsx
import {
  CheckSquare,
  Code,
  Heading1,
  Heading2,
  Heading3,
  List,
  ListOrdered,
  MessageSquarePlus,
  Text,
  TextQuote,
} from "lucide-react";
import { createSuggestionItems } from "novel/extensions";
import { Command, renderItems } from "novel/extensions";

export const suggestionItems = createSuggestionItems([
  {
    title: "Send Feedback",
    description: "Let us know how we can improve.",
    icon: <MessageSquarePlus size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).run();
      window.open("/feedback", "_blank");
    },
  },
  {
    title: "Text",
    description: "Just start typing with plain text.",
    searchTerms: ["p", "paragraph"],
    icon: <Text size={18} />,
    command: ({ editor, range }) => {
      editor
        .chain()
        .focus()
        .deleteRange(range)
        .toggleNode("paragraph", "paragraph")
        .run();
    },
  },
  {
    title: "To-do List",
    description: "Track tasks with a to-do list.",
    searchTerms: ["todo", "task", "list", "check", "checkbox"],
    icon: <CheckSquare size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).toggleTaskList().run();
    },
  },
  {
    title: "Heading 1",
    description: "Big section heading.",
    searchTerms: ["title", "big", "large"],
    icon: <Heading1 size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).setNode("heading", { level: 1 }).run();
    },
  },
  {
    title: "Heading 2",
    description: "Medium section heading.",
    searchTerms: ["subtitle", "medium"],
    icon: <Heading2 size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).setNode("heading", { level: 2 }).run();
    },
  },
  {
    title: "Heading 3",
    description: "Small section heading.",
    searchTerms: ["subtitle", "small"],
    icon: <Heading3 size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).setNode("heading", { level: 3 }).run();
    },
  },
  {
    title: "Bullet List",
    description: "Create a simple bullet list.",
    searchTerms: ["unordered", "point"],
    icon: <List size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).toggleBulletList().run();
    },
  },
  {
    title: "Numbered List",
    description: "Create a list with numbering.",
    searchTerms: ["ordered"],
    icon: <ListOrdered size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).toggleOrderedList().run();
    },
  },
  {
    title: "Quote",
    description: "Capture a quote.",
    searchTerms: ["blockquote"],
    icon: <TextQuote size={18} />,
    command: ({ editor, range }) =>
      editor
        .chain()
        .focus()
        .deleteRange(range)
        .toggleNode("paragraph", "paragraph")
        .toggleBlockquote()
        .run(),
  },
  {
    title: "Code",
    description: "Capture a code snippet.",
    searchTerms: ["codeblock"],
    icon: <Code size={18} />,
    command: ({ editor, range }) =>
      editor.chain().focus().deleteRange(range).toggleCodeBlock().run(),
  },
]);

export const slashCommand = Command.configure({
  suggestion: {
    items: () => suggestionItems,
    render: renderItems,
  },
});
```

### Suggestion item shape

| Field | Type | Notes |
|---|---|---|
| `title` | `string` | Display name; also the cmdk `value` used for filtering. |
| `description` | `string` | Subtext under the title. |
| `searchTerms` | `string[]` | Extra strings cmdk matches against (synonyms, abbreviations). |
| `icon` | `ReactNode` | Lucide icon or any React element. |
| `command` | `({ editor, range }) => void` | The action. **Always start with `editor.chain().focus().deleteRange(range)`** to remove the typed `/foo` text before applying your transform. |

## 2. Register the extension

Add `slashCommand` to your `extensions` array.

```tsx
import { defaultExtensions } from "./extensions";
import { slashCommand } from "./slash-command";

const extensions = [...defaultExtensions, slashCommand];

<EditorContent extensions={extensions} ... />
```

## 3. Wire the keyboard navigation

Without this, arrow keys don't move the slash menu's selection:

```tsx
import { handleCommandNavigation } from "novel/extensions";

<EditorContent
  ...
  editorProps={{
    handleDOMEvents: {
      keydown: (_view, event) => handleCommandNavigation(event),
    },
  }}
/>
```

## 4. Build the palette UI

```tsx
import {
  EditorCommand,
  EditorCommandEmpty,
  EditorCommandItem,
  EditorCommandList,
} from "novel";
import { suggestionItems } from "./slash-command";

<EditorContent>
  <EditorCommand className="z-50 h-auto max-h-[330px] w-72 overflow-y-auto rounded-md border border-muted bg-background px-1 py-2 shadow-md transition-all">
    <EditorCommandEmpty className="px-2 text-muted-foreground">
      No results
    </EditorCommandEmpty>
    <EditorCommandList>
      {suggestionItems.map((item) => (
        <EditorCommandItem
          value={item.title}
          onCommand={(val) => item.command(val)}
          className="flex w-full items-center space-x-2 rounded-md px-2 py-1 text-left text-sm hover:bg-accent aria-selected:bg-accent"
          key={item.title}
        >
          <div className="flex h-10 w-10 items-center justify-center rounded-md border border-muted bg-background">
            {item.icon}
          </div>
          <div>
            <p className="font-medium">{item.title}</p>
            <p className="text-xs text-muted-foreground">{item.description}</p>
          </div>
        </EditorCommandItem>
      ))}
    </EditorCommandList>
  </EditorCommand>
</EditorContent>
```

### Why the wrappers exist

`EditorCommand`, `EditorCommandEmpty`, `EditorCommandList`, and `EditorCommandItem` are thin wrappers around cmdk's `Command`, `Command.Empty`, `Command.List`, and `Command.Item`. They provide:

- The cmdk root context.
- The `aria-selected` styling hook (use `aria-selected:bg-accent` in Tailwind).
- The `onCommand({ editor, range })` callback shape that exposes the slash trigger range so your command can `deleteRange(range)`.

## Adding more commands

Append to the `createSuggestionItems` array. Common additions:

- **Image** — see `references/image-upload.md` for the file-input + `uploadFn` recipe.
- **Divider** — `editor.chain().focus().deleteRange(range).setHorizontalRule().run()`.
- **Table, YouTube, embeds** — install the corresponding Tiptap extension, add to your `extensions` array, and add the matching suggestion item.
