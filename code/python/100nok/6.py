sentence1 = "paraparaparadise"
sentence2 = "paragraph"

#文字bi-gram
X = [sentence1[i:i+2] for i in range(len(sentence1)-1)]
Y = [sentence2[i:i+2] for i in range(len(sentence2)-1)]
X = set(X)
Y = set(Y)
print(X)
print(Y)

union = X|Y #AまたはBに含まれる
print(union)

inter = X&Y #AにもBにも含まれる
print(inter)

dif = X-Y #Aのみに含まれる
print(dif)

dif = Y-X #Bのみに含まれる
print(dif)

TF = {'se'} <= X
print(TF)

TF = {'se'} <= Y
print(TF)
