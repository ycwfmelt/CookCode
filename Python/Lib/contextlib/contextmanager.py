from contextlib import contextmanager


@contextmanager
def co(f):
    try:
        yield f
    finally:
        print('close')


with co('this') as f:
    print(f)
