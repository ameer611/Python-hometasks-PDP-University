def update_dict(dict1, dict2, dict3):
    dict1.update(dict2)
    dict3.update(dict1)
    return dict3

dict_1 = {
    'salom1': 1,
    "men1" : 6,
    'ular1': 4,
    'u1': 7,
    'lor1': 15,
    'ola1': 2,
    'mjuh1': 0,
    'fghjk1': 10,
    'vbn1': 3
}

dict_2 = {
    'salom2': 1,
    "men2" : 6,
    'ular2': 4,
    'u2': 7,
    'lor2': 15,
    'ola2': 2,
    'mjuh2': 0,
    'fghjk2': 10,
    'vbn2': 3
}

dict_3 = {
    'salom3': 1,
    "men3" : 6,
    'ular3': 4,
    'u3': 7,
    'lor3': 15,
    'ola3': 2,
    'mjuh3': 0,
    'fghjk3': 10,
    'vbn3': 3
}
print(update_dict(dict_1, dict_2, dict_3))