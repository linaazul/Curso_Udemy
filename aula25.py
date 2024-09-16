# Interpolação de string com % em Python
# s -> String
# d, i -> int
# f -> float
# x,X -> Hexadecimal (ABCDEF0123456789)  
nome = 'Adriel'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' %(nome, preco)
print(variavel)

print('O hexadecimal de %d é %08X' % (15,15))

#Isso é opcional, posso usar fstrings normalmente.