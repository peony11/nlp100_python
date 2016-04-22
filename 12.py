#encoding: utf-8
"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存

各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""
import sys
def cut_columns(file, col1, col2):
	#input: file, col1(file), col2(file)
	for line in file:
		cols = line.split('\t')
		col1.write(cols[0] + '\n')
		col2.write(cols[1] + '\n')

def main():
	f = open(sys.argv[1])
	col1 = open("col1.txt", "w")
	col2 = open("col2.txt", "w")
	print cut_columns(f, col1, col2)
	f.close()
	col1.close()
	col2.close()

if __name__ == '__main__':
	main()