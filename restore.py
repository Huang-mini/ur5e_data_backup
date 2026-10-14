#!/usr/bin/env python3
import hashlib, json, pathlib, tarfile, urllib.request

root = pathlib.Path(__file__).resolve().parent
cfg = json.loads((root / 'downloads.json').read_text())
for item in cfg['assets']:
    target = root / item['name']
    if not target.exists():
        print('downloading', item['name'])
        urllib.request.urlretrieve(item['url'], target)
    h = hashlib.sha256(target.read_bytes()).hexdigest()
    if h != item['sha256']:
        raise SystemExit(f'checksum mismatch: {target}')
    print('extracting', item['name'])
    with tarfile.open(target) as tf:
        tf.extractall(root, filter='data')
print('restore complete')
