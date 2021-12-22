# 関数の定義と利用  -p116

# # ###########################################
# # 関数の定義
# def mul(a, b):
#     return a * b
# print(mul(10, 5))
#
# mul_lambda = lambda a, b: a* b
# print(mul_lambda(10, 5))

# # ###########################################
# # 本の印税を計算する関数
# def calc_royalty(price, sales, per):
#     '''印税を計算する関数'''
#     rate = per / 100    # 印税率：ここでは10を100で割る
#     ro = int(price * sales * rate)  # 印税 = 定価 * 発行部数 * 印税率
#     return ro
#
# price = int(input("定価 > "))
# sales = int(input("発行部数 > "))
# per = float(input("印税率 > "))
# v = calc_royalty(price, sales, per)
# print(fi"印税は{v}円です")
#
# help(calc_royalty)

# # ###########################################
# # 動物の最高速で都市間移動したときの所要時間
# animal_speed = {
#     "チーター": 110,
#     "トナカイ": 80,
#     "シマウマ": 60,
#     "ライオン": 58,
#     "キリン": 50,
#     "ラクダ": 30
# }
# dist_from_tokyo = {
#     "静岡": 183.7,
#     "名古屋": 350.6,
#     "大阪": 507.5,
#     "札幌": 825
# }
#
# # 時間 = 距離 / 速度
# def calc_time(dist, speed):
#     time = round(dist / speed, 1)
#     return time
#
# # 動物ごとの都市間移動速度
# def calc_animal(animal, speed):
#     # res = "|" + animal
#     res = fi"|{animal:<6}"
#     for city in sorted(dist_from_tokyo.keys()):
#         dist = dist_from_tokyo[city]
#         time = calc_time(dist, speed)
#         res += "|{0:>8}".format(time)
#     return res + "|"
#
# # ヘッダーを作成
# i = 0
# line = ""
# for animal in animal_speed:   # animal_speedのkeyの中から最大文字数を取得
#     if len(animal) > i:
#         i = len(animal)
# for j in range(len(dist_from_tokyo)+1):    # animal_speedのkeyの文字数に合わせて水平の罫線を生成
#     line += "+"
#     for k in range(i*2):
#         line += "-"
# line += "+"
#
# print(line)
# t2 = "| 動物名"
# print(fi"{t2:<7}", end="")
# for city in sorted(dist_from_tokyo.keys()):
#     print(fi"|{city:^6}", end="")
# print(fi"|\n{line}")
#
# # 各動物ごとに結果を求めて表示
# for animal, speed in animal_speed.items():
#     print(calc_animal(animal, speed))
# print(line)

# # ###########################################
# # 再起
# print("# for文で実行")
# for i in range(10, 0, -1):
#     print("hello", i)
#
# print("\n# 関数の再起で実行")
# def say_hello(j):
#     if j <= 0: return
#     print("hello", j)
#     say_hello(j-1)
# say_hello(10)

# # 階乗を求める
# def fact(n):
#     if n == 0:  # 引数が0になったら1を返す
#         return 1
#     else:   # それ以外の場合は再帰的にfact()関数を呼ぶ
#         return n * fact(n - 1)
# print(fact(3))
# print(fact(5))

#  # 畳を平米に変換
# def convert_jou(jou, unit="江戸間"):
#     if unit == "江戸間":
#         base = 0.88 * 1.76
#     elif unit == "京間":
#         base = 0.955 * 1.91
#     elif unit == "中京間":
#         base = 0.91 * 1.82
#     else:
#         print("間取りを正しく入力してください(江戸間/京間/中京間)")
#         return
#     m2 = jou * base
#     print(fi"{unit:5} で {jou}畳 は {m2}㎡")
#
# # 関数を実行
# convert_jou(jou=6, unit="江戸間")
# convert_jou(jou=6, unit="京間")
# convert_jou(6, "中京間")
# convert_jou(6)

# # 可変長引数
# def sum_args(*args):
#     v = 0
#     for n in args:
#         v += n
#     return v
# print(sum_args(1,2,3))
# print(sum_args(1,2,3,4,5,6,7,8,9,10))
# args = [1,2,3,4,5,6,7,8,9,10]     # リストは指定できない
# print(sum_args(args))

# # 辞書型の可変長引数
# def print_args(**args: object) -> object:
#     print(args)
#     return args
# args = print_args(a=30, b=50, c=100)
# print(args)

# グローバル変数
value = 100
def cng_value():
    global value
    value = 20
cng_value()
print(f"value = {value}")