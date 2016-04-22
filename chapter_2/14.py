#coding: utf-8
"""
14. 先頭からN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""
#Usage: python 14.py N filename

import sys

n = int(sys.argv[1])
f = open(sys.argv[2], "r")

for i in range(n):
	print f.readline().rstrip('\n')

"""
head -n 3 hightemp.txt
"""