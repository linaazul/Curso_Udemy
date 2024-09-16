# Exercícios com funções + Solução (prepare-se para pausar)

# Crie uma função que multiplica todos os argumentos 
# não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor 
# da variavel.

def multiplicar_numeros(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

teste = multiplicar_numeros(1, 5, 20, 10)
print(teste)    

# Crie uma funcao que fala se o numero é par ou impar.
# Retorne se o numero é par ou impar

def par_ou_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    
print(par_ou_impar(28))
print(par_ou_impar(21))
print(par_ou_impar(55))
print(par_ou_impar(97))
