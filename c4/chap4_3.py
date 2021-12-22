# # ファイルの読み書き

# # ######################################################################
# # ファイルを読み込む関数
# def open_textfile(path):
#     file = open(path, encoding="utf-8")    # テキストファイルを開く
#     try:
#         stuff = file.read()       # ファイルを読み込んで内容を変数に代入する
#         print(stuff)
#         raise Exception("ファイルエラー")
#     except:
#         pass
#     finally:
#         file.close()              # ファイルを閉じる
#     return stuff
#
# # ファイルを書き込む関数
# def write_textfile(path, text):
#     file = open(path, mode="w", encoding="utf-8")
#     try:
#         file.write(text)
#         raise Exception("ファイルエラー")
#     except:
#         pass
#     finally:
#         file.close()

# # ######################################################################
# # ファイルを読み込む関数 (with構文)
# def open_textfile(path):
#     with open(path, encoding="utf-8") as file:   # テキストファイルを開く
#         stuff = file.read()       # ファイルを読み込んで内容を変数に代入する
#         print(stuff)
#     return stuff
#
# # ファイルを書き込む関数
# def write_textfile(path, text):
#     with open(path, mode="w", encoding="utf-8") as file:
#         file.write(text)
#
# open_textfile("Tomas.txt")
# open_textfile("mt7_7.txt")

# # ######################################################################
# # ファイルを1行ずつ読み込んで表示
# with open("mt7_7.txt", encoding="utf-8") as tf:
#     for line in tf:
#         print(line, end="")
#
# # ファイルを読み込んでキーワードが存在する行だけ表示
# key = "you"
# print(fi"キーワード'{key}'がある行だけ表示する")
# with open("mt7_7.txt", encoding="utf-8") as tf:
#     for i, line in enumerate(tf):
#         if line.find(key) >= 0:
#             print(fi"{i+1} : {line}", end="")

# ######################################################################
# pythonのオブジェクトや変数をJSON形式で保存する
import json
data = {
    "no": 5,
    "code": ("jas", 1, 9),
    "scr": "be quick to listen, slow to speak, slow to anger"
}
# ファイルに書き込み
file_name = "test.json"
with open(file_name, "w") as fp:
    json.dump(data, fp)     # JSON形式で保存
# ファイルから読み込み
with open(file_name, "r") as fp:
    r = json.load(fp)
    print(f"no = {r['no']}\n"
          f"code = {r['code']}\n"
          f"scr = {r['scr']}")
