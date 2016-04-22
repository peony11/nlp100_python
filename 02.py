"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
text_a = u"パトカー"
text_b = u"タクシー"
text = ''
for a, b in zip(text_a, text_b):
    text += a + b
print text
