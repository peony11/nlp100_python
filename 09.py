"""
09. Typoglycemia

スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""
import random
def typoglycemia(text):
    """
    Input: text(str)
    Output: str
    """
    words = text.split(" ")
    rslt = []
    for word in words:
        if len(word) <= 4:
            rslt.append(word)
        else:
            res = []
            middle = list(word[1:len(word)-1])
            random.shuffle(middle)
            res.append(word[0])
            res.extend(middle)
            res.append(word[-1])
            rslt.append("".join(res))
    return " ".join(rslt)

if __name__ == '__main__':
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print typoglycemia(text)
