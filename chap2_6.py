# =============================================
# whileで繰り返し構文 -p70
# energy = 10
# while energy > 0:
#     print("+ keep running")
#     print(f"| energy = {energy}")
#     energy -= 1 # energyを2消費する
# else:
#     print("└ stop.....")

# =============================================
# breakするまで坪数を調べる -p73
# while True:
#     tsubo = input("坪数を入力 > ")
#     if tsubo == "" or float(tsubo) <= 0: break  # 入力が0以下か入力がなかった場合はbreak
#     tsubo = float(tsubo)
#     m2 = round(tsubo * 3.31, 1)
#     print(f"{tsubo}坪は{m2}㎡です")

# =============================================
# forで繰り返し構文 -p74
# for i in range(10):
#     print(i)

# v = 0
# for i in range(1, 11):
#     v = v + i
#     print(f"{i}を足すと{v}")
# print(f'1から10を足すと...{v}')
#
# # 画面に300本の線を引く -p75
# グラフィックライブラリを取り込む
# from tkinter import *
# # 画面の初期化
# w = Canvas(Tk(), width=900, height=400)
# w.pack()
# # 同じ色の線をたくさん引く
# for i in range(300):
#     x = i * 3
#     w.create_line(x, 0, x, 400, fill="#cccccc")
# mainloop()

# =============================================
# 赤と青の線を交互に引く -p77
# for i in range(100):
#     x = i * 9
#     if i % 2 == 0:
#         c = "#0000FF"
#     else:
#         c = "#FF0000"
#     w.create_line(x, 0, x, 400, fill=c)
# mainloop()

# # continue -p79
# for i in range(5):
#     print(f"i = {i}")
#     if i >= 3: continue
#     print("- hello!")

# FizzBuzzGame -p80
# 3の倍数の時はFizz、5の倍数の時はBuzz、両方の倍数の時はFizzBuzzと言う
# for i in range(1, 100):
#     if i % 15 == 0:
#         print("FizzBuzz")
#         continue
#     if i % 5 == 0:
#         print("Buzz")
#         continue
#     if i % 3 == 0:
#         print("Fizz")
#     print(i)

# =============================================
# for文でのelseの使い方 -p82
# foodstuff = ["banana", "apple", "orange", "strawberry", "mango"]
# for food in foodstuff:
#     if food == "mango":
#         print("食材の中にマンゴーがあります！")
#         break
#     # else:
#     #     print("食材の中にマンゴーはありません")

# =============================================
# for dir in dir(30):
#     print(dir)