"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
text1 = u"パトカー"
text2 = u"タクシー"
text = ''
for i in range(4):
    text += text1[i]
    text += text2[i]
print text
