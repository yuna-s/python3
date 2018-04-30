#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力

def cipher(str1):
    if str1.islower():
        for char in str1:
            strInt=219-ord(char)
            str2=chr(strInt)
            print(str2, end="")
    else:
        print(str1, end="")
    print()

str1=input()
cipher(str1)
