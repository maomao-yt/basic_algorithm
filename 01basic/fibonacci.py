"""
フィボナッチ数列
"""
n =int(input())

memo = {1: 1, 2: 1}#終了条件の値を入れる

def fibonacci(n):
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 2)+fibonacci(n - 1)
    return memo[n]


print(fibonacci(n))
