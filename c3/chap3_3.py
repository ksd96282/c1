# 文字列の操作
# # ###########################################
# # 文字列の抽出
# s1 = "abcde"
# print(s1[0])
# s2 = "0123456789"
# print(s2[2:8])

# # ###########################################
# # 文字列の分割
# s1 = "This is a pen."
# print(s1)
# print("スペースで分割: ", s1.split())
#
# s2 = "2021/12/13"
# print("/で分割: ", s2.split("/"))
# print("/で1度だけ分割: ", s2.split("/",maxsplit=1))
#
# # 文字列の結合
# s2_splitted = s2.split("/")
# print("分割した文字列を別の文字(-)で結合: ", "-".join(s2_splitted))
#
# # 文字列の置換
# print("/を=に置換", s2.replace("/", "="))
# print("/を一度だけ=に置換", s2.replace("/", "=",1))