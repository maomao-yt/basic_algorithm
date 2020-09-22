"""
8クイーン問題
"""
N = 8
cnt = 0


# 盤面を可視化
def view_field(col):
    field = []
    # 2次元リストマップを作成
    for i in range(N):
        sub_field = []
        for j in range(N):
            sub_field.append(".")
        field.append(sub_field)

    # "Q"を埋めていく
    for y, x in enumerate(col):
        field[y][x] = "Q"

    # 盤面を可視化
    for lines in field:
        for char in lines:
            print(char, end="")
        print()  # 改行に対応


# 斜めをチェック
def check(x, col):
    # 配置済みの行を逆順に調べる
    for i, row in enumerate(reversed(col)):
        if (x + i + 1 == row) or (x - i - 1 == row):  # 左下と左上があるか
            return False
    return True


def search(col):
    global cnt
    if len(col) == N:  # 全て配置できれば出力
        cnt += 1
        print(cnt, col)
        # 可視化
        view_field(col)
        return

    for i in range(N):
        if i not in col:  # 同じ行は使わない
            if check(i, col):
                col.append(i)
                search(col)  # 再帰的に探索
                col.pop()  # リセット


search([])
