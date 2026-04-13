# EmbedPDF Headless Library

> For detailed API documentation, query Context7 (`/websites/embedpdf`).

## Headless Architecture

EmbedPDF Headless provides logic and rendering primitives with **zero styling**. Developers get 100% UI control while the library handles all PDF logic. The library is fully tree-shakeable -- import only the plugins you need.

Core philosophy: Unlike the drop-in Viewer that gives you a complete UI, Headless gives you building blocks. Compose them into your own UI using your own design system.

## Package Ecosystem

| Package | Exports | Purpose |
|---|---|---|
| `@embedpdf/core` | Core framework | Plugin system, types |
| `@embedpdf/core/react` | `EmbedPDF`, `DocumentContent`, `createPluginRegistration`, `useDocumentPermissions` | React integration |
| `@embedpdf/engines` | Engine implementations | PDFium WASM |
| `@embedpdf/engines/react` | `usePdfiumEngine`, `PdfEngineProvider`, `useEngineContext`, `useEngine` | React engine hooks |
| `@embedpdf/plugin-document-manager` | `DocumentManagerPluginPackage` | Document lifecycle |
| `@embedpdf/plugin-viewport` | `ViewportPluginPackage`, `Viewport` | Scrollable container |
| `@embedpdf/plugin-scroll` | `ScrollPluginPackage`, `Scroller` | Virtualization/layout |
| `@embedpdf/plugin-render` | `RenderPluginPackage`, `RenderLayer` | Content rasterization |

Each plugin also exports a React hook from its `/react` subpath: `import { use<Plugin> } from '@embedpdf/plugin-<name>/react'`

## Component Hierarchy

The headless library has a strict component nesting order:

```
EmbedPDF (provider -- accepts engine + plugins)
  └── DocumentContent (loading gate -- accepts documentId)
       └── Viewport (scrollable container -- accepts documentId)
            └── Scroller (page layout/virtualization -- accepts documentId + renderPage)
                 └── RenderLayer (PDF rasterization -- accepts documentId + pageIndex)
```

**`<EmbedPDF>`** -- Top-level provider. Uses render-prop pattern.
- Props: `engine` (from `usePdfiumEngine`), `plugins` (array of `createPluginRegistration` calls)
- Render prop provides: `{ activeDocumentId }`

**`<DocumentContent>`** -- Guards rendering until document is loaded.
- Props: `documentId` (required)
- Render prop provides: `{ isLoaded }`

**`<Viewport>`** -- Scrollable container for the PDF.
- Props: `documentId` (required), `style` (optional CSS)

**`<Scroller>`** -- Handles page layout and virtualization.
- Props: `documentId` (required), `renderPage` callback
- `renderPage` receives: `{ width, height, pageIndex }`

**`<RenderLayer>`** -- Rasterizes actual PDF content onto canvas.
- Props: `documentId` (required), `pageIndex` (required)

## Plugin Registration Pattern

All plugins are registered using the factory pattern:

```typescript
import { createPluginRegistration } from '@embedpdf/core';
import { DocumentManagerPluginPackage } from '@embedpdf/plugin-document-manager';

const plugins = [
  createPluginRegistration(DocumentManagerPluginPackage, {
    initialDocuments: [{ url: '/document.pdf' }]
  }),
  createPluginRegistration(ViewportPluginPackage, {}),
  createPluginRegistration(ScrollPluginPackage, {}),
  createPluginRegistration(RenderPluginPackage),
];
```

Pattern: `createPluginRegistration(PluginPackage, config?)` -- config is plugin-specific, some plugins need no config.

Pass plugins as an array to `<EmbedPDF engine={engine} plugins={plugins}>`.

## Hook Pattern

