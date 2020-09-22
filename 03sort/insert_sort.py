"""
挿入ソート
先頭はソート済みとする
後ろから移動する
"""
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
    temp = data[i]  # 追加する要素を一時的に別の変数に記録
    j = i - 1
    while (j >= 0) and (data[j] > temp):
        data[j + 1] = data[j]  # 要素を１つずつ後ろにずらす
        j -= 1
    data[j + 1] = temp # 一時的な領域から戻す

print(data)
