# Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores)
# Generation expression, iterables e iterations em python
import sys
iterable = ['Eu', 'Tenho', '__iter__']
iterador = iterable.__iter__()  # tem __iter__ e __next__
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))

# Generator expression, Iterables e Iterators em Python
# assim a lista salva na memoria e ocupa espaço
# lista = [n for n in range(10)]
generator = (n for n in range(10))
print(sys.getsizeof(generator))
