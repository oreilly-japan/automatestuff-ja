#! python3
# -*- coding: utf-8 -*-

import glob
import re
from collections import Counter

counter = Counter()
token_re = re.compile(r'([一-龥]+|[A-Za-z][0-9A-Za-z_]*|[ァ-ヾ]+)')

for fname in glob.glob('ch*.md'):
    print(fname)
    with open(fname, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('> ■'):
                continue
            tokens = token_re.findall(line)
            counter.update(tokens)

for k in sorted(counter.keys()):
    print(k + ',' + str(counter[k]))

