"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    -not:

Operadores binários:
    -and, or, is:

Regras de Funcionamento:
Para o 'and' ambos os valores precisam ser True.
Para o 'or' um ou outro valor precisa ser True.
Para o 'not', o valor do booleano é invertido, ou seja se for True, se torna False e vise versa.
Para o 'is', o valor é comparado com um segundo.
"""

ativo = True
logado = True

if ativo and logado:
    print("Bem-Vindo usuário!")
else:
    print("Você precisa ativar a sua conta. Por favor, cheque seu e-mail.")

