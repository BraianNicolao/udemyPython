"""
Escopo de variaveis

[                  ]

Dois casos de escopos:
1 - Variáveis Globais.
    São reconhecidas, seu escopo reconhece todo o programa

2- Variáveis Locais.
    São reconhecidas, apenas no bloco onde foram declaradas, seu escopo está limitado
    no bloco que foram declaradas

Python é uma linguagem de tipagem dinámica. Isso significa que ao declarar uma variável, nós não colocamos
o tipo de dado dela. Esse tipo é inferido ao atribuir o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))