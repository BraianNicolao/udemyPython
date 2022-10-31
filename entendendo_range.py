"""
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loop for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

#Forma 1:
range(valor_de_parada)

Exemplo:

# Forma 1
for num in range(11):
    print(num)
OBS: Valor de parada não inclusivel. (início da parada 0, e passo de 1 em 1).

# Forma 2
range(valor_de_inicio, valor_de_parada)

for num in range(4, 11):
    print(num)

OBS: Valor de parada não inclusivel. (início da parada especificada pelo usuário, e passo de 1 em 1).

# Forma 3
for num in range(1, 10, 2):
    print(num)

range(valor_de_inicio, valor_de_parada, passo)
OBS: Valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário).

# Forma 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)

# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)

OBS: Valor_de_parada não inclusive (valor_final início especificado pelo usuário, e passo especificado pelo usuário).
"""






