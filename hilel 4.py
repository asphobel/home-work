xxx = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]


def lissst(list1):
    lis2= list1.copy()
    # for i in sorted(list1):
    for i in lis2:
        if i < 21:
            list1.remove(i)
        elif i > 74:
            list1.remove(i)
    return list1

print(lissst(xxx))
