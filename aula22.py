#  Operador Lógico "or"
# Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha = int(senha_digitada)

senha_permitida = 123456

if (entrada == 'E' or entrada == 'e') and senha_permitida == senha:
    print('Entrar.')
else:
    print('Sair.')
