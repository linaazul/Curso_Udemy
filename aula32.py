# Flags, is, is not e None
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True #flag
    print('Faça algo.')
else:
    print('Não faça.')

if passou_no_if is None:
    print('Não passou no if.')
if passou_no_if is not None:
    print('Passou no if.')