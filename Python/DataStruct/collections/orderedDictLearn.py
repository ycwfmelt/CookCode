from collections import OrderedDict
import sys


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

dd = dict()
dd['foo'] = 1
dd['bar'] = 2
dd['spam'] = 3
dd['grok'] = 4

for k in d:
    print(k, d[k])

print(f"dict 占用: {sys.getsizeof(dd)}")
print(f"orderedDict 占用: {sys.getsizeof(d)}")
