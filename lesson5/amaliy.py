from datetime import datetime as dt

bugun = dt.now()
bugun = bugun.day

mashina_raqami = int(input("Mashinangizni raqamini kiriting: >>>"))

if mashina_raqami > 99 and mashina_raqami < 1000:
    
    if bugun%2 == 0 and mashina_raqami%2 == 0:
        print("Siz bugun chiqa olasiz")
    elif bugun%2 == 1 and mashina_raqami%2 == 1:
        print("Siz bugun chiqa olasiz")
    else:
        print("Siz chiqa olmaysiz")

else:
    print("Siz noto'g'ri raqam kiritdingiz.")