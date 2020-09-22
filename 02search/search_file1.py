"""
フォルダにあるファイルを探す
深さ優先探索
"""
import os


def search(dir, name):
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):  # 読み込み可能か
                search(dir + i + '/', name)


search('/', 'book')  # パス名、フォルダ名
