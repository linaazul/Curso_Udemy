# 173. count é um iterador sem fim (itertools)
from itertools import count

count1 = count(0, 8)  # começa do 0 e step para multiplos de 8
count2 = count(step=8, start=0)  # count com argumentos nomeados
range1 = range(10, 100)

print('count', hasattr(count1, '__iter__'))
print('count', hasattr(count1, '__next__'))
print('range', hasattr(range1, '__iter__'))
print('range', hasattr(range1, '__next__'))

print('count')
for i in count1:
    if i >= 100:
        break
    print(i)

print()

print('range')
for i in range1:
    print(i)
