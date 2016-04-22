#coding: utf-8
"""
13. col1.txtとcol2.txtをマージ

12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

import sys

def main():
	col1 = open("col1.txt")
	col2 = open("col2.txt")
	out_f = open("col1_col2.txt", "w")
	
	for line in col1:
		out_f.write(line.rstrip('\n') + '\t' + col2.readline())
	
	col1.close()
	col2.close()
	out_f.close()

if __name__ == '__main__':
	main()

"""
paste col1.txt col2.txt > paste_col1_col2.txt
"""