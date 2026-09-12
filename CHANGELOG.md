# Changelog

## [v49] - 2026-09-11

### Fixed

- Search results now use their own Ren'Py viewport adjustment and persist its
  vertical scroll offset independently from the graph canvas. The results
  sidebar restores its position when Label Tree is reopened, including saved
  search sessions from earlier releases.

## [v48] - 2026-09-11

### Fixed

- Multi-term searches now require every term to occur in the same enabled
  field. For example, `nurse replay` matches `replay_nurse`, but does not
  match a label whose second term appears only in unrelated node details.
- Label Tree reapplies the saved horizontal and vertical viewport offsets
  every time the screen is reopened, not only the first time it is shown.

## [v47] - 2026-09-11

### Fixed

- Removed the remaining build-time sensitivity gate from the Label Tree
  search input. Queries can now be entered and label-name results displayed
  immediately while the detailed AST graph continues to build in the
  background.

## [v46] - 2026-09-11

### Fixed

- Label Tree search now indexes the complete Ren'Py label-name list
  immediately, so label results and previews are available while the detailed
  AST graph continues building in the background. Variable, condition, link,
  and statement matches are refreshed when the full graph is ready.
- Branch confirmation no longer writes arbitrary dotted object attributes.
  Only simple scalar variables in the store or persistent store can be
  changed generically; this prevents a cross-game tool from replacing custom
  quest objects or engine-managed state that later script code expects to be
  a collection or object.
- Diagnosed the reported `q_nurse_roped.rpy` failure as base-game code calling
  `.add("kate")` on `quest.nurse_roped["exhibition_attractions"]` while that
  value is an integer. Label Tree now avoids the unsafe generic mutation path
  that can cause this class of state corruption.

## [v45] - 2026-09-11

### Fixed

- Added a transparent Ren'Py event sink behind the URM window so clicks in
  empty Label Tree viewport space cannot activate the game underneath.
- Label Tree search persistence now also stores and restores the graph's
  horizontal and vertical viewport positions.
- Viewport persistence is sampled during normal Ren'Py interactions and saved
  with the existing debounced search-state persistence, avoiding private
  engine callbacks and keeping mouse-wheel/drag navigation responsive.

## [v44] - 2026-09-11

### Fixed

- Confirmation now preserves each variable's live value instead of selecting
  the first observed branch option by default.
- Done without a dropdown change no longer writes game variables.
- Dropdown values must remain compatible with the variable's existing scalar
  type, preventing day counters from becoming unicode and state collections
  from being replaced with numeric values.
- Confirmation skips a variable if the game changed it while the dialog was
  open, avoiding a race with scene code.

## [v43] - 2026-09-11

### Fixed

- Prevented branch-jump confirmation from overwriting game objects with
  strings or booleans. Only existing scalar variables are now offered and
  written; object roots such as `nurse` remain untouched.
- Added a final scalar-type guard before applying each selected value.
- Confirmation is now a hard gate whenever enabled: even a branch with no
  editable scalar variables waits for Done before jumping.

## [v42] - 2026-09-11

### Fixed

- Fixed a Ren'Py screen-variable scope error caused by reading the local
  search input through `GetScreenInput` during screen evaluation.
- Label Tree now reads its local `InputValue` with the documented
  `get_text()` method, while retaining the original URM bridge for action
  callbacks.
- Normalizes the returned value through the mod's Python 2.7-safe text helper
  so non-ASCII queries do not depend on the base interpreter's `str()`
  conversion.

## [v41] - 2026-09-11

### Fixed

- Fixed incremental searches restarting from index zero on every screen
  redraw, which left the result count at `0 (searching...)` indefinitely.
- Reads the Label Tree query through the original URM screen-input bridge for
  Ren'Py 7.4 compatibility.
- Fixed the direct-jump helper used when branch confirmation is disabled or
  no conditional variables are found.
- Conditional value extraction now recognizes both tuple and list membership
  expressions.

## [v40] - 2026-09-11

