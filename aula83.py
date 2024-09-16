# Empacotamento e desempacotamento de dicionários + *args e **kwargs
a, b = 1, 2
a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.60
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# args (ja vimos)
# kwargs - keywords arguments (argumentos nomeados)


def mostra_argumentos_nomeados(*args, **kwargs):
    print(f"Argumentos nao nomeados: {args}")

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostra_argumentos_nomeados(1, 2, nome='Joana', idade=24)
# mostra_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostra_argumentos_nomeados(**configuracoes)
