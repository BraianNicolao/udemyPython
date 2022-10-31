"""
Tipo de String
Em Python, um dado é considerado do tipo string sempre que:

-Estiver entre àspas  simples -> 'uma string', '234' , 'a', 'True','42.3'
-Estiver entre àspas duplas -> "uma string", "234" , "a", "True","42.3"
-Estiver entre àspas simples tripas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""

# Estiver entre às aspas dupla trplas -> """uma string""",  """234""", """a""", """True""", """42,3"""
"""
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

print(nome.upper())
print(nome.lower())
print(nome.split()) # Transforma em uma lista de string

print(nome[0:4]) # Slice de tring
print(nome[5:15]) # Slice de tring

# [ 0, 1]
# ['Geek', 'University']
print(nome.split()[0])
print(nome.split()[1])

"""

#nome = """Angelina
#Jolie"""
#print(nome)
#print(type(nome))

nome = 'Geek University'

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta.
"""
print(nome[::-1])

print(nome.replace('e', 'i'))

print(type(nome))

texto ='socorram me subino onibus em marrocos' # Palindromo
print(texto)

print(texto[::-1])

nome = 'ana' # Palindromo
print(nome)

print(nome[::-1])
