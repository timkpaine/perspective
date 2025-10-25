# JavaScript NPM Installation

Perspective releases contain several different builds for use in most
environments.

## Browser

Perspective's WebAssembly data engine is available via NPM in the same package
as its Node.js counterpart, `@perspective-dev/perspective`. The Perspective
Viewer UI (which has no Node.js component) must be installed separately:

```bash
$ npm add @perspective-dev/perspective @perspective-dev/perspective-viewer
```

By itself, `@perspective-dev/perspective-viewer` does not provide any
visualizations, only the UI framework. Perspective _Plugins_ provide
visualizations and must be installed separately. All Plugins are optional - but
a `<perspective-viewer>` without Plugins would be rather boring!

```bash
$ npm add @perspective-dev/perspective-viewer-d3fc @perspective-dev/perspective-viewer-datagrid @perspective-dev/perspective-viewer-openlayers
```

## Node.js

To use Perspective from a Node.js server, simply install via NPM.

```bash
$ npm add @perspective-dev/perspective
```
