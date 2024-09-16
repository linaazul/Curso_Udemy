# Fatiamento de strings e a função len
# 012345678
# Olá Mundo
#-987654321

# Fatiamentos de string:
# fatiar [Inicio:Fim:Passo] [::]
# o passo pula os caracteres
#ao usar o passo com sinais negativos ele inverte a string
# a função len retorna a qtd de caracteres da str


variavel = 'Olá mundo'
print(variavel[5])

# Para pegar do começo de uma variavel e ir até o fim, eu informo o começo e omito o fim.
print(variavel[4:]) #mundo

# o Python geralmente exclui o ultimo indice entao se eu quiser pegar o final eu devo por um número a mais do que eu quero ir
print(variavel[4:8]) #mund -> para ir ate o d eu tive que por o ultimo indice como 8 sendo que o d é indice 7

#Ao omitir o começo, meu programa entende que ele deve pegar o começo
print(variavel[:3]) # Olá

#Testando len 
print(len(variavel))

print(variavel[::-1])
