def fatorial(numero):
    resultado = 1
    
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input('escolha um numero positivo: '))

if numero <= 0:
    print(f'Insira um numero positivo, o {numero} não é')
else:
  resultado_fatorial = fatorial(numero)
  print(f'A fatorial do {numero} é {resultado_fatorial}')