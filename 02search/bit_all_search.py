"""
ビット全探索
使いどころは、「2通りの選択肢がN個ある場合に全てのパターン探索」する場合
注意点としては、計算量が N * 2 ^ Nになるため、Nが多くなると計算時間が膨大となる
"""
sample_list = ['A', 'B', 'C', 'D']

## 要素数をカウント
len_sample_list = len(sample_list)

## 2 ** len_sample_listで選択する全パターンを探索
for i in range(2 ** len_sample_list):
    out_list = []
    ## どの桁が1になっているかをチェックするために2進数の各桁をループ
    for j in range(len_sample_list):
        ## i >> jで確認したい桁を一番右までずらして1と論理積をとって「選択」している要素を確認
        if (i >> j) & 1 == 1:
            out_list.append(sample_list[j])
    print(out_list)
