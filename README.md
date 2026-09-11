# URMPlus

URMPlus is a Label Tree enhancement for the Universal Ren'Py Mod (URM). It
adds a navigable view of a game's labels, control-flow links, and in-label
branching to the existing `Alt+M` overlay.

This repository contains the Ren'Py source, the local RPA build tools, the
preserved original archive used as a packing source, and tested release
archives.

## Features

- Label Tree tab in the URM overlay.
- Visual label nodes with connecting control-flow paths.
- Mid-path condition nodes showing branch triggers such as `if ...`, links,
  variables, and statements.
- Expandable in-label details for conditionals and variable/statement data.
- Search across labels, variables, conditions, links, statements, and
  optionally internal labels.
- Search results preview pane with wrapped names, a collapsible layout, and
  Previous/Next navigation.
- Search-result highlighting that remains visible alongside current-label and
  selected-node highlighting.
- Focus filters for searched branches and the current branch.
- Left-mouse drag panning and scroll-wheel zooming in the tree viewport.
- Single-click node selection, a Center Selected control, and double-click
  navigation to a label.
- Center Current control for returning to the active in-game label.
- Incremental AST discovery, cached search fields, bounded viewport rendering,
  and deferred layout work to keep the overlay responsive on large games.
- Save/load-aware current-label tracking that ignores Ren'Py helper labels such
  as `save_screen`, `load_screen`, and `after_load`.
- Isolated `x52URM` state and Ren'Py-compatible Python 2.7/screen-language
  syntax for the bundled Ren'Py 7.4.4 runtime.

## Compatibility

The current release is tested against a Ren'Py 7.4.4.1439 runtime (Python 2.7). 
The implementation intentionally
avoids Python 3-only syntax, variadic `min`/`max` calls, eager full-tree screen
construction, and assumptions about a game's own global variables.

The Label Tree reads Ren'Py's runtime label/AST data and should be treated as
best-effort across games. Games that replace URM screens or label callbacks may
need a small integration adjustment.

## Installation

1. Back up the game's existing `game/0x52_URM.rpa`.
2. Copy a tested `0x52_URM.patched-v*.rpa` archive into the game's `game`
   directory.
3. Rename the selected archive to `0x52_URM.rpa` if necessary.
4. Launch the game and open the URM overlay with `Alt+M`.
5. Select **Label Tree** from the left-hand menu.

Keep the original archive so the change can be reverted safely. Do not unpack
or replace the base game's compiled `.rpyc` files.

## Building and testing

The included tools use the archive's existing RPA format:

```text
python tools/extract_rpa.py <input.rpa> <output-directory>
python tools/pack_rpa.py <base.rpa> <output.rpa> <source-file> [<source-file> ...]
```

For Ren'Py compatibility checks, run the game's bundled Ren'Py executable in
`lint` mode against a temporary extracted source directory. The `.rpy.x52`
files are loaded by URM's runtime loader, so an ordinary project lint may not
enumerate them as normal `.rpy` screens; the actual game remains the final
integration test.

## Repository layout

```text
0x52-URM/screens/       Uncompiled URMPlus Ren'Py sources
tools/                  RPA extraction and packing utilities
original/               Preserved original URM archive
0x52_URM.patched-v*.rpa  Tested distributable archives
CHANGELOG.md            Release history and compatibility notes
DEVELOPMENT.md           Ren'Py-compatible development guide
```

## Project status

URMPlus is an iterative compatibility-focused mod. Report the Ren'Py version,
game version, archive version, and full traceback when reporting an issue.

## Credits and scope

URMPlus modifies the URM overlay and is not affiliated with Ren'Py or the
original game. The repository does not grant redistribution rights for the
original game or its assets. No separate open-source license is currently
declared for this repository.
