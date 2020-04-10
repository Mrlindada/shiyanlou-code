a = 0
while a < 101:
    if a % 7 == 0:
        pass
    if a // 10 ==7:
        pass
    if a % 10 == 7:
        a = a + 1
        continue
    else:
        print(a,end=' ')
    a = a + 1

