#coding: utf-8
"""
17. １列目の文字列の異なり

1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

#Usage: python 17.py filename

import sys

f_in = open(sys.argv[1], "r")
set_char = set()

for line in f_in:
	char = line.split()
	set_char.add(char[0])

sorted_set = sorted(list(set_char))

for n in sorted_set:
	print n

"""
sort hightemp.txt | cut -f 1 | uniq
"""