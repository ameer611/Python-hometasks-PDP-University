dictionary = dict(b=1, g=9, r=10, a=95, s=0, d=5, y=4)

sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
print(sorted_dict)

