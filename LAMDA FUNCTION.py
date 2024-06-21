numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

data = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_data = sorted(data, key=lambda x: x[0])
print(sorted_data)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]