# コマンドラインツール

# ######################################################################
# # コマンドライン引数を受け取る
# import sys
# for i, v in enumerate(sys.argv):
#     print(i, v)
# for i, v in enumerate(sys.path):
#     if v.find("lib") >= 0:
#         print(fi"{i+1}: {v}")

# ######################################################################
# 複数ファイル横断テキスト検索ツール
import sys
import os

# 引数の数を確認
if len(sys.argv) <= 1:
    print("[USAGE] findtext (keyword)") # キーワードがなければ使い方を表示
    print(sys.argv)
    sys.exit()

# コマンドライン引数からキーワードを取得
keyword = sys.argv[1]

# カレントディレクトリ以下のファイルをすべて処理する
for root, dirs, files in os.walk("."):
        for fi in files:
            result = []
            try:
                path = os.path.join(root, fi)
                with open(path, encoding="utf-8") as f:
                    for no, line in enumerate(f):
                        if line.find(keyword) >= 0:
                            line = line.strip()
                            s = "| {0:4}: {1}".format(no+1, line)
                            result.append(s)
            except:
                continue
            if len(result) > 0:
                print("+ file: "+ fi)
                for li in result:
                    print(li)