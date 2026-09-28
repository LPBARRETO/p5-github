import random

valores = []

# Gera 15 números aleatórios entre 1 e 100
for i in range(15):
    n = random.randint(1, 100)
    valores.append(n)

print(f'Lista original: {valores}')

# Busca o primeiro número maior que 80
posicao = -1
indice = 0

while indice < len(valores):
    if valores[indice] > 80:
        posicao = indice
        break
    indice += 1

if posicao != -1:
    print(f'O primeiro número maior que 80 está no índice {posicao} (Valor: {valores[posicao]}).')
else:
    print('Não há números maiores que 80 nesta lista.')

# Ordena a lista em ordem decrescente
valores_decrescentes = sorted(valores, reverse=True)
print(f'Lista em ordem decrescente: {valores_decrescentes}')

# Separa a lista em duas categorias (>= 50 e < 50)
maiores_ou_iguais_50 = []
menores_50 = []

for num in valores_decrescentes:
    if num >= 50:
        maiores_ou_iguais_50.append(num)
    else:
        menores_50.append(num)

print(f'Valores da metade superior (>= 50): {maiores_ou_iguais_50}')
print(f'Valores da metade inferior (< 50): {menores_50}')

print(f'Total na metade superior: {len(maiores_ou_iguais_50)}')
print(f'Total na metade inferior: {len(menores_50)}')