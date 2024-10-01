# reduce - faz a redução de um iterável em um valor
from functools import reduce

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

# reduce always returns an accumulator and the itrable item


def reduce_func(accumulator, product):
    print('accumulator:', accumulator)
    print('product:', product)
    print()
    return accumulator + product['price']


total = reduce(
    reduce_func,
    # or
    # lambda ac, p: ac + p['price'],
    products,
    0.0
)

print('Total: ', total)

# total = 0
# for p in products:
#     total += p['price']
# print(total)

# print(sum([p['price'] for p in products]))
