"""
二分探索
"""


def binary_search(data, value):
    left = 0  # 探索する範囲の左端を設定
    right = len(data) - 1  # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は左端の位置を変える
            left = mid + 1
        else:
            # 中央の値より大きい場合は右端の位置を変える
            right = mid - 1
    return -1


data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 40))
