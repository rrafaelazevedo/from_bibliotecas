'''nascimento = int(input('Ano de nascimento: '))
ano = int(input('Digite o ano atual: '))
idade = ano - nascimento
if idade < 18:
    print('Fique atento, a data de alistamento está próxima.')
elif idade == 18:
    print('É hora de se alistar, não perca o prazo.')
elif idade > 18:
    print('Ultrapassou a data de alistamento.')'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta(m) {} ano(s) para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))