"""
ヒープソート
根のノードaのとき親ノードは（a+1）/2左の子ノードは2a+1右の子ノードは2a+2

ヒープ構造は以下の特性を持つ
・二分木の根には必ず最大値がくる。
・親子関係、すなわちＮ［ａ］・Ｎ［２ａ＋１］・Ｎ［２ａ＋２］の値を比較したとき、必ず親であるＮ［ａ］の値が最大となる。

"""

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# ヒープを構成（親ノードを子ノードより大きい値に並び替え）
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2]
        j = (j - 1) // 2

print("ヒープ構造は",data)
# ソートを実行
for i in range(len(data), 0, -1):  # 最下ノードから繰り返し
    # ヒープの先頭と交換
    data[i - 1], data[0] = data[0], data[i - 1]
    j = 0  # ヒープの先頭から開始
    while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1])) \
            or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])):

        if (2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2]):

            # 左下と交換
            data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
            # 左下に移動
            j = 2 * j + 1
        else:
            # 右下と交換
            data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
            # 右下に移動
            j = 2 * j + 2
print(data)
