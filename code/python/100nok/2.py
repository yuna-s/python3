str1="パトカー"
str2="タクシー"
print(''.join([char1 + char2 for char1, char2 in zip(str1, str2)]))
#print(','.join(文字列のリスト))　--> リストの要素1, リストの要素2, ...

l = [2017, 12, 31]
s = '-'.join([str(n) for n in l])
print(s)
#2017-12-31
#はじめ変数名をstrにしていたら怒られた。関数名とかぶると怒られるら
