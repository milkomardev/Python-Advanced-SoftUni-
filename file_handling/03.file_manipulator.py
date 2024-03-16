import os

abs_path_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    command, *data = input().split('-')

    if command == 'End':
        break

    curr_file_path = os.path.join(abs_path_dir, f'{data[0]}')

    if command == 'Create':
        with open(curr_file_path, 'w'):
            pass

    elif command == 'Add':
        with open(curr_file_path, 'a') as file:
            file.write(f'{data[1]}\n')

    elif command == 'Replace':
        try:
            with open(curr_file_path, 'r+') as file:
                text = file.read()
                text = text.replace(data[1], data[2])

                file.seek(0)
                file.write(text)

        except FileNotFoundError:
            print('An error occurred')

    elif command == 'Delete':
        try:
            os.remove(curr_file_path)

        except FileNotFoundError:
            print('An error occurred')
