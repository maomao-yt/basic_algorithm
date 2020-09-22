"""
3目並べ
ミニマックス法
評価値として勝てば1ポイント負ければー1ポイント引き分けなら0ポイント
"""

import random

goal = [
    0b111000000, 0b000111000, 0b000000111, 0b100100100,
    0b010010010, 0b001001001, 0b100010001, 0b001010100
]


# 3つ並んだか判定
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False


# ミニマックス法
def minmax(p1, p2, turn):
    if check(p2):
        if turn:
            return 1  # 自分の手番の時勝ち
        else:
            return -1  # 相手の手番の時負け

    board = p1 | p2
    if board == 0b111111111:  # 全ておいてあるならば引き分け
        return 0

    # おける場所を探す
    w = [i for i in range(9) if (board & (1 << i)) == 0]  # 左ビットシフト
    if turn:  # 自分の手番の時は最小値を選ぶ
        return min([minmax(p2, p1 | (1 << i), not turn) for i in w])
    else:  # 相手の手番の時は最大値を選ぶ
        return max([minmax(p2, p1 | (1 << i), not turn) for i in w])


# 交互に置く
def play(p1, p2, turn):
    if check(p2):  # ３つ並んでいたら終了
        print([bin(p1), bin(p2)])
        return

    board = p1 | p2
    if board == 0b111111111:  # 全ておいてあるならば
        print([bin(p1), bin(p2)])
        return

    # おける場所を探す
    w = [i for i in range(9) if (board & (1 << i)) == 0]  # 左ビットシフト
    # 各場所に置いた時の評価値をとる
    r = [minmax(p2, p1 | (1 << i), True) for i in w]
    # 評価値が一番高い場所を取得する
    i = [i for i,x in enumerate(r) if x == max(r)]
    # ランダムに１つ選ぶ
    j = w[random.choice(i)]
    play(p2, p1 | (1 << j), not turn)


play(0, 0, True)
