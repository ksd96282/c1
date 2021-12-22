# # イテレータ、ジェネレータ
# for i in range(1, 4):
#     print(i)
# print("---")
#
# nums = [2, 4, 6]
# for i in nums:
#     print(i)
# print(fi"iter(nums) = {iter(nums)}")
# print(list(iter(nums)))

# # range()関数のイテレータ
# i = iter(range(1, 4))
# print(next(i))
# print(next(i))
# print(next(i))

# yieldで値を返す関数を定義
def gen_1to3():
    yield 1
    yield 5
    yield 3
it = gen_1to3()
for i in it:
    print(i)

