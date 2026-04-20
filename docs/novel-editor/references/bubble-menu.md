# Bubble Menu (Selection Toolbar)

Source: <https://novel.mintlify.dev/docs/guides/tailwind/bubble-menu>

The bubble menu is the floating toolbar that appears when text is selected. The official tailwind/Shadcn-UI build is composed of four selectors mounted inside one `EditorBubble`:

1. **Node Selector** — Convert the active block (paragraph, H1–H3, bullet/ordered/to-do list, quote, code).
2. **Link Selector** — Set or remove a hyperlink with URL validation.
3. **Text Buttons** — Toggle inline marks (bold, italic, underline, strike, code).
4. **Color Selector** — Set the text color and highlight background.

All selectors talk to the editor via `useEditor()` and `EditorBubbleItem`'s `onSelect`.

---

## Composition

```tsx
import { NodeSelector } from "./selectors/node-selector";
import { LinkSelector } from "./selectors/link-selector";
import { ColorSelector } from "./selectors/color-selector";
import { TextButtons } from "./selectors/text-buttons";
import { EditorBubble, EditorContent } from "novel";

<EditorContent>
  <EditorBubble
    tippyOptions={{
      placement: openAI ? "bottom-start" : "top",
    }}
    className="flex w-fit max-w-[90vw] overflow-hidden rounded border border-muted bg-background shadow-xl"
  >
    <NodeSelector open={openNode} onOpenChange={setOpenNode} />
    <LinkSelector open={openLink} onOpenChange={setOpenLink} />
    <TextButtons />
    <ColorSelector open={openColor} onOpenChange={setOpenColor} />
  </EditorBubble>
</EditorContent>
```

Each selector with a popover takes its own `open` / `onOpenChange` so the parent owns the open-state and can ensure only one popover is open at a time.

---

## Shared item type

Used by Node Selector and Text Buttons.

```tsx
import type { LucideIcon } from "lucide-react";
import type { useEditor } from "novel";

export type SelectorItem = {
  name: string;
  icon: LucideIcon;
  command: (editor: ReturnType<typeof useEditor>["editor"]) => void;
  isActive: (editor: ReturnType<typeof useEditor>["editor"]) => boolean;
};
```

---

## Node Selector

