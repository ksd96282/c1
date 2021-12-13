# 辞書型   -p102
# # ###########################################
# # 辞書型のデータを作成
# ages = {"鈴木":30, "佐藤":40, "田中":20, "高橋":10}
# print(ages) # リストの内容すべてを表示
# print(ages["鈴木"])   # リストの中から指定したキーの値を表示
# ages["鈴木"] = 31 # リストの中の指定したキーの値を更新
# print(ages["鈴木"])

# # ###########################################
# リストの中にキーがあるか確認する
# fruits_price = {"orange":150, "apple":150, "peach":250, "grape":400, "mango":500, "melon":1500, "banana":100}
# print("grapeはある？", "grape" in fruits_price)
# print("mangoの値段は？", fruits_price["mango"])
# print("pareはある？", "pare" in fruits_price)

# # ###########################################
# # 辞書型をいじる
# fruits_price = {"orange":150, "apple":150, "peach":250, "grape":400, "mango":500, "melon":1500, "banana":100}
# print("キー一覧を表示 dict.keys(): ", fruits_price.keys())
# fruits_list = list(fruits_price.keys())
# print("キー一覧をリストに格納 list(dict.keys()): ", fruits_list)
# print("キー一覧をソートして表示 sorted(dict.keys()):", sorted(fruits_price.keys()))
# print("値の一覧を表示する dict.values(): ", fruits_price.values())
# fruits_tuple = list(fruits_price.items())
# print("(キー, 値)をタプルで得る list(dict.items())", fruits_tuple)
# print(fruits_tuple[0])

# # ###########################################
# # forで辞書型を扱う
# fruits_price = {
#     "orange": 150,
#     "apple": 150,
#     "peach": 250,
#     "grape": 400,
#     "mango": 500,
#     "melon": 1500,
#     "banana": 100
# }
# for name in fruits_price.keys():  # dict.keys()で実行
#     price = fruits_price[name]
#     print(f"{name}は{price}円です")
# for name, price in fruits_price.items():  # dict.items()で実行
#     print(f"{name}は{price}円です")

# # ###########################################
# # 成績データを辞書型で定義
# records = {
#     "Tanaka": 100,
#     "Suzuki": 98,
#     "Takahashi": 89,
#     "Sato": 77,
#     "Watanabe": 87
# }
# sum_points = 0
# for point in records.values():
#     sum_points += point
# ave_points = round(sum_points / len(records))
# print(f"合計点： {sum_points}")
# print(f"平均点： {ave_points}")
#
# # 成績データの一覧と平均点との差を表示
# fmt = "|{0:<10}|{1:>5}|{2:>5}|"
# print(fmt.format("Name", "Pt", "Diff"))
# for name, v in records.items():
#     diff_v = v - ave_points
#     print(fmt.format(name, v, diff_v))

# ###########################################
# 英単語の出現回数をカウント
text = """
Keep on asking, and it will be given you;
Keep on seeking, and you will find;
Keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""
# 単語を区切る
text = text.replace(";", "")    # 「;」を削除
text = text.replace(",", "")    # 「,」を削除
text = text.replace(".", "")    # 「.」を削除
words = text.split()    # スペースで区切って単語をリストに格納する

# 単語を数える
counter = {}    # 空の辞書型を作成
for w in words:
    ws = w.lower()  # 小文字に変換
    if ws in counter:
        counter[ws] += 1    # counterにwsがあれば値を+1
    else:
        counter[ws] = 1     # counterにwsがなければ値を1としてキーに格納

for k, v in sorted(counter.items()):
    if v <= 3:
        print(f"{k}: {v}回")