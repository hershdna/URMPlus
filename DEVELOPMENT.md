# Development guide

## Source of truth

The uncompiled files under `0x52-URM/screens/` are the editable source of the
Label Tree integration. The RPA files are generated test/release artifacts.
The archive under `original/` is kept unchanged for comparison and recovery.

## Ren'Py constraints

The target runtime is Ren'Py 7.4.4.1439 with Python 2.7. Code must remain
compatible with that environment:

- Use Python 2.7 syntax and built-ins only.
- Keep mod state under the isolated `x52URM` namespace.
- Use Ren'Py screen language for displayables and screen actions.
- Avoid work in screen-expression evaluation that scans the entire game.
- Defer expensive indexing/layout work and cache results between interactions.
- Use explicit two-argument min/max helpers where compatibility is important.
- Treat `renpy.context().current` as a statement identifier, not automatically
  as a label name.
- Do not assume a game's labels, variables, or character objects exist.
- Store cross-session UI preferences only in a mod-specific persistent field;
  use `renpy.save_persistent()` after a preference change.

## Safe iteration

1. Copy the installed archive to a backup before testing.
2. Extract or reuse the original archive as the packing base.
3. Modify only the uncompiled source under `0x52-URM/screens/`.
4. Run the bundled Ren'Py lint check against a temporary staging directory.
5. Build a new numbered archive; do not overwrite earlier release artifacts.
6. Test launch, overlay opening, search typing, viewport dragging/zooming,
   save/load, and current-label centering in-game.
7. Record user-visible fixes in `CHANGELOG.md`.

## Runtime references

The implementation follows Ren'Py's documented label and screen behavior:

- [Labels and control flow](https://www.renpy.org/doc/html/label.html)
- [Screen language and viewports](https://www.renpy.org/dev-doc/html/screens.html#viewport)
- [InputValue](https://www.renpy.org/doc/html/screen_python.html#inputvalue)
