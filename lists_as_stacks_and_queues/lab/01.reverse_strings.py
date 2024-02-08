from collections import deque

text = deque(input())

# text.reverse()
# print(''.join(text))

text_as_stack = []
for i in range(len(text)):
    text_as_stack.append(text.pop())

print(''.join(text_as_stack))