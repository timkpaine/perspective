<br />
<a href="https://perspective-dev.github.io">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://github.com/perspective-dev/perspective/raw/master/docs/static/svg/perspective-logo-dark.svg?raw=true">
<img width="260" src="https://github.com/perspective-dev/perspective/raw/master/docs/static/svg/perspective-logo-light.svg?raw=true">
</picture>
</a>
<br/><br/>

[![Build Status](https://img.shields.io/github/actions/workflow/status/perspective-dev/perspective/build.yaml?event=push&style=for-the-badge)](https://github.com/perspective-dev/perspective/actions/workflows/build.yaml)
[![npm](https://img.shields.io/npm/v/@perspective-dev/client.svg?style=for-the-badge)](https://www.npmjs.com/package/@perspective-dev/client)
[![PyPI](https://img.shields.io/pypi/v/perspective-python.svg?style=for-the-badge)](https://pypi.python.org/pypi/perspective-python)
[![crates.io](https://img.shields.io/crates/v/perspective?style=for-the-badge)](https://crates.io/crates/perspective)

<br/>

Perspective is an <i>interactive</i> analytics and data visualization component,
which is especially well-suited for <i>large</i> and/or <i>streaming</i>
datasets. Use it to create user-configurable reports, dashboards, notebooks and
applications.

### Features

- A fast, memory efficient streaming query engine, written in C++ and compiled
  for [WebAssembly](https://webassembly.org/), [Python](https://www.python.org/)
  and [Rust](https://www.rust-lang.org/), with read/write/streaming for
  [Apache Arrow](https://arrow.apache.org/), and a high-performance columnar
  expression language based on [ExprTK](https://github.com/ArashPartow/exprtk).

- A framework-agnostic User Interface packaged as a
  [Custom Element](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements),
  powered either in-browser via WebAssembly or virtually via WebSocket server
  (Python/Node/Rust).

- A [JupyterLab](https://jupyter.org/) widget and Python client library, for
  interactive data analysis in a notebook, as well as _scalable_ production
  applications.

### Documentation

- [Project Site](https://perspective-dev.github.io/)
- [User Guide](https://perspective-dev.github.io/guide/)
- Python API
    - [`perspective`](https://perspective-dev.github.io/python/index.html)
    - [`perspective.widget`](https://perspective-dev.github.io/python/perspective/widget.html)
    - [`perspective.handlers.aiohttp`](https://perspective-dev.github.io/python/perspective/handlers/aiohttp.htm)
    - [`perspective.handlers.starlette`](https://perspective-dev.github.io/python/perspective/handlers/starlett.htm)
    - [`perspective.handlers.tornado`](https://perspective-dev.github.io/python/perspective/handlers/tornado.htm)
- JavaScript API
    - [`@perspective-dev/client` Browser](https://perspective-dev.github.io/browser/modules/src_ts_perspective.browser.ts.html)
    - [`@perspective-dev/client` Node.js](https://perspective-dev.github.io/node/modules/src_ts_perspective.node.ts.html)
    - [`@perspective-dev/viewer`](https://perspective-dev.github.io/viewer/modules/perspective-viewer.html)
    - [`@perspective-dev/react`](https://perspective-dev.github.io/react/index.html)
- Rust API
    - [`perspective`](https://docs.rs/perspective/latest/perspective/)
    - [`perspective-client`](https://docs.rs/perspective-client/latest/perspective_client/)
    - [`perspective-server`](https://docs.rs/perspective-server/latest/perspective_server/)
    - [`perspective-python`](https://docs.rs/perspective-python/latest/perspective_python/)
    - [`perspective-js`](https://docs.rs/perspective-js/latest/perspective_js/)
    - [`perspective-viewer`](https://docs.rs/perspective-viewer/latest/perspective_viewer/)

### Examples

<!-- Examples -->
<table><tbody><tr><td>editable</td><td>file</td><td>fractal</td></tr><tr><td><a href="https://perspective-dev.github.io/block?example=editable"><img height="125" src="https://perspective-dev.github.io/blocks/editable/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=file"><img height="125" src="https://perspective-dev.github.io/blocks/file/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=fractal"><img height="125" src="https://perspective-dev.github.io/blocks/fractal/preview.png?"></img></a></td></tr><tr><td>market</td><td>raycasting</td><td>evictions</td></tr><tr><td><a href="https://perspective-dev.github.io/block?example=market"><img height="125" src="https://perspective-dev.github.io/blocks/market/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=raycasting"><img height="125" src="https://perspective-dev.github.io/blocks/raycasting/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=evictions"><img height="125" src="https://perspective-dev.github.io/blocks/evictions/preview.png?"></img></a></td></tr><tr><td>nypd</td><td>streaming</td><td>covid</td></tr><tr><td><a href="https://perspective-dev.github.io/block?example=nypd"><img height="125" src="https://perspective-dev.github.io/blocks/nypd/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=streaming"><img height="125" src="https://perspective-dev.github.io/blocks/streaming/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=covid"><img height="125" src="https://perspective-dev.github.io/blocks/covid/preview.png?"></img></a></td></tr><tr><td>webcam</td><td>movies</td><td>superstore</td></tr><tr><td><a href="https://perspective-dev.github.io/block?example=webcam"><img height="125" src="https://perspective-dev.github.io/blocks/webcam/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=movies"><img height="125" src="https://perspective-dev.github.io/blocks/movies/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=superstore"><img height="125" src="https://perspective-dev.github.io/blocks/superstore/preview.png?"></img></a></td></tr><tr><td>citibike</td><td>olympics</td><td>dataset</td></tr><tr><td><a href="https://perspective-dev.github.io/block?example=citibike"><img height="125" src="https://perspective-dev.github.io/blocks/citibike/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=olympics"><img height="125" src="https://perspective-dev.github.io/blocks/olympics/preview.png?"></img></a></td><td><a href="https://perspective-dev.github.io/block?example=dataset"><img height="125" src="https://perspective-dev.github.io/blocks/dataset/preview.png?"></img></a></td></tr></tbody></table>
<!-- Examples -->

### Media

<table><tbody>
<tr>
<td><a href="https://github.com/timkpaine"><code>@timkpaine</code></a></td>
<td><a href="https://github.com/timbess"><code>@timbess</code></a></td>
<td><a href="https://github.com/sc1f"><code>@sc1f</code></a></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=v5Y5ftlGNhU"><img width="240" src="https://img.youtube.com/vi/v5Y5ftlGNhU/0.jpg" /></a></td>
<td><a href="https://www.youtube.com/watch?v=lDpIu4dnp78"><img width="240" src="https://img.youtube.com/vi/lDpIu4dnp78/0.jpg" /></a></td>
<td><a href="https://www.youtube.com/watch?v=IO-HJsGdleE"><img width="240"  src="https://img.youtube.com/vi/IO-HJsGdleE/0.jpg" /></a></td>
</tr>
<tr>
<td><a href="https://github.com/texodus"><code>@texodus</code></a></td>
<td><a href="https://github.com/texodus"><code>@texodus</code></a></td>
<td></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=no0qChjvdgQ"><img width="240" src="https://img.youtube.com/vi/no0qChjvdgQ/0.jpg" /></a></td>
<td><a href="https://www.youtube.com/watch?v=0ut-ynvBpGI"><img width="240" src="https://img.youtube.com/vi/0ut-ynvBpGI/0.jpg" /></a></td>
<td></td>
</tr>
</tbody></table>
