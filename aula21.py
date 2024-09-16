# Operador Lógico "and"
# Ao usar o and, todas as condições precisam ser verdadeiras.
# None um valor nao existente
#Avaliação de curto circuito
print(True and False and True)
print(bool(0))
print(bool(0.0))
print(bool(''))


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha = int(senha_digitada)

senha_permitida = 123456

if entrada == 'E' and senha_permitida == senha:
    print('Entrar.')
else: 
    print('Sair.')

