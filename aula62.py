# Exercício - Gerar o segundo dígito de um CPF com Python
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10
somar_digito = 0

for iterador in nove_digitos:
    iterador_int = int(iterador)
    multiplicar_digito = iterador_int * contador_regressivo
    somar_digito += multiplicar_digito
    contador_regressivo -= 1

primeiro_digito = somar_digito * 10
primeiro_digito %= 11

condicao = '0' if primeiro_digito > 9 else primeiro_digito

dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (resultado_digito_2 * 10) % 11
segundo_digito = '0' if segundo_digito > 9 else segundo_digito
print(f'O segundo digito do cpf é {segundo_digito}')