Each plugin exposes a React hook that returns a `provides` object (the plugin's API) and state values.

Pattern: `use<Plugin>(documentId)` returns `{ provides, ...state }`

```typescript
import { usePan } from '@embedpdf/plugin-pan/react';
import { useRotate } from '@embedpdf/plugin-rotate/react';
import { useSpread } from '@embedpdf/plugin-spread/react';
import { useZoom } from '@embedpdf/plugin-zoom/react';

function Toolbar({ documentId }) {
  const { provides: panProvider, isPanning } = usePan(documentId);
  const { provides: rotateProvider } = useRotate(documentId);
  const { spreadMode, provides: spreadProvider } = useSpread(documentId);

  return (
    <div>
      <button onClick={() => panProvider?.togglePan()}>
        {isPanning ? 'Panning' : 'Pan'}
      </button>
      <button onClick={() => rotateProvider?.rotate(90)}>Rotate</button>
    </div>
  );
}
```

Key pattern: `provides` is the method API object. State properties like `isPanning`, `spreadMode` are reactive.

## Engine Setup

Two patterns for engine initialization:

**Direct usage (single component):**

```typescript
import { usePdfiumEngine } from '@embedpdf/engines/react';

function MyViewer() {
  const { engine, isLoading, error } = usePdfiumEngine();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return <EmbedPDF engine={engine} plugins={plugins}>{/* ... */}</EmbedPDF>;
}
```

**Provider pattern (multi-component sharing):**

```typescript
import { PdfEngineProvider, useEngine } from '@embedpdf/engines/react';

function App() {
  const { engine, isLoading, error } = usePdfiumEngine();
  return (
    <PdfEngineProvider engine={engine} isLoading={isLoading} error={error}>
      <ViewerComponent />
    </PdfEngineProvider>
  );
}

function ViewerComponent() {
  const engine = useEngine(); // throws on error
  return <EmbedPDF engine={engine} plugins={plugins}>{/* ... */}</EmbedPDF>;
}
```

`usePdfiumEngine` options:

| Option | Type | Default | Purpose |
|---|---|---|---|
| `wasmUrl` | string | CDN URL | Custom WASM file location |
| `worker` | boolean | `true` | Run in Web Worker |
| `logger` | Logger | undefined | Custom logging |

Critical rule: The engine is **stateless**. Direct engine operations do not update UI or plugin state. Always use plugin hooks for UI-affecting operations.

## Security

Same two-layer model as Viewer, but configured differently in headless.

**Global config:**

```typescript
const config = {
  permissions: {
    enforceDocumentPermissions: false,
    overrides: { print: false, modifyContents: false }
  }
};

<EmbedPDF engine={engine} config={config} plugins={plugins}>{/* ... */}</EmbedPDF>
```

**Per-document override:**

```typescript
createPluginRegistration(DocumentManagerPluginPackage, {
  initialDocuments: [{
    url: '/confidential.pdf',
    permissions: { overrides: { print: true } }
  }]
})
```

Resolution order: Per-Document Override (highest) -> Global Config -> `enforceDocumentPermissions` -> PDF flags (lowest)

**Permission hook:**

```typescript
import { useDocumentPermissions } from '@embedpdf/core/react';

function PrintButton({ documentId }) {
  const { canPrint } = useDocumentPermissions(documentId);
  return <button disabled={!canPrint}>Print</button>;
}
```

## Full Plugin Catalog

| Plugin | Package | Hook | Purpose |
|---|---|---|---|
| Document Manager | `@embedpdf/plugin-document-manager` | -- | Document lifecycle, multi-doc |
| Viewport | `@embedpdf/plugin-viewport` | -- | Scrollable container |
| Scroll | `@embedpdf/plugin-scroll` | -- | Page layout, virtualization |
| Render | `@embedpdf/plugin-render` | -- | Content rasterization |
| Tiling | `@embedpdf/plugin-tiling` | -- | Tile-based rendering |
| Thumbnail | `@embedpdf/plugin-thumbnail` | `useThumbnail` | Page thumbnails |
| Annotation | `@embedpdf/plugin-annotation` | `useAnnotation` | Annotations |
| Form | `@embedpdf/plugin-form` | `useForm` | PDF form fields |
| Stamp | `@embedpdf/plugin-stamp` | `useStamp` | Stamp annotations |
| Selection | `@embedpdf/plugin-selection` | `useSelection` | Text selection |
| Zoom | `@embedpdf/plugin-zoom` | `useZoom` | Zoom control |
| Rotate | `@embedpdf/plugin-rotate` | `useRotate` | Page rotation |
| Print | `@embedpdf/plugin-print` | `usePrint` | Printing |
| Export | `@embedpdf/plugin-export` | `useExport` | Document export |
| Signature | `@embedpdf/plugin-signature` | `useSignature` | Digital signatures |
| Spread | `@embedpdf/plugin-spread` | `useSpread` | Multi-page layouts |
| Pan | `@embedpdf/plugin-pan` | `usePan` | Hand tool |
| Capture | `@embedpdf/plugin-capture` | `useCapture` | Screenshot/capture |
| Redaction | `@embedpdf/plugin-redaction` | `useRedaction` | Content redaction |
| Internationalization | `@embedpdf/plugin-i18n` | -- | Localization |
| View Manager | `@embedpdf/plugin-view-manager` | `useViewManager` | View state |
| Commands | `@embedpdf/plugin-commands` | `useCommands` | Command registry |
| Layout Analysis | `@embedpdf/plugin-layout-analysis` | -- | ONNX-powered layout detection |
| Search | `@embedpdf/plugin-search` | `useSearch` | Text search |
| Interaction Manager | `@embedpdf/plugin-interaction-manager` | -- | Input coordination |
| Fullscreen | `@embedpdf/plugin-fullscreen` | `useFullscreen` | Fullscreen mode |

Hook imports follow the pattern `import { use<Name> } from '@embedpdf/plugin-<name>/react'`. Core infrastructure plugins (Document Manager, Viewport, Scroll, Render, Tiling, I18n, Interaction Manager, Layout Analysis) typically do not expose user-facing hooks -- they work through the component hierarchy.

## Data Flow Architecture

```
usePdfiumEngine() -> engine instance
  -> createPluginRegistration() calls -> plugins array
    -> <EmbedPDF engine={engine} plugins={plugins}> provider
      -> activeDocumentId from render prop
        -> <DocumentContent documentId={id}> loading gate
          -> <Viewport> scrollable area
            -> <Scroller> virtualized pages
              -> <RenderLayer> canvas rendering
```

All plugins consume `documentId` and coordinate through the shared engine instance managed by `<EmbedPDF>`.
