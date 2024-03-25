lugat = {
    'olma': 'apple',
    'gilos': 'cherry',
    'nok': 'pear'
}

lugat2 = {
    'apple': 'olma',
    'cherry': 'gilos',
    'pear': "nok"
}

choice = int(input('ingiliz-uzbek (1)\nuzbek-ingliz (2)\n>>>'))
suz = input('suz kiritish: ')

if choice == 1:
    print(lugat2[suz])
elif choice == 2:
    print(lugat[suz])
else:
    print('notugri')
