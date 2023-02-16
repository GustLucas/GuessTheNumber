import random 

print('-='*10)
print('ADIVINHE O NÚMERO')
print('-='*10)

maximo = int(input('Até quanto?  '))

numero = random.randint(1, maximo)
tentativa = 0
cont = 0

print(f'Estou pensando em número de 1 até {maximo}...')

while tentativa != numero:
    tentativa = int(input('Qual o seu chute? '))
    if tentativa < 1 or tentativa > maximo:
        print(f'O número precisa estar entre 1 e {maximo}') 
    
    else:
        cont += 1

        if tentativa > numero:
            print('Menos!')

        elif tentativa < numero:
            print('Mais!')

        else:
            print(f'Parabéns! Você acertou o número em {cont} tentativas.')
    
    print()


