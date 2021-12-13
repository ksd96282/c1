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
# print(f"印税は{v}円です")
#
# help(calc_royalty)

# ###########################################
# 動物の最高速で都市間移動したときの所要時間
animal_speed = {
    "チーター": 110,
    "トナカイ": 80,
    "シマウマ": 60,
    "ライオン": 58,
    "キリン": 50,
    "ラクダ": 30
}
dist_from_tokyo = {
    "静岡": 183.7,
    "名古屋": 350.6,
    "大阪": 507.5
}

# 時間 = 距離 / 速度
def calc_time(dist, speed):
    time = round(dist / speed, 1)
    return time

# 動物ごとの都市間移動速度
def calc_animal(animal, speed):
    res = "|" + animal
    for city in sorted(dist_from_tokyo.keys()):
        dist = dist_from_tokyo[city]
        time = calc_time(dist, speed)
        res += "|{0:>6}".format(time)
    return res + "|"

# ヘッダーを作成
line = "+--------+------+------+------+"
print(line)
print("|動物名", end="")
for city in sorted(dist_from_tokyo.keys()):
    print(f"|{city}", end="")
print(f"|\n{line}")

# 各動物ごとに結果を求めて表示
for animal, speed in animal_speed.items():
    print(calc_animal(animal, speed))
print(line)
