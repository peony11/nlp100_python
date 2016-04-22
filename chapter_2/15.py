#coding: utf-8
"""
15. 末尾のN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""
#Usage: python 15.py N filename

import sys

def line_counter(file):
    cnt = 0
    for line in file:
        cnt += 1
    return cnt

n = int(sys.argv[1])
f = open(sys.argv[2], "r")

head_line = line_counter(f) - n

f.seek(0, 0) #ファイルの現在位置を初期位置にもどす

while head_line > 0:
	f.readline()
	head_line -= 1

while n > 0:
	print f.readline().rstrip('\n')
	n -= 1

"""
tail -n 3 hightemp.txt
"""