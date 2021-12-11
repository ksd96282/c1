# 変数に計算式を入れて表示
# one = 10+20*30/50
# two = (1+2+3)*22
# three = 3333*4444*5555
# print(one)
# print(two)
# print(three)

# 三重引用符の利用
# str = """\
# 今日はよい天気です。
# 明日もよい天気です。
# でも明後日は雨です。\
# """
# print(str)

# 文字列の連結
# s = "hello,"+"world"
# print("s = "+ s)
# s1 = "hello,"
# s2 = "world"
# s3 = s1 + s2
# print("s3 = "+ s3)

#文字列と数字の連結
# kion = 30
# kionStr = str(kion)
# print("気温は"+ kionStr +"度です")

# インチをセンチメートルに変換
# per_inch = 2.54
# inch = 24
# cm = inch * per_inch
# # 普通に記述
# desc1 = str(inch) +"インチ = "+ str(cm) +"センチ"
# print(desc1)
# # format()関数を使って記述
# desc2 = "{0}インチ = {1}センチ".format(inch, cm)
# print(desc2)

# format()関数で名前付き引数を使う
# 1
print("私は{name}です".format(name="ミドリ"))
# 2
fmt = "年齢は{age}歳、{job}をやっています"
s = fmt.format(age=25, job="プログラマー")
print(s)
