"""
Boyer-Moore法
文字列検索
末尾から比較し、一気にずらす
ずらす文字数はあらかじめ設定しておく
"""

text = list('SHOEISHA SESHOP')
pattern = list('SHA')

skip = {}
for i in range(len(pattern) - 1):
    skip[pattern[i]] = len(pattern) - i - 1#ずらす文字数をカウント

i = len(pattern) - 1
while i < len(text):
    match = True
    for j in range(len(pattern)):
        if text[i - j] != pattern[len(pattern) - 1 - j]:
            match = False
            break
    if match:
        print(i - len(pattern) + 1)
        break
    if text[i] in skip:
        i += skip[text[i]]#用意した数だけ位置をずらす
    else:
        i += len(pattern)#パターンの文字数だけ位置をすらす
