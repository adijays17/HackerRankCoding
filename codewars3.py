def printer(num, limit):
    n = num
    while limit:
        pre = num[0]
        count = 1
        for each in n[1:]:
            if each == pre:
                count += 1
            else:
                print(str(count)+each)
        print(str(count)+each)
        n = n + str(count)+each
        limit -= 1

printer('12', 4)

