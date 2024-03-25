#  s va s0 satrlar berilgan. s satrdan s0 satr bilan ustma-ust tushuvchi 1-qism satr o‘chirilsin. Agar
# s satrda s0 satr topilmasa s satr o‘zgarishsiz chop etilsin.

s= 'uny'
s0 = 'dunyo'

if s in s0:
    print(s0.replace(s))
else:
    print(s0)