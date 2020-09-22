"""
基数を変換するプログラム
2進数を変換
"""
N = input()

ans = 0
for i in range(len(N)):
    ans += int(N[i]) * (2 ** (len(N) - i - 1))

print(ans)
