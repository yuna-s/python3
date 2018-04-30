#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import re

list1=[]

str1 = "Now I need a drink, alcoholic of course, after \" the heavy lectures involving quantum mechanics."
strlst = [i for i in re.split(r'\s|"|,|\.', str1) if not (i == '')]
#re.split('\s.', str1) こういうふうに区切りたい文字を並べただけではうまく区切れない

for char1 in strlst:
    count = len(char1)
    moji = str(count)
    list1.append(moji)
    #print(str(moji), end="")改行なしprint
    #特に意味はなくstrにしてみた
print(list1)

#r'...' --> raw文字列
#not 条件式
