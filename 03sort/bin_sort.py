"""
ビンソート
１から９の数値を小さい方からリストの中にいくつあるか数を数えていく
"""

data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]

result =[0]*10
for i in data:
    result[i] += 1

for i in range(10):
    for j in range(result[i]):
        print(i,end =" ")