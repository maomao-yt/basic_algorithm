"""
3目並べ
ビット演算で実装
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


# 交互に置く
def play(p1, p2):
    if check(p2):  # ３つ並んでいたら終了
        print([bin(p1), bin(p2)])
        return

    board = p1 | p2
    if board == 0b111111111:  # 全ておいてあるならば
        print([bin(p1), bin(p2)])
        return

    # おける場所を探す
    w = [i for i in range(9) if (board & (1 << i)) == 0] #左ビットシフト
    # ランダムにおいてみる
    r = random.choice(w)
    play(p2, p1 | (1 << r))  # 手番を入れ替えて次を探す#左ビットシフト


play(0, 0)
