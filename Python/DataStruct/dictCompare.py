"""查找两字典的相同点"""
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}


comm_key = a.keys() & b.keys()
only_a = a.keys()-b.keys()
comm_kv = a.items() & b.items()

c = {key: a[key] for key in a.keys()-{'z', 'w'}}

print(comm_key)
print(only_a)
print(comm_kv)
print(c)
