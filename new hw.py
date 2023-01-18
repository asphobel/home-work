
def word(w):
    n = len(w)
    m = f"Word {w} has {n} letters"
    return m
print(word('Python'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def mmm():
    input_ = input("Введіть свій вік \t")
    result = ''
    try:
      t_ = int(input_)
    except:
      result += "An exception occurred"
    if t_ < 7:
        result += "Де твої батьки?"
    elif 7 <= t_ <= 16:
        result += "Це фільм для дорослих!"
    elif 16 < t_ <65:
        result += "А білетів вже немає!"
    if "7" in input_:
        result += "Вам сьогодні пощастить!"
    elif t_ >= 65:
        result += "Покажіть пенсійне посвідчення!"
    return result

print(mmm())