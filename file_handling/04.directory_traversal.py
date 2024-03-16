import os


def save_extensions(dir_name, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(file_name)

        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


abs_path_dir = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(abs_path_dir, input())

extensions = {}
result = []

try:
    save_extensions(directory)
except FileNotFoundError:
    print('Invalid directory')

extensions = sorted(extensions.items())

for extension, files in extensions:
    result.append(f'.{extension}')
    [result.append(f'- - - {file}') for file in sorted(files)]

report_file_path = os.path.join(abs_path_dir, 'report.txt')

with open(report_file_path, 'w') as report_file:
    report_file.write('\n'.join(result))
