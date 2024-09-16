# try, except, else e finally + Built-in Exceptions
# o finally sempre será executado
try:
    print('ABRIR ARQUIVO')
    # 2/0
except ZeroDivisionError:
    print('Dividiu por 0.')
else:
    print('Caso não ocorra nenhum erro, esse else será executado.')
finally:
    print('FECHAR ARQUIVO')
