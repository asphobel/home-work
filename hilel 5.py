



def ff():
    while True:
        input_ = input("Введіть свій вік \t")
        result = ''
        try:
          t_ = int(input_)
        except:
          result += "An exception occurred"
        if t_ < 7:
            result += f"Тобі ж {t_} років! Де твої батьки?\n"
        elif 7 <= t_ <= 16:
            result += f"Тобі лише {t_} років, а це е фільм для дорослих!\n"
        elif 16 < t_ <65:
            result += f"Незважаючи на те, що вам {t_} рік, білетів всеодно нема!\n"
        if input_ == input_[::-1] :
            result += f"О, вам {t_} років! Який цікавий вік!\n"
        elif t_ >= 65:
            result += f"Вам {t_} рік? Покажіть пенсійне посвідчення!\n"
        print(result)
        qw = input("повторити виконання? ")
        if qw == 'No':
            break
        return result

print(ff())