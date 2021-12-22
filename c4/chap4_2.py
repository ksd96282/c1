# # # PyPIパッケージ
# # qrcodeをインストール
#
# # コマンドラインで以下を入力 ################
# # pip install pillow qrcode
# # pip install -U pip
# # #######################################
#
# import qrcode
# img = qrcode.make("http://kujirahand.com/")
# img.save("qrcode-test.png")

# # 暗号化ライブラリ「pycryptodome」
# # # コマンドラインで以下を入力 ################
# # pip install pycryptodome
# # # #######################################
# from Crypto.Cipher import AES
# import base64
#
# # 暗号化したいデータとパスワードを指定
# message = "自分がしてほしいと思うことを人にもするように"
# password = "password"
# iv = "jofw43483j$R#Rq3".encode("utf-8")  # 適当な初期ベクトル
# # iv = "L3f4mlTJtCIPV9af".encode("utf-8")  # 適当な初期ベクトル
# mode = AES.MODE_CBC                      # 暗号化モードを指定
#
# # 特定の長さの売位数にするため空白でデータを埋める関数
# def mkpad(s, size):
#     s = s.encode("utf-8")                # utf-8文字列をバイト列に変換する
#     pad = b' ' * (size - len(s) % size)  # 特定の長さの倍数にするための空白を生成
#     return s + pad
#
# # 暗号化する
# def encrypt(pw, data):
#     # 特定の長さに調節する
#     pw = mkpad(pw, 16)[:16]
#     data = mkpad(data, 16)
#     # pw = pw[:16]
#     # 暗号化
#     aes = AES.new(pw, mode, iv)
#     data_cipher = aes.encrypt(data)
#     return base64.b64encode(data_cipher).decode("utf-8")
#
# # 複合化する
# def decrypt(pw, encdata):
#     # パスワードの文字数を調節
#     pw = mkpad(pw, 16)[:16]
#     # pw = pw[:16]
#     # 複合化
#     aes = AES.new(pw, mode, iv)
#     encdata = base64.b64decode(encdata)
#     data = aes.decrypt(encdata)
#     return data.decode("utf-8")
#
# # 暗号化する
# enc = encrypt(password, message)
# # 複合化する
# dec = decrypt(password, enc)
# # 結果を表示する
# print(fi"暗号化: {enc}")
# print(fi"複合化: {dec}")
