def mkStr(x,y,z):
    return "{0}時の{1}は{2}".format(x,y,z)
#format関数を使えば方に関係なく埋め込みができる

if __name__=="__main__":
    print(mkStr(12,"気温",22.4))


"""
def tenpre(x, y, z):
    print("{0}時の{1}は{2}".format(x, y, z))
    #12時の気温は22.4

tenpre(12, "気温", 22.4)
"""
