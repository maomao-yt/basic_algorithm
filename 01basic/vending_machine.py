"""
金額を入れて商品を購入した時のおつりを紙幣、硬貨で最小の数を求めなさい。
(不適切な入力に対応)
"""
import sys

insert_price = input("insert: ")
# 数値判定
if not insert_price.isdecimal():
    print("整数で入力してください")
    sys.exit()  # 強制終了

product_price = input("product: ")
# 数値判定
if not product_price.isdecimal():
    print("整数で入力してください")
    sys.exit()

change = int(insert_price) - int(product_price)

if change < 0:
    print("金額が不足しています。")
    sys.exit()

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i  # 枚数
    change %= i  # 残額
    print(str(i) + ":" + str(r) + "枚")
