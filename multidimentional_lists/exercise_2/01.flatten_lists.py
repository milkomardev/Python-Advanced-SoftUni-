# line = input().split("|")
# # sublist = []
# #
# # for sub_string in line[::-1]:
# #     sublist.extend(sub_string.split())
# #
# # print(*sublist)

numbers = [string.split() for string in input().split('|')]
print(*[' '.join(sublist) for sublist in numbers[::-1] if sublist])