"""
1から100までの数を出力するプログラムを作成しなさい。
ただし、3の倍数の時「Fizz」、5の倍数の時「Buzz」、3と5の両方の倍数の時は「FizzBuzz」と出力すること。
"""
for i in range(1, 101):
    # 3と5の倍数の時
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    # 3の倍数の時
    elif i % 3 == 0:
        print("Fizz", end=" ")
    # 5の倍数の時
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
