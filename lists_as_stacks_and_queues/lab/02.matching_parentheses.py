text = input()
parentheses_stack = []

for i in range(len(text)):
    if text[i] == '(':
        parentheses_stack.append(i)
    elif text[i] == ')':
        print(text[parentheses_stack.pop():i + 1])
