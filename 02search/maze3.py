"""
迷路の探索（番兵）
深さ優先探索（右手法）
"""
maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 9, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
    [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
    [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
    [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

# 右手法での移動方向（下、右、上、左）をセット
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# スタート位置（ｘ座標、ｙ座標、移動回数、方向）をセット
x, y, depth, d = 1, 1, 0, 0

while maze[x][y] != 1:
    # 探索済みとしてセット
    maze[x][y] = 2

    # 右手法で探索
    for i in range(len(dir)):
        # 進行方向の右側から順に探す
        j = (d + i - 1) % len(dir)
        if maze[x + dir[j][0]][y + dir[j][1]] < 2:
            # 未訪問の場合は進めて移動回数を増やす
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break
        elif maze[x + dir[j][0]][y + dir[j][1]] == 2:
            # 訪問済みの場合は進めて表示回数を減らす
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break


print(depth)
