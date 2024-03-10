numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_word = line

    try:
        number_in_digits = int(input())
        numbers_dictionary[number_as_word] = number_in_digits
    except ValueError:
        print('The variable number must be an integer.')

    line = input()

line = input()
while line != "Remove":
    number_to_search = line

    try:
        print(numbers_dictionary[number_to_search])
    except KeyError:
        print('Number does not exist in dictionary.')

    line = input()

line = input()
while line != "End":
    number_to_delete = line

    try:
        del numbers_dictionary[number_to_delete]
    except KeyError:
        print('Number does not exist in dictionary.')

    line = input()

print(numbers_dictionary)
