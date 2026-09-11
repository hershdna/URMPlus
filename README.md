# Label Tree test workspace

This directory contains the uncompiled Label Tree sources, the preserved original URM archive, and the local RPA pack/extract tools used for iteration.

The current test build uses incremental AST scanning, timer-driven build steps,
cached search fields, cached search results, and viewport-limited displayables
for Ren'Py 7.4.4.

Compatibility target: the bundled Ren'Py 7.4.4 runtime (Python 2.7-style
screen/Python behavior). New code avoids newer Python syntax and uses Ren'Py
screen-language constructs supported by that runtime.

The preserved original archive is used as the pack source. The generated patched
archive is kept outside this repository and installed into the game during local
testing, so the original archive remains recoverable.
