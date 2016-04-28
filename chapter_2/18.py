#coding: utf-8
"""
18. 各行を3コラム目の数値の降順にソート

各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

#Usage: python 18.py filename

import sys

def file2tuplelist(file):
	return [tuple(line.split('\t')) for line in file]


f_in = open(sys.argv[1], "r")
f_out = open("18_sorted_col3" , "w")

file_content = file2tuplelist(f_in)
f_in.close()

sorted_file = sorted(file_content, key=lambda x: x[2])

for line in sorted_file:
	f_out.write('\t'.join(line))

f_out.close()

"""
sort -k3 hightemp.txt 
"""