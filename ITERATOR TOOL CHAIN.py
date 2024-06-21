from itertools import chain

l = [[1, ' ', 2], [12]]
flattened_list = list(chain.from_iterable(l))
flattened_list_no_spaces = [elem for elem in flattened_list if elem != ' ']
print("".join(map(str, flattened_list_no_spaces)))
