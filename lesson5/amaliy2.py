
bugun = input('Kunni kiriting: >>>')
oy = input('Oyni kiriting: >>>')
yil = input('Yilni kiriting: >>>')

mashina_raqami = input("Mashinangizni raqamini kiriting: >>>")

if not (int(bugun) < 0 or int(bugun) > 31) and not (int(oy) < 0) or (int(oy) > 12) and not (int(yil) < 2023):

    if int(bugun) % 2 == 0 and int(mashina_raqami) % 2 == 0:
        print("Siz bugun chiqa olasiz")
    elif int(bugun) % 2 == 1 and int(mashina_raqami) % 2 == 1:
        print("Siz bugun chiqa olasiz")
    else:
        print("Siz chiqa olmaysiz")

else:
    print('notugri kiritdingiz')

