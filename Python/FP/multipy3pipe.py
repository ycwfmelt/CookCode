class Pipe:
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.func(obj)
        return generator()

@Pipe
def even_filter(num):
    return num if num%2==0 else None
