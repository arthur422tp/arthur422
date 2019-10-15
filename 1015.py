c = ["96182420","47464012","62781818"]
d = [['貳獎','參獎','肆獎','伍獎','陸獎'],["四萬元","一萬元","四千元","一千元","兩百元"]]
while True:
    user = input("發票號碼：")
    if user == "Quit":
        break
    if len(user) != 8:
        print("您的輸入不為發票形式")
        continue
    elif user == "45698621":
        print("你中了特別獎一千萬元")
    elif user == "19614436":
        print("你中了特獎兩百萬元")
    elif user in c:
        print("你中了頭獎二十萬元")
    else:
        n = 0
        while n < 5:
            n += 1
            for i in c:
                if user[n:] == i[n:]:
                    print("你中了{}{}".format(d[0][n-1],d[1][n-1]))
                    n = 10
                    break
        if n == 5:
            print("你沒有中獎")
print("感謝使用")
