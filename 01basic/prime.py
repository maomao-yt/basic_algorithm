"""
素数を判定する。
"""
import math

N = int(input())

# 素数列挙（高速）
# エラトステネスの篩
def get_prime(n):
    if n <= 1:
        return []
    prime = [2]  # 素数リスト
    limit = int(math.sqrt(n))  # 検索する上限を設定
    # 奇数リストを作成
    data = [i + 1 for i in range(2, n, 2)]
    while limit > data[0]:
        prime.append(data[0])
        #割り切れない数だけを取り出す
        data = [j for j in data if j % data[0] != 0]
    print(data)
    return prime + data


# 素数判定
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(get_prime(N))
print(is_prime(N))
