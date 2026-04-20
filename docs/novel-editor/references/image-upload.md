# Image Upload

Source: <https://novel.mintlify.dev/docs/guides/image-upload>

End-to-end image upload involves four pieces:

1. Configure the **image extension** with `UploadImagesPlugin` so the editor inserts a placeholder while the upload is in flight.
2. Build an **`uploadFn`** with `createImageUpload` — pairs your `onUpload` (returns the final URL) with a synchronous `validateFn` (file-type/size guard).
3. Wire the `uploadFn` into the editor's **`handlePaste` and `handleDrop`** props so paste/drag-drop trigger uploads.
4. Add an **"Image" entry to the slash command** that opens a file picker and calls `uploadFn` programmatically.

## 1. Image extension with `UploadImagesPlugin`

```tsx
// extensions.ts
import { UploadImagesPlugin } from "novel/plugins";
import { TiptapImage } from "novel/extensions";
import { cx } from "class-variance-authority";

const tiptapImage = TiptapImage.extend({
  addProseMirrorPlugins() {
    return [
      UploadImagesPlugin({
        imageClass: cx("opacity-40 rounded-lg border border-stone-200"),
      }),
    ];
  },
}).configure({
  allowBase64: true,
  HTMLAttributes: {
    class: cx("rounded-lg border border-muted"),
  },
});

export const defaultExtensions = [
  tiptapImage,
  // other extensions
];
```

| Option | Purpose |
|---|---|
| `imageClass` | Class applied to the **placeholder** image while it's uploading. The official kit uses `opacity-40 rounded-lg border border-stone-200` so it visibly looks like a pending upload. The CSS spinner is provided by `.img-placeholder` in `prosemirror.css`. |
| `allowBase64` | Lets the inserted image accept `data:` URLs (used during the placeholder phase). |
| `HTMLAttributes.class` | Class applied to the **final rendered** image. |

## 2. `uploadFn` with `createImageUpload`

```tsx
// image-upload.ts
import { createImageUpload } from "novel/plugins";
import { toast } from "sonner";

const onUpload = async (file: File) => {
  const promise = fetch("/api/upload", {
    method: "POST",
    headers: {
      "content-type": file?.type || "application/octet-stream",
      "x-vercel-filename": file?.name || "image.png",
    },
    body: file,
  });

  // Must resolve to the final URL string of the uploaded image.
  return promise;
};

export const uploadFn = createImageUpload({
  onUpload,
  validateFn: (file) => {
    if (!file.type.includes("image/")) {
      toast.error("File type not supported.");
      return false;
    } else if (file.size / 1024 / 1024 > 20) {
      toast.error("File size too big (max 20MB).");
      return false;
    }
    return true;
  },
});
```

| Option | Type | Purpose |
|---|---|---|
| `onUpload` | `(file: File) => Promise<string>` | Returns the final image URL. The official example posts the raw bytes to `/api/upload`; your endpoint can do whatever (S3 presign, Vercel Blob, R2, etc.) as long as it resolves with the URL. |
| `validateFn` | `(file: File) => boolean` | Synchronous gate. Returning `false` aborts the upload. The example checks MIME type and a 20 MB max. |

> **Note on the official `onUpload` example:** it returns the bare `fetch` promise, which resolves to a `Response`, not a URL string. In real code you must `await` and return `await res.text()` (or `(await res.json()).url`, etc.) so `uploadFn` receives a URL string.

## 3. Editor-prop event handlers

```tsx
// editor.tsx
import { handleImageDrop, handleImagePaste } from "novel/plugins";
import { uploadFn } from "./image-upload";

<EditorContent
  editorProps={{
    handlePaste: (view, event) => handleImagePaste(view, event, uploadFn),
    handleDrop: (view, event, _slice, moved) =>
      handleImageDrop(view, event, moved, uploadFn),
    // keep your other editorProps (handleDOMEvents, attributes, etc.)
  }}
/>
```

These helpers detect image data in the paste/drop event, insert a placeholder at the drop point, then swap in the real image when `uploadFn` resolves.

## 4. Slash-command "Image" entry

```tsx
import { ImageIcon } from "lucide-react";
import { createSuggestionItems } from "novel/extensions";
import { uploadFn } from "./image-upload";

export const suggestionItems = createSuggestionItems([
  // ...other items
  {
    title: "Image",
    description: "Upload an image from your computer.",
    searchTerms: ["photo", "picture", "media"],
    icon: <ImageIcon size={18} />,
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).run();
      // Trigger a hidden file picker
      const input = document.createElement("input");
      input.type = "file";
      input.accept = "image/*";
      input.onchange = async () => {
        if (input.files?.length) {
          const file = input.files[0];
          const pos = editor.view.state.selection.from;
          uploadFn(file, editor.view, pos);
        }
      };
      input.click();
    },
  },
]);
```

`uploadFn(file, view, pos)` is the signature `createImageUpload` returns: file + ProseMirror view + insert position. The placeholder is inserted at `pos`, then replaced when the URL resolves.

## Placeholder visuals

The animated spinner around the placeholder image is purely CSS — comes from the `.img-placeholder` rules already in `prosemirror.css` (see `references/tailwind-setup.md`). No JS needed.

## Common failure modes

| Symptom | Fix |
|---|---|
| Image appears, then never resolves to the real URL | `onUpload` returned a `Response`, not a URL string. Return `await res.text()` (or `(await res.json()).url`). |
| Drag/drop does nothing | `handleDrop` not wired into `editorProps`, or another `handleDrop` returned `true` first. |
| Paste of large image freezes | Add a stricter `validateFn` size check, or compress on the client before calling `onUpload`. |
| Spinner CSS missing | `.img-placeholder` rule from `prosemirror.css` not included. |
| Base64 paste shows but doesn't upload | `handleImagePaste` only fires when the clipboard has a real `File` — pasting a `<img src="data:...">` HTML snippet doesn't trigger it. |
