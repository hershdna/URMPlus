from __future__ import print_function

import pickle
import sys
import zlib
from pathlib import Path


def read_archive(path):
    with path.open('rb') as fp:
        header = fp.readline()
        if not header.startswith(b'RPA-2.0'):
            raise RuntimeError('unsupported archive')
        offset = int(header.split()[1], 16)
        fp.seek(offset)
        index = pickle.loads(zlib.decompress(fp.read()))
        payloads = {}
        for name, chunks in index.items():
            pieces = []
            for chunk in chunks:
                offset, length = chunk[:2]
                fp.seek(offset)
                pieces.append(fp.read(length))
            payloads[name] = b''.join(pieces)
    return payloads


def write_archive(path, payloads):
    index = {}
    with path.open('wb') as fp:
        fp.write(b'RPA-2.0 0000000000000000\n\r\n')
        for name in sorted(payloads):
            data = payloads[name]
            offset = fp.tell()
            fp.write(data)
            index[name] = [(offset, len(data))]
        index_offset = fp.tell()
        fp.write(zlib.compress(pickle.dumps(index, protocol=2), 3))
    with path.open('r+b') as fp:
        header = ('RPA-2.0 %016x\n\r\n' % index_offset).encode('ascii')
        fp.write(header)


if __name__ == '__main__':
    source_archive = Path(sys.argv[1])
    output_archive = Path(sys.argv[2])
    main_source = Path(sys.argv[3])
    labeltree_source = Path(sys.argv[4])
    payloads = read_archive(source_archive)
    payloads['0x52-URM/screens/main.rpy.x52'] = main_source.read_bytes()
    payloads['0x52-URM/screens/labeltree_v2.rpy.x52'] = labeltree_source.read_bytes()
    write_archive(output_archive, payloads)
    print('packed', len(payloads), 'files to', output_archive)
