# ============================================================
# # リストの中身をforで取り出す
# points = [100, 90, 73, 98, 34]
# sum_v = 0
# # 合計点
# for i in points:
#     sum_v += i
#     print(f"{i}点を足して合計は{sum_v}")
# # 平均点
# ave_v = sum_v / len(points)
# print(f"平均点: {ave_v}")

# # ============================================================
# # sum()関数を使う
# points = [100, 90, 73, 98, 34]
# sum_v = sum(points)
# ave_v = round(sum_v / len(points))
# print(f"合計点: {sum_v}\n"
#       f"平均点: {ave_v}")

# # ============================================================
# # ランダム格言bot
# import random
# kakugen = [
#     "能ある鷹は爪を隠す",
#     "豚に真珠",
#     "二兎を追う者は一兎をも得ず",
#     "たたき続けなさい。そうすれば開かれます。"
# ]
# i = random.randint(0, len(kakugen)-1)
# print(kakugen[i])

# # ============================================================
# # インデックス番号付きでfor -enumerate()
# animal = ["cat", "dog", "rabbit", "lion", "tiger", "wolf", "dragon", "orca", "duck"]
# for i, v in enumerate(animal):
#     print(i, v)
# # enumerate()の挙動 (REPLで実行)
# list(enumerate(animal))

# # ============================================================
# # リストに要素を追加 -append()
# animal = ["cat", "dog", "rabbit", "lion", "tiger", "wolf", "dragon", "orca", "duck"]
# animal.append("fox")
# animal.append("baby")

# # # 点数リストから赤点だけ取り出す
# # 10人の点数をランダムに生成
# import random
# points = []
# for i in range(10):
#     points.append(random.randint(0,100))
# print(points)
# # 30点未満だけ取り出して赤点リストに追加
# akaten = []
# for p in points:
#     if p < 30:
#         akaten.append(p)
# print(akaten)

# # ============================================================
# # リストをシャッフル
# import random
# # 元のリストをシャッフル -random.shuffle()
# random.shuffle(animal)
# print(animal)
# # リストをシャッフルして新しいリストに代入 -random.sample()
# animal_sh = random.sample(animal, len(animal))
# for i, v in enumerate(animal_sh):
#     print(i, v)
# print(animal_sh)

# # ============================================================
# # ■リストを結合する
# # リストを結合して新しいリストを生成
# n1 = [1, 2, 3]
# n2 = [4, 5, 6]
# n3 = n1 + n2
# print(f"n3 = {n3}")
# # 既存のリストに複数の要素を追加
# n4 = [7, 8, 9]
# n4 += [10, 11, 12]
# print(f"n4 = {n4}")
# # extend()を使って結合
# n5 = [13, 14, 15]
# n5.extend([16, 17, 18])
# n5.extend([19])
# print(f"n5 = {n5}")

# # ============================================================
# # ■リストをスライス
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a[0:3])   # index0からindex3の手前まで
# print(a[7:])    # index7から最後まで
# print(a[-2])    # 後ろから2つ目の要素
# print(a[-3:])   # 後ろから3つ目から最後まで
# print(a[2:8:2]) # index2からindex8の手前までを2つ刻みで
# print(a[::3])   # 最初から最後まで3つ刻みで

# # ============================================================
# # ■リストから要素を削除する
# l = []
# for i in range(10):
#     l.append(i)
# del l[2]    # index2の要素を削除
# print(l)
# del l[5:8]  # スライスを指定して特定の範囲を削除
# print(l)

# ============================================================
# ■その他のリスト操作メソッド
# import random

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # append(x) 値xをリストの末尾に追加する
# l.append(11)
# print(l)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# # extend(L) 異なるリストLを末尾に追加する
# L = [11, 12, 13]
# l.extend(L)
# print(l)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# # insert(i, x) インデックスiの位置に値xを追加する
# l.insert(1, 111)
# print(l)    # [0, 111, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # remove(x) リストの中の値xを削除する(最初に見つかったもののみ)
# l.remove(5)
# print(l)    # [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]

# # pop() リストの末尾にある要素を取り出し、リストから削除する
# l.pop()
# print(l)    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# l_pop = l.pop()
# print(l_pop)    # 9 (l[-1]と同じ)

# # clear リストの要素をすべて削除
# l.clear()
# print(l)    # []

# # index(x) リストの中の値xを探してそのインデックスを返す
# index_l = l.index(9)
# print(index_l) # 9

# # count(x) リストの中に値xが何回出現するか階数を返す
# ll = [1, 2, 3, 1, 4, 5, 1, 6, 7, 8, 1, 9, 10, 1]
# cnt_ll = ll.count(1)
# print(cnt_ll)   # 5

# # sort(key, reverse) リストを昇順に並び替える
# l.sort(reverse=True)
# print(l)    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# l.sort()
# print(l)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # copy() リストの複製(浅いコピー)を返す
# copy_l = l.copy()
# print(copy_l)

# # random.shuffle(l) リストlの要素をランダムに並べ替える
# random.shuffle(l)
# print(l)
# # random.sample(l, len(l)) リストlの要素をランダムに並べ替えて新しいリストLを生成
# L = random.sample(l, len(l))
# print(L)

# # ============================================================
# # tuple 要素を変更できないリスト
# t = (0, 1, 2, 3, 4, 5)
# print(t[1])
# print(t[:3])
# l = list(t) # タプルをリストに変換
# print(l)
# l.extend(t) # リストの末尾にタプルを追加
# print(l)
# tt = tuple(l)   # リストをタプルに変換
# print(tt)

# ============================================================
# # ■集合型(set) 重複する値×  順序を付ける× 数学的な演算〇
# colors = {"blue", "red", "green", "yellow", "black"}    # setを生成
# print(colors)
# e = set()   # 空のsetを生成
# print(e)
# fruits = set({"orange", "apple", "grape", "peach", "pineapple", "banana"})  # set()でsetを生成(実はset()は不要)

# clrs1 = {"blue", "red", "green", "yellow", "black"}
# clrs2 = {"blue", "green", "black", "white", "purple", "brown"}
# clrs1_2 = clrs1 - clrs2 # clrs1とclrs2の差分をclrs1_2に代入
# clrs2_1 = clrs2 - clrs1 # clrs2とclrs1の差分をclrs2_1に代入
# print(f"clrs1 - clrs2 = {clrs1_2}")
# print(f"clrs2 - clrs1 = {clrs2_1}")
# print("white" in clrs1)
# print("white" in clrs2)
#
# clrs3 = clrs1 | clrs2   # clrs1 + clrs2
# print(clrs3)
# clrs4 = clrs1 & clrs2   # clrs1とclrs2の重複している要素
# print(clrs4)