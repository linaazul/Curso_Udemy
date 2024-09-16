"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro_string = input('Digite um número INTEIRO: ')

try:
    numero_inteiro = int(numero_inteiro_string)
    numero_par = numero_inteiro % 2 == 0
    if numero_par:
        print('Este número é par.')
    else:
        print('Este número é impar.')
except:
    print('Isso não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario_string = input('Informe o horario atual: ')

try:
    horario_int = int(horario_string)
    if horario_int >= 0 and horario_int <= 11:
        print('Bom dia.')
    elif horario_int >= 12 and horario_int <= 17:
        print('Boa tarde.')
    elif horario_int >= 18 and horario_int <= 23:
        print('Boa noite.')
    else:
        print('Esse não é um horario valido, informe entre as 0 e 23.')
except:
    print("Informe um horario valido.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_usuario = input('Informe seu nome: ')

caracteres_no_nome = len(nome_usuario)

if caracteres_no_nome >=1 and caracteres_no_nome <= 4:
   print('Seu nome é curto.')
elif caracteres_no_nome >=5 and caracteres_no_nome <=6:
    print('Seu nome é normal.')
elif caracteres_no_nome > 6:
   print('Seu nome é grande.')
else:
   print('Informe seu nome.')
