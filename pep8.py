"""
PEP 8 - Python Enchancenmt Proposal
São propostas de melhorias para a línguagem Python
The Zen  of Python
import this
A ideia da PEP 8  é que as pessoas possam escrever código Python de forma Pythônica.
[1] - Utilize Camel Case para nomes de Classes;
[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;



class Calculadora:
    pass


class CalculadoraCientifica:
    pass


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação! Não utilize tab!
if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
-Métodos dentro de uma classe devem ser separados com uma única linha em branco;

class Class:
    pass


class Outra:
    pass

[5] - Import
- Impors devem ser sempre em linhas separadas;

# Import Errado

import sys, os

# import Certo
import sys
import os

# Não tem problema em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de uma mesmo pacote, recomenda-se fazer:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

# Import devem ser colcoados no topo do arquivo, recomenda-se fazer:
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções
- Não faça
function(algo[ 1 ], { outro: 2 } )

- Faça
function(algo[1], {outro:2})
"""


