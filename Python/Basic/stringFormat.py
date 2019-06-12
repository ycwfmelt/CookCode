class Test:
    def __repr__(self):
        return 'repr'

    def __str__(self):
        return 'str'


if __name__ == '__main__':
    test = Test()

    print("{!r}".format(test))
    # repr

    print("{!s}".format(test))
    # str

    print("{here!r:20}".format(here=test))
