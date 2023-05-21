import random

numeros_sorteio = random.sample(range(1, 10), 15)

print("Números sorteados:")
for numero in numeros_sorteio:
    print(numero)
