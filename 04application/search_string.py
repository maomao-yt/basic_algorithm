"""
力任せ法
一致している場合は、1文字ずつ追加しながら比較する
一致しない場合は、1文字ずらして改めて比較する
"""

text = list('SHOEISHA SESHOP')#文字列をリストに変換
pattern = list('SHA')#確認したい文字列

for i in range(len(text)):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
            break
    if match:#一致していれば最初の位置を返す
        print(i)
        break
