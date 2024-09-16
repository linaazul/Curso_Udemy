# (Parte 1) Escopo de funções e módulos em Python + global
"""
Escopo de funções em python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcancavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 # escopo global

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x 
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)