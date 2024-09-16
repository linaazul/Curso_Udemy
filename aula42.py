# while - Qual letra apareceu mais vezes na frase? (Iterando strings com while)

frase = 'O python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

indice = 0
quantidade_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == ' ':
        indice += 1
        continue
        
    quantidade_atual = frase.count(letra_atual)

    if quantidade_apareceu_mais_vezes < quantidade_atual:
        quantidade_apareceu_mais_vezes = quantidade_atual
        letra_apareceu_mais_vezes = letra_atual
    indice += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}" e ela apareceu {quantidade_apareceu_mais_vezes} vezes.')

