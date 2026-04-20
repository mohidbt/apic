# Components API Reference

Source pages:
- <https://novel.mintlify.dev/docs/components/editor-root>
- <https://novel.mintlify.dev/docs/components/editor-content>
- <https://novel.mintlify.dev/docs/components/editor-bubble>
- <https://novel.mintlify.dev/docs/components/editor-bubble-item>
- <https://novel.mintlify.dev/docs/components/editor-command>
- <https://novel.mintlify.dev/docs/components/editor-command-item>
- <https://novel.mintlify.dev/docs/components/utils/use-editor>

> Reminder: the `editor` instance returned anywhere below is a Tiptap `Editor`. For methods like `chain`, `commands`, `isActive`, `getJSON`, `getHTML`, `getAttributes`, `view`, `state`, etc., see the [Tiptap Editor API](https://tiptap.dev/docs/editor/api/editor).

---

## `<EditorRoot>`

Top-level wrapper. Provides the React context the rest of the components and `useEditor` rely on.

```tsx
<EditorRoot>{...}</EditorRoot>
```

| Prop | Type | Required | Notes |
|---|---|---|---|
| `children` | `ReactNode` | yes | Editor content (typically an `<EditorContent>` and your menu components). |

---

## `<EditorContent>`

Wraps Tiptap's `EditorProvider`. Renders the actual contenteditable surface and accepts every Tiptap setting in addition to the props below.

```tsx
<EditorRoot>
  <EditorContent>{children}</EditorContent>
</EditorRoot>
```

| Prop | Type | Required | Notes |
|---|---|---|---|
| `children` | `ReactNode` | yes | Slot for menu components (`EditorBubble`, `EditorCommand`). |
| `extensions` | `Extension[]` | yes | Array of Tiptap extensions. Typically `[...defaultExtensions, slashCommand]`. |
| `initialContent` | `JSONContent` | no | Initial doc as Tiptap JSON. See [Tiptap Output](https://tiptap.dev/docs/editor/guide/output). |
| `onUpdate` | `(props: { editor: Editor; transaction: Transaction; }) => void` | no | Fires on every change — **debounce before persisting**. |
| `onCreate` | `(props: { editor: Editor; }) => void` | no | Fires once on mount. |
| `className` | `string` | no | Class on the parent container. |
| `editorProps` | Tiptap `EditorProps` | no | Forwarded to Tiptap. Wire `handleDOMEvents.keydown = handleCommandNavigation` here for slash-menu arrow keys. Also where you put `handlePaste` / `handleDrop` for image upload, and `attributes.class` for prose styling. |

For all other props, see [Tiptap Settings](https://tiptap.dev/docs/editor/api/editor#settings).

---

## `<EditorBubble>`

Wrapper over Tiptap's [BubbleMenu](https://tiptap.dev/docs/editor/api/extensions/bubble-menu) extension — the floating toolbar that appears when text is selected.

```tsx
<EditorBubble>
  <EditorBubbleItem />
  <EditorBubbleItem />
  <EditorBubbleItem />
</EditorBubble>
```

| Prop | Type | Required | Notes |
|---|---|---|---|
| `children` | `ReactNode` | yes | Bubble items / your custom selectors. |
| `className` | `string` | no | Container class. |
| `tippyOptions` | Tippy `Props` | no | Tippy.js options. Common: `{ placement: "top" }`. |

---

## `<EditorBubbleItem>`

A single item inside an `EditorBubble`. Calls `onSelect` with the editor instance when clicked/activated.

```tsx
<EditorBubbleItem
  key={index}
  onSelect={(editor) => {
    item.command(editor);
  }}>
  ...
</EditorBubbleItem>
```

| Prop | Type | Required | Notes |
|---|---|---|---|
| `children` | `ReactNode` | yes | What to render inside the bubble. |
| `className` | `string` | no | |
| `onSelect` | `(editor: Editor) => void` | no | Fired when the item is selected. |

---

## `<EditorCommand>`

Wrapper for the slash-command palette. Built on [cmdk](https://github.com/pacocoursey/cmdk) — supports its full prop surface.

```tsx
<EditorCommand>
  <EditorCommandItem />
  <EditorCommandItem />
  <EditorCommandItem />
</EditorCommand>
```

| Prop | Type | Required | Notes |
|---|---|---|---|
| `children` | `ReactNode` | yes | Command items / list / empty slots. |
| `className` | `string` | no | |

> Companion components also exported (used in the slash-command guide): `EditorCommandEmpty` (cmdk's `Command.Empty`) and `EditorCommandList` (cmdk's `Command.List`).

---

## `<EditorCommandItem>`

A single command-palette entry. Filtered by cmdk against `value`.

```tsx
<EditorCommandItem
  value={item.title}
  onCommand={(val) => item.command(val)}>
  Do something
</EditorCommandItem>
```

| Prop | Type | Required | Notes |
|---|---|---|---|
| `children` | `ReactNode` | yes | Render the row UI. |
| `value` | `string` | yes | The string cmdk filters/searches against. |
| `onCommand` | `({ editor, range }: { editor: Editor; range: Range }) => void` | yes | Fired when the item is selected. `range` is the slash-trigger range so you can `.deleteRange(range)` before applying your command. |
| `className` | `string` | no | |

---

## `useEditor()` hook

Imperative access to the underlying Tiptap `Editor` from any descendant of `EditorRoot`.

```tsx
import { useEditor } from "novel";

const CustomComponent = () => {
  const { editor } = useEditor();
  if (!editor) return null;
  // editor.chain().focus().toggleBold().run() etc.
};

<EditorRoot>
  <CustomComponent />
</EditorRoot>;
```

| Returned field | Type | Notes |
|---|---|---|
| `editor` | `Editor \| null` | Tiptap editor instance. `null` until the editor mounts. **Always null-check.** |

For the full method/property surface, see the [Tiptap Editor API](https://tiptap.dev/docs/editor/api/editor).

---

## Other exports worth knowing

| Export | From | Purpose |
|---|---|---|
| `EditorInstance` | `novel` | Type alias for the Tiptap `Editor`. Use as the typed argument when destructuring `onUpdate`/debounce callbacks. |
| `defaultEditorProps` | `novel` | Sensible default Tiptap `editorProps`. Spread or augment instead of replacing. |
| `handleCommandNavigation` | `novel/extensions` | Required `keydown` handler so slash-menu arrow keys work. |
| `Command`, `renderItems`, `createSuggestionItems` | `novel/extensions` | Slash-command primitives — see `references/slash-command.md`. |
| `UploadImagesPlugin`, `createImageUpload`, `handleImagePaste`, `handleImageDrop`, `startImageUpload` | `novel/plugins` | Image-upload pipeline — see `references/image-upload.md`. |
