# "def" define uma função personalizada - Introdução às funções em Python
"""
introdução as funções (def) em python
funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrão, funções em python reornam None(nada).
"""
# def Print():
#     print("Várias1")
#     print("Várias2")
#     print("Várias3")
#     print("Várias4")

def imprimir(a, b):
    print(a, b)

imprimir(1, 2)

def saudacao(nome= 'sem nome'):
    print(f'Olá, {nome}')

saudacao()
saudacao('adriel')

resultado = 16 % 8 == 0
print(resultado)