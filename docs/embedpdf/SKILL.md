---
name: embedpdf
description: "Build PDF viewing experiences with @embedpdf/react-pdf-viewer. Use this skill whenever the user mentions PDF viewing, PDF rendering, PDF reader, PDF annotations, PDF forms, PDF viewer component, embedpdf, or building any kind of PDF experience in React/Next.js/Vue/Svelte. Covers both the ready-made Viewer and the headless component library. Always use alongside Context7 for detailed API reference."
---

# EmbedPDF Skill

## Context7 — Always Query for Implementation Details

For detailed API docs, props, configuration options, and code examples, ALWAYS query Context7 with the library ID below. This skill provides architectural understanding and decision guidance. Context7 provides the up-to-date implementation details, prop signatures, and configuration reference.

```
Context7 Library ID: /websites/embedpdf
```

Do not rely solely on this skill file for API specifics. Query Context7 before writing any EmbedPDF integration code.

---

## What is EmbedPDF

EmbedPDF is an open-source, framework-agnostic PDF viewer powered by PDFium compiled to WebAssembly. It provides a two-tier architecture:

- **Drop-in Viewer** (`@embedpdf/react-pdf-viewer`): A production-ready UI that drops into your app in seconds. Includes a polished toolbar, sidebar, thumbnails, and everything needed for a complete PDF viewing experience out of the box.
- **Headless Library** (`@embedpdf/core` + plugins): An unopinionated UI toolkit providing logic and rendering primitives with zero styling. Gives you 100% UI control with a tree-shakeable architecture.

EmbedPDF supports React, Vue 3, and Svelte. MIT licensed.

---

## Key Architectural Rules

- Client-side only -- no server required. Uses Canvas + WebAssembly for rendering.
- In Next.js App Router, components MUST use the `'use client'` directive.
- The PDFium engine is **stateless** -- direct engine operations do not update UI or plugin state. Always use plugins for any UI-affecting operations.
- All features are delivered as plugins -- modular, composable architecture throughout.
- The engine runs in a Web Worker by default for performance.

---

## Decision Guide: Viewer vs Headless

| Aspect | Drop-in Viewer | Headless |
|---|---|---|
| Package | `@embedpdf/react-pdf-viewer` | `@embedpdf/core` + individual plugins |
| Setup time | Minutes | Hours |
| Customization | Theme tokens + disabledCategories + toolbar schema | 100% UI control |
| Bundle size | Larger (all-in-one) | Minimal (tree-shakeable) |
| Use case | Standard PDF viewing, quick integration | Custom design systems, unique PDF experiences |
| Styling | Themed, configurable | Zero styling included |

**Decision heuristic:**

- Use **Viewer** when: you want a working PDF viewer fast, standard UI is acceptable, and theming provides sufficient customization.
- Use **Headless** when: you need a fully custom UI, you are building into a design system, you need to minimize bundle size, or you need control over every pixel.

---

## Viewer Quick Start

Install:

```bash
npm install @embedpdf/react-pdf-viewer
```

Basic usage:

```tsx
import { PDFViewer } from '@embedpdf/react-pdf-viewer';

export default function App() {
  return (
    <div style={{ height: '100vh' }}>
      <PDFViewer
        config={{
          src: 'https://snippet.embedpdf.com/ebook.pdf',
          theme: { preference: 'light' }
        }}
      />
    </div>
  );
}
```

Next.js App Router pattern:

```tsx
'use client';
import { PDFViewer } from '@embedpdf/react-pdf-viewer';

export default function ViewerPage() {
  return (
    <div style={{ height: '100vh' }}>
      <PDFViewer config={{ src: '/document.pdf' }} />
    </div>
  );
}
```

---

## Headless Quick Start

Install all required packages:

```bash
npm install @embedpdf/core @embedpdf/engines @embedpdf/plugin-document-manager @embedpdf/plugin-viewport @embedpdf/plugin-scroll @embedpdf/plugin-render
```

Minimal 4-plugin setup:

```tsx
import { usePdfiumEngine } from '@embedpdf/engines/react';
import { EmbedPDF, DocumentContent } from '@embedpdf/core/react';
import { createPluginRegistration } from '@embedpdf/core';
import { DocumentManagerPluginPackage } from '@embedpdf/plugin-document-manager';
import { ViewportPluginPackage, Viewport } from '@embedpdf/plugin-viewport';
import { ScrollPluginPackage, Scroller } from '@embedpdf/plugin-scroll';
import { RenderPluginPackage, RenderLayer } from '@embedpdf/plugin-render';

const plugins = [
  createPluginRegistration(DocumentManagerPluginPackage, {
    initialDocuments: [{ url: '/document.pdf' }]
  }),
  createPluginRegistration(ViewportPluginPackage, {}),
  createPluginRegistration(ScrollPluginPackage, {}),
  createPluginRegistration(RenderPluginPackage),
];

export default function CustomViewer() {
  const { engine, isLoading, error } = usePdfiumEngine();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <EmbedPDF engine={engine} plugins={plugins}>
      {({ activeDocumentId }) =>
        activeDocumentId && (
          <DocumentContent documentId={activeDocumentId}>
            {({ isLoaded }) =>
              isLoaded && (
                <Viewport documentId={activeDocumentId} style={{ height: '100vh' }}>
                  <Scroller
                    documentId={activeDocumentId}
                    renderPage={({ pageIndex }) => (
                      <RenderLayer documentId={activeDocumentId} pageIndex={pageIndex} />
                    )}
                  />
                </Viewport>
              )
            }
          </DocumentContent>
        )
      }
    </EmbedPDF>
  );
}
```