```tsx
// node-selector.tsx
import {
  Check,
  ChevronDown,
  Heading1,
  Heading2,
  Heading3,
  TextQuote,
  ListOrdered,
  TextIcon,
  Code,
  CheckSquare,
  type LucideIcon,
} from "lucide-react";
import { EditorBubbleItem, useEditor } from "novel";

import { Popover } from "@radix-ui/react-popover";
import { PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Button } from "@/components/ui/button";

export type SelectorItem = {
  name: string;
  icon: LucideIcon;
  command: (editor: ReturnType<typeof useEditor>["editor"]) => void;
  isActive: (editor: ReturnType<typeof useEditor>["editor"]) => boolean;
};

const items: SelectorItem[] = [
  {
    name: "Text",
    icon: TextIcon,
    command: (editor) => editor.chain().focus().toggleNode("paragraph", "paragraph").run(),
    isActive: (editor) =>
      editor.isActive("paragraph") &&
      !editor.isActive("bulletList") &&
      !editor.isActive("orderedList"),
  },
  {
    name: "Heading 1",
    icon: Heading1,
    command: (editor) => editor.chain().focus().toggleHeading({ level: 1 }).run(),
    isActive: (editor) => editor.isActive("heading", { level: 1 }),
  },
  {
    name: "Heading 2",
    icon: Heading2,
    command: (editor) => editor.chain().focus().toggleHeading({ level: 2 }).run(),
    isActive: (editor) => editor.isActive("heading", { level: 2 }),
  },
  {
    name: "Heading 3",
    icon: Heading3,
    command: (editor) => editor.chain().focus().toggleHeading({ level: 3 }).run(),
    isActive: (editor) => editor.isActive("heading", { level: 3 }),
  },
  {
    name: "To-do List",
    icon: CheckSquare,
    command: (editor) => editor.chain().focus().toggleTaskList().run(),
    isActive: (editor) => editor.isActive("taskItem"),
  },
  {
    name: "Bullet List",
    icon: ListOrdered,
    command: (editor) => editor.chain().focus().toggleBulletList().run(),
    isActive: (editor) => editor.isActive("bulletList"),
  },
  {
    name: "Numbered List",
    icon: ListOrdered,
    command: (editor) => editor.chain().focus().toggleOrderedList().run(),
    isActive: (editor) => editor.isActive("orderedList"),
  },
  {
    name: "Quote",
    icon: TextQuote,
    command: (editor) =>
      editor.chain().focus().toggleNode("paragraph", "paragraph").toggleBlockquote().run(),
    isActive: (editor) => editor.isActive("blockquote"),
  },
  {
    name: "Code",
    icon: Code,
    command: (editor) => editor.chain().focus().toggleCodeBlock().run(),
    isActive: (editor) => editor.isActive("codeBlock"),
  },
];

interface NodeSelectorProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const NodeSelector = ({ open, onOpenChange }: NodeSelectorProps) => {
  const { editor } = useEditor();
  if (!editor) return null;
  const activeItem = items.filter((item) => item.isActive(editor)).pop() ?? {
    name: "Multiple",
  };

  return (
    <Popover modal={true} open={open} onOpenChange={onOpenChange}>
      <PopoverTrigger
        asChild
        className="gap-2 rounded-none border-none hover:bg-accent focus:ring-0"
      >
        <Button variant="ghost" className="gap-2">
          <span className="whitespace-nowrap text-sm">{activeItem.name}</span>
          <ChevronDown className="h-4 w-4" />
        </Button>
      </PopoverTrigger>
      <PopoverContent sideOffset={5} align="start" className="w-48 p-1">
        {items.map((item, index) => (
          <EditorBubbleItem
            key={index}
            onSelect={(editor) => {
              item.command(editor);
              onOpenChange(false);
            }}
            className="flex cursor-pointer items-center justify-between rounded-sm px-2 py-1 text-sm hover:bg-accent"
          >
            <div className="flex items-center space-x-2">
              <div className="rounded-sm border p-1">
                <item.icon className="h-3 w-3" />
              </div>
              <span>{item.name}</span>
            </div>
            {activeItem.name === item.name && <Check className="h-4 w-4" />}
          </EditorBubbleItem>
        ))}
      </PopoverContent>
    </Popover>
  );
};
```

---

## Link Selector

Includes URL validation/normalization helpers (`isValidUrl`, `getUrlFromString`) — paste-friendly: bare strings like `example.com` get auto-prefixed with `https://`.

```tsx
// link-selector.tsx
import { cn } from "@/lib/utils";
import { useEditor } from "novel";
import { Check, Trash } from "lucide-react";
import { useEffect, useRef } from "react";
import { Popover, PopoverTrigger } from "@radix-ui/react-popover";
import { Button } from "@/components/tailwind/ui/button";
import { PopoverContent } from "@/components/tailwind/ui/popover";

export function isValidUrl(url: string) {
  try {
    new URL(url);
    return true;
  } catch (e) {
    return false;
  }
}

export function getUrlFromString(str: string) {
  if (isValidUrl(str)) return str;
  try {
    if (str.includes(".") && !str.includes(" ")) {
      return new URL(`https://${str}`).toString();
    }
  } catch (e) {
    return null;
  }
}

interface LinkSelectorProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const LinkSelector = ({ open, onOpenChange }: LinkSelectorProps) => {
  const inputRef = useRef<HTMLInputElement>(null);
  const { editor } = useEditor();

  useEffect(() => {
    inputRef.current && inputRef.current?.focus();
  });

  if (!editor) return null;

