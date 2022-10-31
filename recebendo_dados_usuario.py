"""
Recebendo dados do usuário:

input() -> Todo dado recebido via imput é do tipo String

Em Python, string é tudo que estiber entre:
- Aspas simples;
- Aspas duplas;
- Asplas simples triplas;
- aspas duplas triplas;

Exemplo:
- Aspas simples -> 'angelita'
- Aspas duplas -> "Roberto"
- Asplas simples triplas -> ''' 12459 '''
"""
# aspas duplas triplas ->  """ Bernador """

# Entrada de dados
#print("Qual é o seu nome?")
#nome= input() # Input -> Significa entrada

nome = input('\nQual seu nome? ')

#Exemplo de print - 'antigo'
#print('Seja bem-vindo (a) %s' % nome)

#Exemplo de print moderno - 3.x Python
#print('Seja Bem-Vindo(a) {0}'.format(nome))

#Exemplo de print mais modenor 3.7
print(f'Seja Bem-vindo(a) {nome}')

#print("Qual a sua idade? ")
#idade = input()

idade = int(input('\nQual a sua idade? '))

# Processamento

# Saída de dados
#Exemplo de print - 'antigo'
#print('A %s tem %s anos' % (nome, idade))
#As variáveis dentro do parêntese vão substituir a %s

#Exemplo de print moderno - 3.x Python
#print('A {0} tem {1}'.format(nome, idade))

#Exemplo de print mais modenor 3.7
print(f'\nA {nome} tem {idade} anos')
"""
 #int(idade) -> Cast
Cast é a conversão de um tipo de dado para outro.
"""
print(f'\nA {nome} nasceu em {2022 - idade}.')