from collections import deque


def is_match(n1, n2, char, collection):
    if str(n1) + char in collection:
        return F"{n1}{char}"
    elif str(n2) + char in collection:
        return F"{n2}{char}"


seats = input().split(', ')
first_seq = deque([int(x) for x in input().split(', ')])
second_seq = deque([int(x) for x in input().split(', ')])

matches = []
rotations = 0

while len(matches) < 3 and rotations < 10:
    n1 = first_seq.popleft()
    n2 = second_seq.pop()
    ascii_char = chr(n1 + n2)
    current_str = is_match(n1,n2,ascii_char,seats)
    rotations += 1
    if current_str:
        matches.append(current_str)
        seats.remove(current_str)
    else:
        first_seq.append(n1)
        second_seq.appendleft(n2)

print(f"Seat matches: {', '.join(str(m) for m in matches)}")
print(f"Rotations count: {rotations}")