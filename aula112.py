# 177. filter é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

# filter
# new_products = [
#     p for p in products
#     if p['price'] > 10
# ]
new_products = filter(
    lambda p: p['price'] > 10,
    products
)


print_iter(products)
print_iter(new_products)