---

## Plugin System Overview

Both the Viewer and Headless tiers use a plugin architecture. All features are modular and composable.

### Viewer Plugins

These are built into the Viewer and configured via the `config` prop:

| Plugin | Purpose |
|---|---|
| Document Manager | Multi-document management, tab bar |
| Scrolling | Scroll direction and behavior |
| Zoom | Zoom levels, fit-to-page/width, marquee zoom |
| Spread Layouts | Single page, two-page spreads |
| Pan Tool | Hand tool for panning |
| Annotations | Markup, ink, text, stamps, shapes |
| Forms | Interactive PDF form fields |
| Text Selection | Text selection and copy |
| Rotation | Page rotation |
| Printing | Document printing |
| Internationalization | Locale and translations |
| Export & Save | Download, save as copy |
| Signatures | Digital signature fields |

### Headless Plugins

Individually installed as `@embedpdf/plugin-*` packages:

| Plugin | Package | Purpose |
|---|---|---|
| Document Manager | `@embedpdf/plugin-document-manager` | Document lifecycle |
| Viewport | `@embedpdf/plugin-viewport` | Scrollable container |
| Scroll | `@embedpdf/plugin-scroll` | Page layout/virtualization |
| Render | `@embedpdf/plugin-render` | Content rasterization |
| Tiling | `@embedpdf/plugin-tiling` | Tile-based rendering |
| Thumbnail | `@embedpdf/plugin-thumbnail` | Page thumbnails |
| Annotation | `@embedpdf/plugin-annotation` | Annotations |
| Form | `@embedpdf/plugin-form` | PDF forms |
| Stamp | `@embedpdf/plugin-stamp` | Stamp annotations |
| Selection | `@embedpdf/plugin-selection` | Text selection |
| Zoom | `@embedpdf/plugin-zoom` | Zoom control |
| Rotate | `@embedpdf/plugin-rotate` | Page rotation |
| Print | `@embedpdf/plugin-print` | Printing |
| Export | `@embedpdf/plugin-export` | Document export |
| Signature | `@embedpdf/plugin-signature` | Digital signatures |
| Spread | `@embedpdf/plugin-spread` | Multi-page layouts |
| Pan | `@embedpdf/plugin-pan` | Hand tool |
| Capture | `@embedpdf/plugin-capture` | Screenshot/capture |
| Redaction | `@embedpdf/plugin-redaction` | Content redaction |
| Internationalization | `@embedpdf/plugin-i18n` | Localization |
| View Manager | `@embedpdf/plugin-view-manager` | View state management |
| Commands | `@embedpdf/plugin-commands` | Command registry |
| Layout Analysis | `@embedpdf/plugin-layout-analysis` | ONNX-powered layout |
| Search | `@embedpdf/plugin-search` | Text search |
| Interaction Manager | `@embedpdf/plugin-interaction-manager` | Input coordination |
| Fullscreen | `@embedpdf/plugin-fullscreen` | Fullscreen mode |

---

## Security Model

EmbedPDF provides two layers of document security:

1. **Document Encryption** (AES-256/RC4) -- Real cryptographic protection with user/owner passwords. This is enforced by the engine.
2. **Permission Flags** -- Metadata-only hints that are not cryptographically enforced. These are a "polite request" to compliant viewers and can be bypassed by any tool that ignores them.

Both Viewer and Headless support permission overrides for the following flags:

- `print`
- `printHighQuality`
- `modifyContents`
- `copyContents`
- `modifyAnnotations`
- `fillForms`
- `extractForAccessibility`
- `assembleDocument`

Query Context7 and consult the reference files for implementation details on encryption and permission handling.

---

## Reference Files

When working on EmbedPDF integrations, consult these additional reference files for detailed guidance:

- Read `references/viewer.md` when working with the drop-in `PDFViewer` component -- covers theming, UI customization, registry API, toolbar modification, and engine access.
- Read `references/headless.md` when building custom PDF UI with headless components -- covers component hierarchy, plugin registration, hooks, engine setup, and the full plugin import map.

Always pair these references with a Context7 query for the most current API details.
