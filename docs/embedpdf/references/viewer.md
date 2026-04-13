# EmbedPDF Viewer Reference

Architectural reference for the drop-in Viewer component (`@embedpdf/react-pdf-viewer`).
For detailed API docs and full type definitions, query Context7 (`/websites/embedpdf`).

---

## 1. Viewer Architecture

The `PDFViewer` component from `@embedpdf/react-pdf-viewer` is a self-contained, production-ready PDF viewer. Single import, single component, configured via the `config` prop. Use a `ref` (type `PDFViewerRef`) for imperative access to the registry, theme control, and icon registration.

Key types:

| Type | Purpose |
|---|---|
| `PDFViewer` | The viewer component |
| `PDFViewerRef` | Ref type -- exposes `registry` (Promise), `setTheme()`, `registerIcon()` |

---

## 2. Config Props Overview

The top-level `config` prop accepts:

| Option | Type | Description |
|---|---|---|
| `src` | `string` | URL or path to PDF |
| `theme` | `object` | Light/dark/custom theme config |
| `tabBar` | `'always' \| 'multiple' \| 'never'` | Tab bar visibility (default: `'multiple'`) |
| `disabledCategories` | `string[]` | Hide specific UI features |
| `i18n` | `object` | Locale and translation config |
| `annotations` | `object` | Annotation defaults (author, tools) |
| `pan` | `object` | Hand tool behavior |
| `zoom` | `object` | Default zoom levels and limits |
| `spread` | `object` | Two-page spread layouts |
| `scroll` | `object` | Scroll direction and logic |
| `documentManager` | `object` | Advanced document loading |
| `permissions` | `object` | Security/permission overrides |

Query Context7 for full prop types and nested config shapes.

---

## 3. Theming System

Theme preference: `'light' | 'dark' | 'system'`

The theme uses **design tokens** organized into categories:

```typescript
type ThemeTokens = {
  accent: {
    primary: string;
    primaryHover: string;
    primaryActive: string;
    primaryLight: string;
    primaryForeground: string;
  };
  background: {
    app: string;
    surface: string;
    surfaceAlt: string;
    elevated: string;
    overlay: string;
    input: string;
  };
  foreground: {
    primary: string;
    secondary: string;
    muted: string;
    disabled: string;
    onAccent: string;
  };
  interactive: {
    hover: string;
    active: string;
    selected: string;
    focus: string;
  };
  border: {
    default: string;
    subtle: string;
    strong: string;
  };
  state: {
    error: string;
    errorLight: string;
    warning: string;
    warningLight: string;
    success: string;
    successLight: string;
    info: string;
    infoLight: string;
  };
};
```

Config shape:

```typescript
theme: {
  preference: 'system',
  light: { accent: {...}, background: {...}, ... },
  dark: { accent: {...}, background: {...}, ... }
}
```

Key behaviors:

- **Deep merge** -- only override tokens you want to change
- **Independent light/dark configs** -- customize each mode separately
- **Automatic OS detection** with `'system'` preference

### Brand Color Example

```typescript
theme: {
  preference: 'system',
  light: {
    accent: {
      primary: '#9333ea',
      primaryHover: '#7e22ce',
      primaryActive: '#6b21a8',
      primaryLight: '#f3e8ff',
      primaryForeground: '#fff'
    }
  },
  dark: {
    accent: {
      primary: '#a855f7',
      primaryHover: '#9333ea',
      primaryActive: '#7e22ce',
      primaryLight: '#581c87',
      primaryForeground: '#fff'
    }
  }
}
```

### External Theme Sync

Use the ref to sync with external theme providers:

```typescript
import { PDFViewer, PDFViewerRef } from '@embedpdf/react-pdf-viewer';
import { useTheme } from 'your-theme-provider';
import { useRef, useEffect } from 'react';

export default function ThemeSync() {
  const { theme } = useTheme();
  const viewerRef = useRef<PDFViewerRef>(null);

  useEffect(() => {
    viewerRef.current?.setTheme(theme);
  }, [theme]);

  return (
    <PDFViewer
      ref={viewerRef}
      config={{ src: '/doc.pdf', theme: { preference: theme } }}
    />
  );
}
```

---

## 4. UI Customization

### Disabling Features with `disabledCategories`

Pass an array of category strings. Disabling a parent cascades to all children.

**Full category hierarchy:**

| Group | Categories |
|---|---|
| Zoom | `zoom`, `zoom-in`, `zoom-out`, `zoom-fit-page`, `zoom-fit-width`, `zoom-marquee`, `zoom-level` |
| Annotation | `annotation`, `annotation-markup`, `annotation-highlight`, `annotation-underline`, `annotation-strikeout`, `annotation-squiggly`, `annotation-ink`, `annotation-text`, `annotation-stamp` |
| Annotation Shapes | `annotation-shape`, `annotation-rectangle`, `annotation-circle`, `annotation-line`, `annotation-arrow`, `annotation-polygon`, `annotation-polyline` |
| Form | `form`, `form-textfield`, `form-checkbox`, `form-radio`, `form-select`, `form-listbox`, `form-fill-mode` |
| Redaction | `redaction`, `redaction-area`, `redaction-text`, `redaction-apply`, `redaction-clear` |
| Document | `document`, `document-open`, `document-close`, `document-print`, `document-capture`, `document-export`, `document-fullscreen`, `document-protect` |
| Page | `page`, `spread`, `rotate`, `scroll`, `navigation` |
| Panel | `panel`, `panel-sidebar`, `panel-search`, `panel-comment` |
| Tools | `tools`, `pan`, `pointer`, `capture` |
| Selection | `selection`, `selection-copy` |
| History | `history`, `history-undo`, `history-redo` |