  return (
    <Popover modal={true} open={open} onOpenChange={onOpenChange}>
      <PopoverTrigger asChild>
        <Button variant="ghost" className="gap-2 rounded-none border-none">
          <p className="text-base">↗</p>
          <p
            className={cn("underline decoration-stone-400 underline-offset-4", {
              "text-blue-500": editor.isActive("link"),
            })}
          >
            Link
          </p>
        </Button>
      </PopoverTrigger>
      <PopoverContent align="start" className="w-60 p-0" sideOffset={10}>
        <form
          onSubmit={(e) => {
            const target = e.currentTarget as HTMLFormElement;
            e.preventDefault();
            const input = target[0] as HTMLInputElement;
            const url = getUrlFromString(input.value);
            url && editor.chain().focus().setLink({ href: url }).run();
          }}
          className="flex p-1"
        >
          <input
            ref={inputRef}
            type="text"
            placeholder="Paste a link"
            className="flex-1 bg-background p-1 text-sm outline-none"
            defaultValue={editor.getAttributes("link").href || ""}
          />
          {editor.getAttributes("link").href ? (
            <Button
              size="icon"
              variant="outline"
              type="button"
              className="flex h-8 items-center rounded-sm p-1 text-red-600 transition-all hover:bg-red-100 dark:hover:bg-red-800"
              onClick={() => {
                editor.chain().focus().unsetLink().run();
              }}
            >
              <Trash className="h-4 w-4" />
            </Button>
          ) : (
            <Button size="icon" className="h-8">
              <Check className="h-4 w-4" />
            </Button>
          )}
        </form>
      </PopoverContent>
    </Popover>
  );
};
```

---

## Text Buttons (inline marks)

```tsx
// text-buttons.tsx
import { cn } from "@/lib/utils";
import { EditorBubbleItem, useEditor } from "novel";
import { BoldIcon, ItalicIcon, UnderlineIcon, StrikethroughIcon, CodeIcon } from "lucide-react";
import type { SelectorItem } from "./node-selector";
import { Button } from "@/components/tailwind/ui/button";

export const TextButtons = () => {
  const { editor } = useEditor();
  if (!editor) return null;

  const items: SelectorItem[] = [
    {
      name: "bold",
      isActive: (editor) => editor.isActive("bold"),
      command: (editor) => editor.chain().focus().toggleBold().run(),
      icon: BoldIcon,
    },
    {
      name: "italic",
      isActive: (editor) => editor.isActive("italic"),
      command: (editor) => editor.chain().focus().toggleItalic().run(),
      icon: ItalicIcon,
    },
    {
      name: "underline",
      isActive: (editor) => editor.isActive("underline"),
      command: (editor) => editor.chain().focus().toggleUnderline().run(),
      icon: UnderlineIcon,
    },
    {
      name: "strike",
      isActive: (editor) => editor.isActive("strike"),
      command: (editor) => editor.chain().focus().toggleStrike().run(),
      icon: StrikethroughIcon,
    },
    {
      name: "code",
      isActive: (editor) => editor.isActive("code"),
      command: (editor) => editor.chain().focus().toggleCode().run(),
      icon: CodeIcon,
    },
  ];

  return (
    <div className="flex">
      {items.map((item, index) => (
        <EditorBubbleItem
          key={index}
          onSelect={(editor) => {
            item.command(editor);
          }}
        >
          <Button size="icon" className="rounded-none" variant="ghost">
            <item.icon
              className={cn("h-4 w-4", {
                "text-blue-500": item.isActive(editor),
              })}
            />
          </Button>
        </EditorBubbleItem>
      ))}
    </div>
  );
};
```

> Underline is **not** in StarterKit by default — install and add `@tiptap/extension-underline` if you use the underline button.

---

## Color Selector

Two palettes: text color (uses Tiptap's TextStyle/Color extensions) and highlight background (uses the Highlight extension). Highlights consume the `--novel-highlight-*` CSS variables defined in `references/tailwind-setup.md`.

```tsx
// color-selector.tsx
import { Check, ChevronDown } from "lucide-react";
import { EditorBubbleItem, useEditor } from "novel";

import { PopoverTrigger, Popover, PopoverContent } from "@/components/tailwind/ui/popover";
import { Button } from "@/components/tailwind/ui/button";

export interface BubbleColorMenuItem {
  name: string;
  color: string;
}

const TEXT_COLORS: BubbleColorMenuItem[] = [
  { name: "Default", color: "var(--novel-black)" },
  { name: "Purple", color: "#9333EA" },
  { name: "Red", color: "#E00000" },
  { name: "Yellow", color: "#EAB308" },
  { name: "Blue", color: "#2563EB" },
  { name: "Green", color: "#008A00" },
  { name: "Orange", color: "#FFA500" },
  { name: "Pink", color: "#BA4081" },
  { name: "Gray", color: "#A8A29E" },
];

