"""
フォルダにあるファイルを探す
幅優先探索
"""
import os

queue = ['C:/Users']

while len(queue) > 0:
    dir = queue.pop()
    for i in os.listdir(dir):
        if i == "Default":  # 探したいファイルorフォルダ名
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                queue.append(dir + i + ' / ')
