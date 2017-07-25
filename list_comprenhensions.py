combination = [[(row, column) for column in range(1, 7)]
               for row in range(1, 7)]
print combination

numbers_list = [1, 2, 3, 4, 5, 6]
print [(c, r) for r in numbers_list for c in numbers_list]

num = 5
identity_matrix = [
    [1 if row == column else 0 for column in range(num)] for row in range(num)]
print identity_matrix

string_list = ['cat', 'dog', 'duck', 'bird', 'lion']
print [(animal.upper(), animal.lower(), len(animal)) for animal in string_list]
