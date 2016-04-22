# coding: UTF-8
"""
11. タブをスペースに置換

タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""
import sys, re

def tab2space(file, filename):
	#Input: file, filename(str)
	out_f = open("tab2space_" + filename, "w")
	for line in file:
		out_f.write(re.sub('\t', ' ', line))
	out_f.close()
	
def main():
	filename = sys.argv[1]
	f = open(filename)
	print tab2space(f, filename)
	f.close()

if __name__ == '__main__':
	main()

"""
sed -e "s/\t/ /g" hightemp.txt > hightemp_t2s_sed.txt
cat hightemp.txt | tr "\t" " " > hightemp_t2s_tr.txt
expand -t 1 hightemp.txt > hightemp_t2s_expand.txt
"""