Example:

```tsx
<PDFViewer config={{ src: '/doc.pdf', disabledCategories: ['annotation', 'print', 'export'] }} />
```

### Registry API -- Custom Commands and Toolbar Modification

Access the internal registry via the ref for advanced customization:

```typescript
const registry = await viewerRef.current?.registry;
const commands = registry.getPlugin('commands').provides();
const ui = registry.getPlugin('ui').provides();
```

**Register a custom command:**

```typescript
commands.registerCommand({
  id: 'custom.hello',
  label: 'Say Hello',
  icon: 'smiley',
  action: () => alert('Hello!')
});
```

**Modify toolbar schema:**

```typescript
const schema = ui.getSchema();
const toolbar = schema.toolbars['main-toolbar'];
const items = JSON.parse(JSON.stringify(toolbar.items));
const rightGroup = items.find(item => item.id === 'right-group');

if (rightGroup) {
  rightGroup.items.push({
    type: 'command-button',
    id: 'custom-button',
    commandId: 'custom.hello',
    variant: 'icon'
  });
}

ui.mergeSchema({
  toolbars: { 'main-toolbar': { ...toolbar, items } }
});
```

**Register custom icons:**

```typescript
viewerRef.current?.registerIcon('smiley', {
  viewBox: '0 0 24 24',
  paths: [
    { d: 'M3 12a9 9 0 1 0 18 0a9 9 0 1 0 -18 0', stroke: 'currentColor', fill: 'none' },
    { d: 'M9.5 15a3.5 3.5 0 0 0 5 0', stroke: 'currentColor', fill: 'none' }
  ]
});
```

**Key registry methods:**

- `registry.getPlugin('commands').provides().registerCommand({id, label, icon, action})`
- `registry.getPlugin('ui').provides().getSchema()`
- `registry.getPlugin('ui').provides().mergeSchema({...})`
- `viewerRef.current?.registerIcon(name, {viewBox, paths})`

---

## 5. Security

Two layers:

1. **Document Encryption** (AES-256/RC4) -- real cryptographic protection
2. **Permission Flags** -- metadata-only, NOT cryptographically enforced

Config:

```typescript
permissions: {
  enforceDocumentPermissions: false, // default: true
  overrides: {
    print: false,
    copyContents: true
  }
}
```

Resolution order: Overrides (highest) -> Enforcement flag -> PDF embedded flags (lowest)

Available permissions: `print`, `printHighQuality`, `modifyContents`, `copyContents`, `modifyAnnotations`, `fillForms`, `extractForAccessibility`, `assembleDocument`

The viewer UI automatically adapts (hides/disables buttons) based on effective permissions.

---

## 6. Engine Access

Use the engine for read-only operations and export outside the plugin system:

```typescript
const registry = await viewerRef.current?.registry;
const engine = registry.getEngine();
const documentManager = registry.getPlugin('document-manager').provides();
const document = documentManager.getActiveDocument();

const metadata = await engine.getMetadata(document).toPromise();
```

Key engine methods (all return Observables -- use `.toPromise()`):

| Method | Purpose |
|---|---|
| `getMetadata(document)` | Title, author, dates |
| `renderPage(document, page, options?)` | Generate page image |
| `getPageText(document, pageIndex)` | Extract text |
| `getPageAnnotations(document, pageIndex)` | Read annotations |
| `saveAsCopy(document)` | Save to buffer |

Rule: Use the engine for read-only/export. Use plugins for anything that affects the UI.

---

## 7. Viewer Plugin Catalog

All 13 viewer plugins:

| Plugin | Config Key | Purpose |
|---|---|---|
| Document Manager | `documentManager` | Multi-doc management, tabs |
| Scrolling | `scroll` | Scroll direction/behavior |
| Zoom | `zoom` | Zoom levels, fit modes |
| Spread Layouts | `spread` | Single/two-page layouts |
| Pan Tool | `pan` | Hand tool panning |
| Annotations | `annotations` | Markup, ink, text, stamps, shapes |
| Forms | -- | Interactive form fields |
| Text Selection | -- | Select and copy text |
| Rotation | -- | Page rotation |
| Printing | -- | Print document |
| Internationalization | `i18n` | Locale/translations |
| Export & Save | -- | Download/export |
| Signatures | -- | Digital signatures |

Plugins with a config key accept configuration through the top-level `config` prop. Plugins without a config key use sensible defaults and are controlled via the registry API or `disabledCategories`.
