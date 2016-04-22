"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""
def temp_sentence(x, y, z):
    return "%s時の%sは%s"%(x, y, z)

if __name__ == '__main__':
    print temp_sentence(12, "気温", 22.4)
