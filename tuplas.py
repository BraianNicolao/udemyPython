"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:
1 - Tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis. Isso significa que ao se criar uma tupla ela não muda. Toda operaçãoem uma tupla gera
# uma nova tupla.

print(type(())) # Tupla
print(type([])) # List

# DEFINIÇÃO DE UMA TUPLA;

# CRUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

# Criada uma tupla sem (), mas no momento da impressão é adicionado ()
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com um elemento.
tupla3 = (4) # Não é uma tupla, para o Python é considerado um Int
print(tupla3)
print(type(tupla3))

tupla4 = (4, ) # Isso para o Python é uma tupla.
print(tupla4)
print(type(4))

tupla5 = 4, #Por definição tupla é por vírgula e não parentese.
print(tupla5)
print(type(tupla5))

# Conclusão: Podemos concluir que Tuplas são definidas pela vírgula e não pelo uso do parenteses.

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera error (ValueError) se colocarmos um número diferente de elementos para desenpacotar.
# Métodos para: Adição, remoção de elementos nas tuplas não existem, dado o fato das tupla serem imutáveis.

# Soma, valor máximo, valor minimo e tamanho.

# Se os valores forem inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print((max(tupla)))
print(min(tupla))
print(len(tupla))
"""

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)











