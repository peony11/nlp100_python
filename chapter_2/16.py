#coding: utf-8
"""
16. ファイルをN分割する

自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
#Usage: python 16.py N filename

import sys

N = int(sys.argv[1]) #the number of divisions
f_in = open(sys.argv[2], "r")

total_lines = 0 #the number of lines in the file
for line in f_in:
	total_lines += 1
f_in.seek(0, 0)#move cursol to the head

division_size = total_lines // N

if total_lines % N > 0:
	division_size += 1 

#output
for cnt in range(N):
	f_out = open("16_result-%d.txt" % (cnt+1), "w")
	line_cnt = division_size
	
	while line_cnt > 0:
		f_out.write(f_in.readline())
		line_cnt -= 1
	f_out.close()

f_in.close()

"""
split -l 5 hightemp.txt split_16.
"""