import random

numero_aleatorio = random.randint(1, 100)

tentativa = 0
while True:
    tentativa_usuario= int(input('faça sua tentativa: '))
    tentativa = tentativa + 1
    if tentativa_usuario == numero_aleatorio:
        print(f"Parabéns, você venceu em {tentativa}")
        break
    elif tentativa_usuario < numero_aleatorio:
        print("Tente um numero maior!")
        
    else:
        print("Tente um numero menor")
        