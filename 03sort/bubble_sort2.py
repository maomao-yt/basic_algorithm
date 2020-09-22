"""
バブルソート(改良)
隣同士を比較し小さい方を左に持ってくる
"""

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

change = True
for i in range(len(data)):
    if not change:  # 交換が発生していなければ終了
        break
    change = False  # 交換が発生していないものとする
    for j in range(len(data) - i - 1):  # ソート済みの部分以外でループ
        if data[j] > data[j + 1]:  # 前の方が大きいとき
            data[j], data[j + 1] = data[j + 1], data[j]
            change = True  # 交換が発生した

print(data)
