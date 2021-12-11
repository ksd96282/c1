# ==============================================
# n = int(input("数字を入力 > "))
# if n % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")

# ==============================================
# kion = input("今の気温は？ > ")
# kion = int(kion)
# if kion >= 25:
#     print("氷水を出す")
# else:
#     print("熱いお茶を出す")

# ==============================================
# # 遊園地の入場料を計算
# price_children = 500
# price_adult = 1000
# price_elder = 700
#
# children_num = int(input("13歳以下の子供の人数 > "))
# children_total_price = children_num * price_children
# adult_num = int(input("大人(14～64歳)の人数 > "))
# adult_total_price = adult_num * price_adult
# elder_num = int(input("65歳以上の人数 > "))
# elder_total_price = elder_num * price_elder
#
# total_num = children_num + adult_num + elder_num
# total_price = children_total_price + adult_total_price + elder_total_price
#
# waribiki = "なし"
# if total_num >= 10:
#     print("団体割引で合計金額から8割引きされます")
#     waribiki = "あり(8割引き)"
#     total_price = round(total_price * 0.8, 0)
#
# fmt = """
# 子供の料金： {0}人 * {1}円 = {2}円
# 大人の料金： {3}人 * {4}円 = {5}円
# 年配者の料金： {6}人 * {7}円 = {8}円
# 割引き： {9}
# 合計金額： {10}円
# """

# print(fmt.format(children_num, price_children, children_total_price,
#                  adult_num, price_adult, adult_total_price,
#                  elder_num, price_elder, elder_total_price,
#                  waribiki,
#                  total_price))

# ==============================================
# BMI計算 p62
# height = float(input("身長(m) > "))
# weight = float(input("体重(kg) > "))
# bmi = round(weight / (height * height), 1)
#
# result = ""
# if bmi < 18.5:
#     result = "やせ型"
# if 18.5 <= bmi < 25:
#     result = "標準体形"
# if 25 <= bmi < 30:
#     result = "軽度の肥満"
# if bmi >= 30:
#     result = "重度の肥満"
#
# print(f"BMI: {bmi}")
# print(f"結果: {result}")

# ==============================================
# a = True
# b = True
# if a:
#     print("aはTrue")
# elif b:
#     print("bはTrue")
# else:
#     print("aもbもFalse")

# ==============================================
# うるう年を判定するプログラム -66
# year = int(input("西暦を入力 > "))
# is_leap = False

# if year % 4 == 0:   # 4で割れたらうるう年
#     if year % 100 == 0: #100で割れたらうるう年ではない
#         if year % 400 == 0: #400で割れたらうるう年
#             is_leap = True
#         else:
#             is_leap = False
#     else:
#         is_leap = True
# else:
#     is_leap = False

# is_leap = (year % 400 == 0)or\
#           (year % 100 != 0)or\
#           (year % 4 == 0)
# if is_leap:
#     print(f"{year}年はうるう年です")
# else:
#     print(f"{year}年はうるう年ではありません")

# ==============================================
