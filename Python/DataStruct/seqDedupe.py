def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)
        print("seen:", seen)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


def dedupe(items, key=None):
    seen = set()
    for item in items:
        if val == key:
            pass

