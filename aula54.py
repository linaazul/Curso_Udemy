#  Exercício - crie uma lista de compras com listas
"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista_de_compras = []
acao = ''
while acao != 'e':
    print("Digite para fazer uma ação.")
    acao = input("[i]nserir, [a]pagar, [l]istar, [e]ncerrar: ")

    if acao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista_de_compras.append(item)
    elif acao == 'l':
        os.system('cls')
        if lista_de_compras == []:
            print('Nada para listar por enquanto.')
        else:
            for indice, nome in enumerate(lista_de_compras):
                print(indice, nome) 
    elif acao == 'a':
        os.system('cls')
        apagar_indice = input("Escolha o indice do item que deseja apagar: ")
        try:
            apagar_indice_int = int(apagar_indice)
            del lista_de_compras[apagar_indice_int]
            print("Item deletado com sucesso.")
        except:
            print("Não foi possivel apagar esse item, verifique se o número que digitou foi o correto.")
    elif acao == 'e':
        os.system('cls')
        print("Obrigado por comprar conosco, volte NUNCA.")
    else:
        print("Digite uma opção valida.")
        continue