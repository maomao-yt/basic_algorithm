"""
基数を変換するプログラム
10→2進数
"""
N = int(input())

ans = ""
while N > 0:
    ans = str(N % 2) + ans
    N //= 2

print(ans)
