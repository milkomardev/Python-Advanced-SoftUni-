import os
from string import punctuation

abs_path_dir = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(abs_path_dir, 'text.txt')
output_file_path = os.path.join(abs_path_dir, 'output.txt')

with open(text_path, 'r') as text:
    lines = text.readlines()

output_file = open(output_file_path, 'w')

for i in range(0, len(lines)):
    letters, marks = 0, 0

    for symbol in lines[i]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(lines[i][:-1])} ({letters})({marks})\n")

output_file.close()
