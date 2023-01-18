def kkk():
    while True:
        n = input("Введіть слово з буквой 'о': \t ")
        if "о" in n or "О" in n:
            return n

print(kkk())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if type(i) == str:
        lst2.append(i)
print(lst2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ddd():
    put = input('Hello my name is Orrlando BloomO')
    k = put.split(' ')
    l = 0
    for i in k:
        if i != '':
            if i[-1] == 'o' or i[-1] =='O':
                l += 1
    return l
print(ddd())
