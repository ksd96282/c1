# モジュール


# datetime
import datetime

# print(datetime.date.today())            # 今日の日付を取得
# t1 = datetime.datetime.now()            # 今日の日付と現在時刻を取得
# print(t1.strftime("%Y/%m/%d %H:%M:%S")) # 現在時刻をフォーマットを指定して表示
# print(datetime.date(2021,12,21))        # 特定の日付を指定する
# t2 = datetime.date(2021, 12, 21)        # 変数に日付を代入
# print(t2 + datetime.timedelta(weeks=1)) # 1週間後を計算
# print(t2 - datetime.timedelta(days=3))  # 3日前を計算
# t3 = datetime.date(2006, 12, 21)        # 日付の差を計算
# print(t2 - t3)

# # 東京オリンピックの開催日
# t4 = datetime.date(2021, 7, 24)
# t5 = datetime.date.today()
# diff = t5 - t4
# print("東京オリンピック開催日： ", t4.strftime("%Y/%m/%d"))
# print("今日： ", t5.strftime("%Y/%m/%d"))
# print(fi"今日で{diff.days}日経過")

# # 標準モジュールと自作モジュールの優先度
# import math
# print(math.pi)    # 標準モジュールが優先される