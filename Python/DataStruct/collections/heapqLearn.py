import heapq
import pysnooper


class LargeAndSmall:
    def __init__(self, data: list):
        self._data = data

    def getLarge(self, n: int, key: str):
        return heapq.nlargest(n, self._data, lambda s: s[key])

    def getSmall(self, n: int, key: str):
        return heapq.nsmallest(n, self._data, lambda s: s[key])

    @staticmethod
    def testData():
        return [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]

    @staticmethod
    def test():
        testit = LargeAndSmall(LargeAndSmall.testData())
        with pysnooper.snoop(watch=['tmp']):
            tmp = testit.getLarge(3, 'price')
            tmp = testit.getSmall(3, 'price')


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        # item1 < item2 => wrong,不能比较
        # 引入元组可以比较大小：
        #   (1, item1) < (2, item2) => true
        # 防止优先级一样时比较大小出错，引入 index:
        #   (1, index1, item1) < (2, index2, item2) => true

    def pop(self):
        return heapq.heappop(self._queue)

    @staticmethod
    @pysnooper.snoop(watch=['tmp'])
    def test():
        testit = PriorityQueue()
        for x in iter([['test1', 10], ['test2', 20],
                       ['test3', 30], ['test4', 5], ]):
            testit.push(*x)
        # print(testit._queue)
        tmp = testit.pop()[-1]
        print(f"优先级最高的是:{tmp}")


if __name__ == '__main__':
    # LargeAndSmall.test()
    PriorityQueue.test()
