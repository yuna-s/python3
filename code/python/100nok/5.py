#n-gramとは --> 任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法
original = "I am an NLPer"

def ngram(input, n):
    last = len(input) - n + 1
    print(last)
    ret = []
    for i in range(last):
        ret.append(input[i:i+n])
    return ret

s=ngram(original, 2)              # 文字 n-gram
print(s)
original = original.split()
s=ngram(original, 2)              # 単語 n-gram
print(s)

"""
----努力のあとｗ----

print("pls type sequence")
sequence = input()
print("pls type n. ex: bi-gram --> 1")
n = input() #n-gram
n = int(n)
print("word or letter or both?")
period = input()

seqlst = [i for i in re.split(r'\s|"|,|\.|\[|\]', sequence) if not (i == '')]
print(seqlst)
#与えられたシーケンスを単語ごとに分解

if period == "word":
    print("yes!")
    cha = sequence[::n]
print(cha)
"""

def ngram2(sequence, n):
    length = len(sequence)-n+1
    result=[]
    for i in range(0, length):
        result.append(sequence[i:i+n])
    return result
