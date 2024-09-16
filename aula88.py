# 143. Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis listas[], dicionario{}, set()
# Imutáveis tuplas(), strings"", ints0, floats0.0, None, False, range(0, 10)
lista = []  # falso
dicionario = {}  # falso
conjunto = set()  # falso
tupla = ()  # falso
string = ""  # falso
inteiro = 0  # falso
flutuante = 0.0  # falso
nada = None  # falso
falso = False  # falso
intervalo = range(0)  # falso


def falsy(valor):
    return 'falsy' if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
