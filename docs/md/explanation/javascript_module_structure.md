# Module Structure

Perspective is designed for flexibility, allowing developers to pick and choose
which modules they need for their specific use case. The main modules are:

- `@perspective-dev/perspective`  
  The data engine library, as both a browser ES6 and Node.js module. Provides a
  WebAssembly, WebWorker (browser) and Process (node.js) runtime.

- `@perspective-dev/perspective-viewer`  
  A user-configurable visualization widget, bundled as a
  [Web Component](https://www.webcomponents.org/introduction). This module
  includes the core data engine module as a dependency.

`<perspective-viewer>` by itself only implements a trivial debug renderer, which
prints the currently configured `view()` as a CSV. Plugin modules for popular
JavaScript libraries, such as [d3fc](https://d3fc.io/), are packaged separately
and must be imported individually.

Perspective offers these plugin modules:

- `@perspective-dev/perspective-viewer-datagrid`  
  A custom high-performance data-grid component based on HTML `<table>`.

- `@perspective-dev/perspective-viewer-d3fc`  
  A `<perspective-viewer>` plugin for the [d3fc](https://d3fc.io) charting
  library.

When imported after `@perspective-dev/perspective-viewer`, the plugin modules
will register themselves automatically, and the renderers they export will be
available in the `plugin` dropdown in the `<perspective-viewer>` UI.

## Which modules should I import?

Depending on your requirements, you may need just one, or all, Perspective
modules. Here are some basic guidelines to help you decide what is most
appropriate for your project:

- For Perspective's high-performance streaming data engine (in WebAssembly), or
  for a purely Node.js based application, import:
    - `@perspective-dev/perspective`, as detailed [here](#perspective-library)

- For Perspective as a simple, browser-based data visualization widget, you will
  need to import:
    - `@perspective-dev/perspective`, detailed [here](#perspective-library)
    - `@perspective-dev/perspective-viewer`, detailed
      [here](#perspective-viewer-web-component)
    - `@perspective-dev/perspective-viewer-datagrid` for data grids
    - `@perspective-dev/perspective-viewer-d3fc` for charting

- For more complex cases, such as
  [sharing tables between viewers](#sharing-a-table-between-multiple-perspective-viewers)
  and
  [binding a viewer to a remote view in Node.js](#remote-perspective-via-workerhost),
  you will likely need all Perspective modules.