const HIGHLIGHT_COLORS: BubbleColorMenuItem[] = [
  { name: "Default", color: "var(--novel-highlight-default)" },
  { name: "Purple",  color: "var(--novel-highlight-purple)"  },
  { name: "Red",     color: "var(--novel-highlight-red)"     },
  { name: "Yellow",  color: "var(--novel-highlight-yellow)"  },
  { name: "Blue",    color: "var(--novel-highlight-blue)"    },
  { name: "Green",   color: "var(--novel-highlight-green)"   },
  { name: "Orange",  color: "var(--novel-highlight-orange)"  },
  { name: "Pink",    color: "var(--novel-highlight-pink)"    },
  { name: "Gray",    color: "var(--novel-highlight-gray)"    },
];

interface ColorSelectorProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const ColorSelector = ({ open, onOpenChange }: ColorSelectorProps) => {
  const { editor } = useEditor();
  if (!editor) return null;

  const activeColorItem = TEXT_COLORS.find(({ color }) =>
    editor.isActive("textStyle", { color })
  );
  const activeHighlightItem = HIGHLIGHT_COLORS.find(({ color }) =>
    editor.isActive("highlight", { color })
  );

  return (
    <Popover modal={true} open={open} onOpenChange={onOpenChange}>
      <PopoverTrigger asChild>
        <Button className="gap-2 rounded-none" variant="ghost">
          <span
            className="rounded-sm px-1"
            style={{
              color: activeColorItem?.color,
              backgroundColor: activeHighlightItem?.color,
            }}
          >
            A
          </span>
          <ChevronDown className="h-4 w-4" />
        </Button>
      </PopoverTrigger>

      <PopoverContent
        sideOffset={5}
        className="my-1 flex max-h-80 w-48 flex-col overflow-hidden overflow-y-auto rounded border p-1 shadow-xl"
        align="start"
      >
        <div className="flex flex-col">
          <div className="my-1 px-2 text-sm font-semibold text-muted-foreground">Color</div>
          {TEXT_COLORS.map(({ name, color }, index) => (
            <EditorBubbleItem
              key={index}
              onSelect={() => {
                editor.commands.unsetColor();
                name !== "Default" &&
                  editor.chain().focus().setColor(color || "").run();
              }}
              className="flex cursor-pointer items-center justify-between px-2 py-1 text-sm hover:bg-accent"
            >
              <div className="flex items-center gap-2">
                <div className="rounded-sm border px-2 py-px font-medium" style={{ color }}>
                  A
                </div>
                <span>{name}</span>
              </div>
            </EditorBubbleItem>
          ))}
        </div>
        <div>
          <div className="my-1 px-2 text-sm font-semibold text-muted-foreground">Background</div>
          {HIGHLIGHT_COLORS.map(({ name, color }, index) => (
            <EditorBubbleItem
              key={index}
              onSelect={() => {
                editor.commands.unsetHighlight();
                name !== "Default" && editor.commands.setHighlight({ color });
              }}
              className="flex cursor-pointer items-center justify-between px-2 py-1 text-sm hover:bg-accent"
            >
              <div className="flex items-center gap-2">
                <div
                  className="rounded-sm border px-2 py-px font-medium"
                  style={{ backgroundColor: color }}
                >
                  A
                </div>
                <span>{name}</span>
              </div>
              {editor.isActive("highlight", { color }) && <Check className="h-4 w-4" />}
            </EditorBubbleItem>
          ))}
        </div>
      </PopoverContent>
    </Popover>
  );
};
```

> Color and highlight require Tiptap's `@tiptap/extension-text-style`, `@tiptap/extension-color`, and `@tiptap/extension-highlight`. They are *not* shipped in `defaultExtensions` — install and add them yourself.

---

## Why each selector lives in its own popover

Putting `Popover` controls outside the bubble — and giving each selector its own `open` state — lets the user open the Color picker without losing the bubble menu when their selection moves. `EditorBubble` re-renders cheaply when selection changes; the popovers are siblings in the DOM (Radix portals them out) so they don't get unmounted.
