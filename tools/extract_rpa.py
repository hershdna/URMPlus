from __future__ import annotations

import pickle
import shutil
import sys
import zlib
from pathlib import Path


def main() -> None:
    archive = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    with archive.open("rb") as fp:
        header = fp.readline()
        if not header.startswith(b"RPA-2.0"):
            raise RuntimeError(f"unsupported archive header: {header!r}")
        index_offset = int(header.split()[1], 16)
        fp.seek(index_offset)
        index = pickle.loads(zlib.decompress(fp.read()))
        for name, chunks in index.items():
            target = out_dir / Path(name)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("wb") as dst:
                for offset, length, *rest in chunks:
                    fp.seek(offset)
                    data = fp.read(length)
                    if rest:
                        data = zlib.decompress(data)
                    dst.write(data)
    print(f"extracted {len(index)} files to {out_dir}")


if __name__ == "__main__":
    main()
