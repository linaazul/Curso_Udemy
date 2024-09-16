# Formatação de strings com f-strings
# s -> String
# d, i -> int
# f -> float
# x,X -> Hexadecimal (ABCDEF0123456789)
# (Caractere)(><^)(quantidade)
# > ESQUERDA
# < DIREITA
# ^ CENTRO
# SINAL + ou -, serve para caso eu queira exibir se o número é negativo ou positivo
#o = força o numero ou simbolo a aparecer depois do sinal positivo ou negativo
#EX.: 0>-100,.1f
#Conversion flags !r

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel:$^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')