# (Parte 1) try e except para tratar exceções

try:
    a = 18
    b = 0
    print('Linha'[50])
    c = a / b[0]
except ZeroDivisionError:
    print('Dividiu por 0')
except NameError:
    print('informação não definida.')
except (TypeError, IndexError) as error:  # error: variavel que recebe a instancia do erro
    print('TypeError ou indexError.')
    print('Nome: ', error.__class__.__name__)
    print('Msg:', error)
except Exception as erro:
    print('ERRO DESCONHECIDO.')
    print('Nome: ', erro.__class__.__name__)
print('Continuar')
