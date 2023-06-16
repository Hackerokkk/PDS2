import itertools

# Задання вхідних змінних
variables = ['p', 'q', 'r']

# Побудова всіх можливих комбінацій значень вхідних змінних
input_combinations = list(itertools.product([False, True], repeat=len(variables)))

# Побудова заголовка таблиці
table_header = variables + ['fn']

# Виведення заголовка таблиці
print('\t'.join(table_header))

# Побудова та виведення значень функції fn для кожної комбінації
for inputs in input_combinations:
    p, q, r = inputs
    fn = p and (q != r)

    # Формування рядка таблиці
    row = [str(int(input)) for input in inputs] + [str(int(fn))]

    # Виведення рядка таблиці
    print('\t'.join(row))
