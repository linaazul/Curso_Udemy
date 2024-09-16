# Dictionary Comprehension e Set Comprehension
product = {
    'name': 'Blue pen',
    'price': 2.5,
    'category': 'office pen'
}

new_product = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
    if key != 'category'
}

list1 = [
    ('a', 'a value'),
    ('b', 'b value'),
    ('c', 'c value'),
]

new_dictionary = {
    key: value
    for key, value in list1
}

print(new_product)
print()
print(new_dictionary)

s1 = {
    i ** 2
    for i in range(10)
}

print(s1)
