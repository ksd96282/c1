# # ■無名関数
# def mul_func(a, b): return a * b
# def div_func(a, b): return a / b
# def add_func(a, b): return a + b
# def sub_func(a, b): return a - b
#
# func = mul_func
# result = func(2, 3)
# # print(result)
# func2 = div_func
# result2 = func2(2, 3)
# # print(result2)
#
# def calc_5_3(func):
#     return func(5, 3)
#
# # result = calc_5_3(mul_func)
# result = calc_5_3(lambda a, b: a * b)
# print(result)
# # result = calc_5_3(mul_func)
# result = calc_5_3(lambda a, b: a + b)
# print(result)

# def calc_time(dist, speed): round(dist / speed)
# calc_time = lambda dist, speed: round(dist / speed)
# print(calc_time(500, 100))

# # lambda map()と併用
# nums = [1, 3, 5, 7, 9]
# print(fi"nums = {nums}")
# x2 = lambda x: x * 2  # 値を2倍にするlambda式
# print(fi"lambda式で値を2倍にしたnums = {list(map(x2, nums))}")
# print(fi"lambda式で値を文字列にしたnums = {list(map(lambda x: str(x)+'_str', nums))}")

# # lambda filter()と併用
# import random
#
# nums = []
# for i in range(10):
#     n = random.randint(1, 100)
#     nums.append(n)
#
# print(fi"nums = {nums}")
# print(fi"numsから奇数を抽出 = {list(filter(lambda x: (x % 2), nums))}")
# print(fi"numsから偶数を抽出 = {list(filter(lambda x: (x % 2)==0, nums))}")
# print(fi"50より大きい値を抽出 = {list(filter(lambda x: x > 50, nums))}")

# # タプルのリストをソートする
# animal_list = [
#     ((1, "lion"), 58),
#     ((2, "cheetah"), 110),
#     ((3, "zebra"), 60),
#     ((4, "reindeer"), 80)
# ]
# # 速い順に並べ替え
# faster_list = sorted(
#     animal_list,
#     key=lambda ani: ani[0][1],
#     reverse=False
# )
# for i in faster_list: print(i)

# 辞書型をソートする
animal_list = {
    "lion": 58,
    "cheetah": 110,
    "zebra": 60,
    "reindeer": 80
}
faster_list = sorted(
    animal_list.items(),
    key=lambda x: x[1],
    reverse=True
)
# li = {}
def less_than_100(faster_list):
    li = {}
    for name, speed in faster_list:
        # print(name, speed)
        if speed < 100:
            li[name] = speed
    return li
print(less_than_100(faster_list))
