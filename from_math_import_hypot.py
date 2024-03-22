'''catetoa = float(input('Digite o comprimento do cateto a: '))
catetob = float(input('Agora chegou a hora de inserir o comprimento do cateto b: '))
hipotenusa = (catetoa ** 2) + (catetob ** 2)
print('A soma do quadrado do cateto de lado {} com o quadrado do cateto de lado {} (catetoa + catetob)², resulta no quadrado da hipotenusa {}, e o lado (raíz) da hipotenusa vale {:.2f}.'.format(catetoa, catetob, hipotenusa, (hipotenusa**(1/2))))'''


from math import hypot
catetoa = float(input('Digite o comprimento do cateto a: '))
catetob = float(input('Digite o comprimento do cateto b: '))
hipotenusa = hypot(catetoa, catetob)
print('A soma do quadrado do cateto de lado {} com o quadrado do cateto de lado {} (cateboa + catebob)², resulta no quadrado da hipotenusa {:.2f}, e o lado da hipotenusa vale {:.2f}.'.format(catetoa, catetob, hipotenusa**2, hipotenusa))