import math
â = float(input('Digite um ângulo para calcular os valores do seno, cosseno e tangente: '))
senâ = math.sin(math.radians(â))
cosâ = math.cos(math.radians(â))
tanâ = math.tan(math.radians(â))
print('O valor do seno de {}º é {:.2f}, o cosseno vale {:.2f} e a tangente assume o valor de {:.2f}.'. format(â, senâ, cosâ, tanâ))