import json
import pathlib

import pooch


def main():
    data_dir = pathlib.Path(__file__).parent / 'data'
    files = sorted(f for f in data_dir.iterdir() if f.is_file() and not f.name.endswith('.json'))
    checksums = {file.name: pooch.file_hash(file, alg='sha256') for file in files}
    with open(data_dir.parent / 'sha256_checksums.json', 'w') as f:
        json.dump(checksums, f, indent=2)


if __name__ == '__main__':
    main()
