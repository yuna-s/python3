# coding: utf-8
N = 3
howline = input()
times=0

l = [input().split("=") for i in range(N)]#指定した行数分インプットしてリストで返す
l2 = [l[i][0] for i in range(N)]

max = len(max(l2,key=len))
for i in l2:
    length = len(i)
    if not length == max:
        if howline == "l":
            n = i+"."*(max-length)
            str = n+"="+l[times][1]
            print(str)
        elif howline == "r":
            n = "."*(max-length)+i
            str = n+"="+l[times][1]
            print(str)
        else:
            print("pls type l or r first")
    else:
        str = i+"="+l[times][1]
        print(str)


    times=times+1



"""
list(map(lambda x: x * 2, filter(lambda x: x % 3 == 1, range(1, 10))))


if howline == l:
    for i in varlst:
        strlen = len(i)
        if not strlen == maxVar:
s = [input() for i in range(3)] #指定した行数分インプットしてリストで返す
t = [int(input()) for i in range(3)] #複数行を数値型で取得
u = [input().split() for i in range(2)] #複数行の入力を分割して取得

if howline==r:


test = "orange,apple,banana,strawberry"
>>> test.split(",", 2) # 2回目までは区切って、３個目以降は区切らない。
['orange', 'apple', 'banana,strawberry']

l2=input()
print(l1+" "+l2)
l = list(range(3))
print(l)
# [0, 1, 2]

l.extend([100, 101, 102])
print(l)
# [0, 1, 2, 100, 101, 102]

l.extend((-1, -2, -3))
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3]
print(s)
print(t)
print(u)
print(s[0])
"""
