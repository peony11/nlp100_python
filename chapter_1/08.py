"""
08. 暗号文

与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力

この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""
def cipher(text):
    """
    Input: text(str)
    Output: str
    """
    res = []
    for c in text:
        if c.isalpha() and c.islower():
            res.append(chr(219 - ord(c)))
        else:
            res.append(c)
    return "".join(res)

if __name__ == '__main__':
    print cipher("aAAabcDd")
    print cipher(cipher("aAAabcDd"))
