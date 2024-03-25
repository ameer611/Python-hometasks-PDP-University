 # s va s0 satrlar berilgan. s satrda s0 satrning necha marta uchrashi aniqlansin.

s= 'uny'
s0 = 'dunyo'
counter = 0
while True:
    if s in s0:
        index_ = s0.index(s)

        counter += 1
    else:
        break

print(counter)