### Added

- Added an optional branch-variable confirmation dialog before Label Tree
  jumps. Conditional variables are collected from the complete flow, with
  observed comparison and membership values available from dropdown menus.
- Added a persistent View Filter toggle for the confirmation dialog.

### Fixed

- Searches now start against the first published partial graph instead of
  remaining at `0 (searching...)` until the full AST build completes.

## [v39] - 2026-09-11

### Fixed

- Keeps an active search synchronized with labels published by the background
  AST build, so a search cannot finish against only the first partial graph.

## [v38] - 2026-09-11

### Fixed

- Adds an in-pane searching indicator while large result sets are still being
  indexed, so partial results are clearly distinguished from the final count.

## [v37] - 2026-09-11

### Added

- Search now accepts context terms in any order. For example, `nurse quest`
  matches `nurse_quest`, `quest_nurse`, and `nurse_02_quest` when the relevant
  search fields are enabled.
- Search indexing runs in small background batches, with ranked results and a
  debounced persistent query so typing and reopening URM remain responsive.

## [v35] - 2026-09-11

### Fixed

- Places the depth chooser on URM's `x52Overlay` layer so it renders above
  the Label Tree window instead of underneath the overlay.
- Removes the remaining Ren'Py load-order dependency in the depth wrapper.
  Captured module functions are now called directly instead of being assumed
  to exist as `LabelTreeClass` instance attributes, preventing the
  `_lt_original_depth_step` launch-time crash.

## [v34] - 2026-09-11

### Fixed

- Binds the runtime graph reindex helper to `LabelTreeClass` before the
  incremental build wrapper uses it, preventing the launch-time
  `_lt_reindex_partial` AttributeError on Ren'Py 7.4.

## [v33] - 2026-09-11

### Fixed

- Loads the depth-control overlay explicitly through x52MF2, so the depth
  chooser and bidirectional branch traversal are active in the runtime archive.
- Keeps the full-flow default while allowing bounded incoming/outgoing depth
  around the current, selected, and searched anchors.

## [v32] - 2026-09-11

### Added

- Added a persistent current-branch depth chooser. The default `All` mode
  shows the complete flow in both directions; bounded modes include the
  selected number of incoming and outgoing flow edges around each active
  label.
- The depth traversal is cached and uses the graph's published partial index,
  so the view grows as the background build discovers more labels and links.

### Fixed

- The current-branch filter now uses bidirectional adjacency for bounded
  views, instead of showing only the active label when a full static path is
  not yet available.

## [v31] - 2026-09-11

### Fixed

- The main x52MF2 loader now explicitly loads all Label Tree runtime overlay
  sources. Previously those files could be packed into the RPA but remained
  inactive, leaving only the old single-label view.

## [v30] - 2026-09-11

### Fixed

- Prioritizes the live game label during the initial build so the current
  label appears before the background scan continues.
- Observes the original URM label monitor and resolves Ren'Py 7.4 live
  context, rollback, and return-stack statements back to labels when possible.
- Publishes partial indexes while scanning so the current branch appears
  immediately and grows into the complete start-to-finish flow.

### Compatibility

- Guards opaque/unhashable Ren'Py return-stack statement names.
- The packer now accepts optional extra source files for compatibility overlays.

All notable URMPlus changes are recorded here. Release archives use the
`0x52_URM.patched-vN.rpa` naming convention.

## [v29] - 2026-09-11

### Fixed

- Corrected current-label detection for Ren'Py 7.4.4. The tree now reads the
  live execution context's current AST statement and resolves it back to its
  containing label, instead of treating the public context-info object as if
  it exposed the executing statement.
- Added an AST-object fallback for opaque or unnamed statement identifiers,
  while retaining the original URM `LabelMon.lastLabel` callback as a safe
  fallback during menu, save, and load context transitions.
- View-filter branches now walk from their entry labels through the complete
  directed flow to every reachable join and terminal path, including
  conditional branches, cycles, and implicit fall-through links.

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
