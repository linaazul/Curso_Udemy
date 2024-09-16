# Métodos úteis do tipo set em Python
# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Luiz')  # adiciona um valor por vez pro set
s1.add(1)
# Tomar cuidado ao enviar strings pelo update
s1.update(('Olá, mundo', 1, 2, 3, 4))
# s1.clear()  # Limpa o set
s1.discard('Olá, mundo')  # Descarta valores especificados no parentese

print(s1)
