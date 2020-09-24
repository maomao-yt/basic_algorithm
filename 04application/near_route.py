"""
最短経路問題
動的計画法
"""
M, N = 6, 5

route = [[0 for i in range(N + 1) ]for j in range(M + 1)]

# 横方向の最初の1列をセット
for i in range(M + 1):
    route[i][0] = 1


for i in range(1, N + 1):
    # 縦方向の最初の1行をセット
    route[0][i] = 1
    for j in range(1, M + 1):
        # 左と下の値を加算する
        route[j][i] = route[j - 1][i] + route[j][i - 1]

for lines in route:
    for char in lines:
        print(char, end=" ")
    print()  # 改行に対応


print(route[M][N])
