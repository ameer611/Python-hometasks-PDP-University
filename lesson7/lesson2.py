sonBir = ['bir', 'ikki', 'uch', 'turt', 'besh', 'olti', 'yetti', 'sakkiz', 'tuqqiz']
sonOn = ["o'n", 'yigirma', 'uttiz', 'qirq', 'ellik', 'olmish', 'yetmish', 'sakson', 'tuqson']

son = int(input("son kiritish: "))
sonBirlik = son%10
sonOnlik = son//10

if son==0:
    print('nul')
elif son==100:
    print("yuz")
elif sonBirlik==0:
    print(sonOn[sonOnlik-1])
elif sonOnlik==0:
    print(sonBir[sonBirlik-1])
else:
    print(sonOn[sonOnlik - 1], sonBir[sonBirlik - 1])