# Exercício com funções
# Crie funções que duplicam, triplicam, quadruplicam
# o número recebido como parametro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = criar_multiplicador(2)
print(duplicar(2))

triplicar = criar_multiplicador(3)
print(triplicar(2))