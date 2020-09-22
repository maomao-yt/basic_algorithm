"""
クイックソート
基準となるデータを選んで小さい方を左、大きい方を右に分割していき、最後に統合
再帰的に処理する

リスト内包表記でより簡潔に
"""

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]


def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]  # ピボットとしてリストの先頭を使用
    # ピボットより小さいものでリストを作成
    left = [i for i in data[1:] if i <= pivot]
    # ピボットより大きいものでリストを作成
    right = [i for i in data[1:] if i > pivot]

    left = quick_sort(left)
    right = quick_sort(right)
    # ソートされたものとピポットの値を合わせて返す
    return left + [pivot] + right


print(quick_sort(data))
