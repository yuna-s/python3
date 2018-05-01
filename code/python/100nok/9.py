# coding: utf-8
import re
import random

str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result = []
strlst = [i for i in re.split(r'\s|"|,|\.', str1) if not (i == '')]

for word in strlst:
    length = len(word)
    if length > 4:
        wordlist = list(word[1:length-1])
        #先頭と末尾を除いた単語のリストを作る
        wordlist = random.sample(wordlist, length-2)
        #random.shuffle(list)だと文字列はNoneになるから、文字列をピックアップして指定した長さのリストを返す関数をみつけた
        wordlist = [word[0]]+wordlist+[word[(length-1)]]
        word = "".join(wordlist)

    result.append(word)

result = " ".join(result)

print(result)
