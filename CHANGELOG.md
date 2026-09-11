# Changelog

All notable URMPlus changes are recorded here. Release archives use the
`0x52_URM.patched-vN.rpa` naming convention.

## [v28] - 2026-09-11

### Fixed

- Restored double-click navigation: the first click selects a node, and a
  second click on that same node within the native double-click interval uses
  Ren'Py's `renpy.jump()` to navigate directly to the label.
- Added implicit fall-through edges between sequential compiled labels, in
  addition to explicit `jump` and `call` links.
- Removed the arbitrary nested-AST depth cutoff so deeply nested in-label
  conditionals are included in the branch.
- Uses the complete indexed label set when resolving links, avoiding missed
  edges caused by repeated runtime label checks.

### Performance

- Full label/AST and flow discovery remains incremental and timer-driven in the
  background; complete branch expansion is cached after the index is ready.

## [v27] - 2026-09-11

### Changed

- View-filter defaults now show the complete current label flow with only
  **Current branch** enabled. **Searched branches** starts disabled and can be
  enabled when search-driven flow context is needed.
- Branch filtering now retains the complete connected label flow for each
  active current/search anchor instead of only the anchor and one adjacent
  level.
- All Label Tree search and view-filter checkboxes are remembered in
  Ren'Py persistent data and restored when the overlay is reopened or the game
  is restarted.

### Compatibility

- Persistent settings are stored under a mod-specific attribute and saved via
  Ren'Py's `renpy.save_persistent()` API; no game-defined variables are used.

## [v26] - 2026-09-11

### Fixed

- Kept the View Filter control inside the graph column so it cannot cover or
  push the search-results pane off-screen.
- Reserved the overlay's left tab rail before calculating graph and results
  widths.
- Tracked the active game label through Ren'Py's current context and a bounded
  rollback-log fallback during save/load transitions.
- Ignored Ren'Py helper labels (`save_screen`, `load_screen`, `after_load`, and
  related internal helpers) when choosing the label shown as current.

### Performance

- Cached statement-to-label ownership while building the AST index.
- Avoided repeated label-existence queries during every screen interaction.
- Kept current-label resolution bounded and cached by runtime state.

## [v25] - 2026-09-11

### Added

- View Filter menu with **Searched branches** and **Current branch** toggles.

### Fixed

- Reworked graph/results sizing so the results pane remains a sibling of the
  graph viewport instead of being consumed by an expanding container.

## [v24] - 2026-09-11

### Added

- Search preview pane with all matching labels, wrapped long names, detail
  counts, and Previous/Next navigation.
- Collapsible search results and viewport panning/zooming controls.
- Current, selected, and search-result visual states with path highlighting.
- Center Current and Center Selected actions.

### Fixed

- Deferred screen registration for Ren'Py 7.4 so `use` does not run before the
  dynamically loaded Label Tree screen is known.
- Replaced unsupported or unsafe screen/Python patterns found during runtime
  testing.

## [v1] - 2026-09-11

### Added

- Initial performant Label Tree implementation.
- Incremental label/AST discovery, cached search indexing, and deferred build
  work for large Ren'Py games.
- Ren'Py 7.4/Python 2.7-compatible screen and Python code.
- Local RPA extraction and packing tools for nondestructive iteration.

## Versioning notes

- `v26` refers to the tested archive build, not a change to the base game's
  version number.
- The original URM archive is retained under `original/` as a recovery and
  comparison reference.
