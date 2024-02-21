from functools import reduce
from math import floor

expression = input().split()
idx = 0

functions = {
    '*': lambda x: reduce(lambda a, b: a * b, map(int, expression[:x])),
    '/': lambda x: reduce(lambda a, b: a / b, map(int, expression[:x])),
    '+': lambda x: reduce(lambda a, b: a + b, map(int, expression[:x])),
    '-': lambda x: reduce(lambda a, b: a - b, map(int, expression[:x])),
}

while idx < len(expression):
    element = expression[idx]

    if element in '+-*/':
        expression[0] = functions[element](idx)
        [expression.pop(1) for i in range(idx)]
        idx = 1

    idx += 1

print(floor(int(expression[0])))