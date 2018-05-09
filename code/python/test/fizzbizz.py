import sys
#3:fizz 5:bizz 12
check_lst = []
length = len(sys.argv)
argv = sys.argv[1:length]
flag=0
#flag: Nが割り切れたら1

try:
    for i, word in enumerate(argv):
        if i == length-2:
            N = word
            N = int(N)
        else:
            strlst = word.split(":")
            check_lst.append(strlst)

    for check in check_lst:
        i = int(check[0])
        if N % i == 0:
            print("{0}".format(check[1]), end="")
            flag = 1

    if flag == 0:
        print("{0}".format(N))

    else:
        print("!")

except ValueError:
    print("pls type int")
    sys.exit()
    #整数以外のものが与えられたら終了
