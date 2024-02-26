import random

numero=random.randint(1,100)
if numero <= 20:
    print(f'{numero}, Você é nivel : iniciante')
elif 20 < numero <= 40:
    print(f'{numero}, voce é nivel : mediano') 
elif 40 < numero <= 60:
    print(f'{numero}, voce é nivel : bom')  
elif 60 < numero <= 80:
    print(f'{numero}, voce é nivel : extremamente bom')
elif 80 < numero <= 100:
    print(f'{numero}, voce é nivel : um dos melhores, quase um Deus')