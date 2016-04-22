#coding: utf-8
"""
06. 集合

"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
def ngram(seq, n, unit="word"):
    """
    Input: seq(str), n(int), unit("word" or "unit")
    Output: set of tuples
    """
    res = set()
    if unit == "word":
        words = seq.split(" ")
        for i in range(len(words)-n+1):
            res.add(tuple(words[i:i+n]))
    if unit == "char":
        for i in range(len(seq)-n+1):
            res.add(tuple(seq[i:i+n]))
    return res

if __name__ == '__main__':
    text1 = "paraparaparadise"
    text2 = "paragraph"
    X = ngram(text1, 2, "char")
    Y = ngram(text2, 2, "char")
    
    print "XとYの和集合"
    print X.union(Y)
    print "XとYの積集合"
    print X.intersection(Y)
    print "XとYの差集合"
    print X.symmetric_difference(Y)
    
    print "'se'というbi-gramがXに含まれるかどうか"
    print ('s','e') in X
    print "'se'というbi-gramがYに含まれるかどうか"
    print ('s','e') in Y
    
