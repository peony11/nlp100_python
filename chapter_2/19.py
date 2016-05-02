#coding: utf-8
"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

#Usage: python 19.py filename

import sys

def first_row_list(file):
	return [line.split('\t')[0] for line in file]

def count_frequency(li):
	s = set(li)
	d = {x:0 for x in s}
	for text in li:
		d[text] += 1
	return sorted(d.items(), key=lambda x:x[1])

f_in = open(sys.argv[1], "r")
li = first_row_list(f_in)
f_in.close()

print "count", "col1"
for k,v in count_frequency(li)[::-1]:
	print v, k

	"""
	cut -f 1 hightemp.txt | sort | uniq -c | sort -r
	"""