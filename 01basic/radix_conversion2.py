"""
基数を変換するプログラム
10進数を変換
"""
N, base = map(int, input().split())


def convert(N, base):
    ans = ""
    while N > 0:
        ans = str(N % base) + ans
        N //= base
    return ans


print(convert(N, base))
