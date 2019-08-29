def pr(s): return s


def print_num(x): return (x == 1 and pr('one')) \
    or (x == 2 and pr('two')) \
    or (pr('three'))

print(print_num(1))
print(print_num(2))
print(print_num(3))
