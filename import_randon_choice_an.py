import random
a1 = str(input('Preencha o nome completo pra chamada: '))
a2 = str(input('Preencha o nome completo pra chamada: '))
a3 = str(input('Preencha o nome completo pra chamada: '))
a4 = str(input('Preencha o nome completo pra chamada: '))
an = (a1, a2, a3, a4)
choice = random.choice(an)
print('Por gentileza {}, apague a lousa.'.format(choice))
