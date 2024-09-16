# Exercício guiado - Calculadora - Parte 1

"""Calculadora while  """
condicao = True

while condicao:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    numeros_validos = None # FLAG

    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)

        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Algum número é invalido.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = ', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = ', numero_1_float - numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} = ', numero_1_float * numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = ', numero_1_float / numero_2_float)
    else:
        print('ué')

    sair = input('Caso queira sair digite sim: ').lower().startswith('s')

    if sair is True:
        condicao = False 