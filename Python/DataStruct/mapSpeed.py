from timeit import timeit


def a():
    nums = ""
    for n in range(2000):
        nums += str(n)
    return nums


def b():
    nums = [str(n) for n in range(2000)]
    return "".join(nums)


def c():
    nums = map(str, range(2000))
    return "".join(nums)


ta = timeit(a, number=100)
tb = timeit(b, number=100)
tc = timeit(c, number=100)
print(ta)   # 0.09160405400000002
print(tb)   # 0.06693120000000002
print(tc)   # 0.05834111999999997
