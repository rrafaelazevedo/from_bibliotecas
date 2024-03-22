from random import shuffle
a1 = str(input('Preencha o nome completo pra chamada: '))
a2 = str(input('Preencha o nome completo pra chamada: '))
a3 = str(input('Preencha o nome completo pra chamada: '))
a4 = str(input('Preencha o nome completo pra chamada: '))
an = [a1, a2, a3, a4]
shuffle(an)
print('A ordem de apresentação dos trabalhos, será {}.'.format(an))