primeiro_valor = input('Informe um valor: ')
segundo_valor = input('Informe outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}.')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}.')
else:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=}.')
