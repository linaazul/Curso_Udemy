# Formatação de strings com o método format
a = 'A'
b = 'B'
c = 1.1

formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
print(formato)

#Parametro nomeado é quando nomeamos um parametro dentro de uma função.
#Tudo que vinher depois de um parametro nomeado deve ser nomeado.
#exemplo:
e = 'EE'
f = 12
formato2 = 'e={0}, f={nomeando:.2f}'.format(e, nomeando=f)
print(formato2)