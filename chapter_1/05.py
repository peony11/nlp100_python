"""
05. n-gram

与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
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
    sentence = "I am an NLPer"
    print ngram(sentence, 2, "word")
    print ngram(sentence, 2, "char")
