# 4つの数字の組み合わせの配列を生成
# 4つのうちどれとどれがペアににあるか区別する
# 試合数が少ない人から優先的に入る
# すべてのペアの組み合わせが試合するまではペアは重複しない
# 生成するごとに違う結果になる

import random
import re
from itertools import combinations, product

# num_player = int(input("プレイヤー数 > "))
num_player = 5
# num_game = int(input("試合数 > "))
num_game = 4
num_game_total = num_player * num_game / 2  # 全試合数

player = []                 # プレイヤーNoのリスト
player_game_count = {}      # プレイヤーNoと残り試合数
for i in range(num_player):
    player.append(i + 1)
    player_game_count[i + 1] = num_game
comb = list(combinations(player, 2)); print(f"組み合わせの全パターン(重複なし)\n = {comb}")        # 組み合わせの全パターン
comb_exist = []; print(f"組み合わせ済みのパターン\n = {comb_exist}")        # 組み合わせの全パターン

# 全playerの残り試合数が0になるまで組み合わせを生成
done = False
while done:
    # 残り試合数の多いplayerを抽出
    player_pri = []
    for p, c in player_game_count.items():
        if c >= max(player_game_count.values()):
            player_pri.append(p)
    # if len(player_pri) < 4:

    # 残り試合数の多いplayerからランダムに2組のペアリングを生成
    paring1 = []
    paring2 = []
    paring = False
    while not paring:
        random.shuffle(player_pri)
        paring1 = [player_pri[0], player_pri[1]]; paring1_1 = [player_pri[1], player_pri[0]]
        paring2 = [player_pri[2], player_pri[3]]; paring2_2 = [player_pri[3], player_pri[2]]
        if (paring1 in comb_exist) and (paring1_1 in comb_exist):
            paring = False
        else:
            comb_exist.append(paring1)
            paring = True
        if (paring2 in comb_exist) and (paring2_2 in comb_exist):
            paring = False
        else:
            comb_exist.append(paring2)
            paring = True
    print(f"組み合わせ済みのパターン\n = {comb_exist}")        # 組み合わせの全パターン



# # ゲームマッチング
# matching_all = {}
# # def matching(i):
# for i in range(num_game_total):
#     make_match = False
#     while not make_match:
#         # プレイヤーをシャッフル
#         player = list(player_game_count.keys())
#         random.shuffle(player)
#         # 順番にマッチング
#         match = str(player[0]) + "-" + str(player[1])
#         confirm = str(player[1]) + "-" + str(player[0])
#         if (match in matching_all) or (confirm in matching_all):  # マッチングが重複していたら再度マッチング生成
#             make_match = False
#         else: # マッチングが重複していなかったらmatching_allに格納して次のマッチングを作成
#             matching_all[i] = match
#             player_game_count[player[0]] -= 1
#             player_game_count[player[1]] -= 1
#             make_match = True
#     # matching(i - 1)
# # matching(num_game_total)
# print(matching_all)
# print(player_game_count)
