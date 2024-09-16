# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
print(not True)
print(not False)

senha = input("Digite a senha: ")
if not senha:
    print("Nada digitado")
else:
    print(senha)
