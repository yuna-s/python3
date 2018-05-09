import sys
import codecs

"""
---main-test.txt---

#何掛何のマスか
5

#与えられる爆弾のマップ(1が爆弾)
00000
00010
00000
01100
00000
"""

#txtファイルの文字列からマップを読み込んでリストに
def knowMap(arg, map, flag):
    for line in codecs.open(arg, "r","utf-8"):
        if flag == 0:
            length = int(line)
            flag = 1
            print(length)
            l=length
        else:
            l = list(line.strip())
            if l == []:
                l = ['x']*length
            l = ['x']+l+['x']
            #strip() で文字を読み込んだ時の空白文字を削除できる

        if not l == []:
            map.append(l)
    map.append(['x']*(length+2))
    return map
    #map[y][x]

#地雷を確かめる
def checkMain(map):
    length = map.pop(0)
    count = 0
    for s in range(1, length+1):
        for t in range(1, length+1):
            if map[s][t] == '0':
                if map[(s-1)][(t-1)] == '1':
                    count = count+1
                if map[(s-1)][t] == '1':
                    count = count+1
                if map[s][(t-1)] == '1':
                    count = count+1
                if map[(s+1)][(t+1)] == '1':
                    count = count+1
                if map[(s+1)][t] == '1':
                    count = count+1
                if map[s][(t+1)] == '1':
                    count = count+1
                if map[(s-1)][(t+1)] == '1':
                    count = count+1
                if map[(s+1)][(t-1)] == '1':
                    count = count+1

                map[s][t] = count
                print(count)
                count = 0
    return map

#0-padding
def popX(map):
    newmap = []
    for maplst in map:
        list1 = [i for i in maplst if not i == 'x']
        if not list1 == []:
            newmap.append(list1)
    return newmap

if __name__ == '__main__':
    map = knowMap(sys.argv[1], [], 0)
    map = checkMain(map)
    newmap = popX(map)

    print(newmap)
