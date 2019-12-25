# def process(num):
#     if num % 2 != 0:
#         return
#     num = num * 3
#     num = 'The Number: %s' % num
#     return num

# nums = [i for i in range(10)]

# for num in nums:
#     print(process(num))


def even_filter(nums):
    return filter(lambda x: x % 2 == 0, nums)


def multipy_by_three(nums):
    return map(lambda x: x*3, nums)


def convert_to_string(nums):
    return map(lambda x: 'The Number: %s' % x, nums)

nums = [i for i in range(1,10)]
pipeline = convert_to_string(multipy_by_three(even_filter(nums)))

for num in pipeline:
    print(num)
