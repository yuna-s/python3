import re

list1 = []

str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
strlst = [i for i in re.split(r'\s|"|,|\.', str1) if not (i == '')]
words_index = {}#連想配列

for i, word in enumerate(strlst):
    n = i + 1
    l = 1 if n in (1, 5, 6, 7, 8, 9, 15, 16, 19) else 2
    words_index[word[:l]] = n
    #配列に要素を追加
    #words_index.setdefault(word[:l], n)
    #enumerate() インデックス付きループ

print(words_index)
#配列内の要素の番号は記録されないため適当に出力される

words_index.clear()#全部消す
print(words_index)
