from collections import deque

kids = deque(input().split())
leaving_toss = int(input())
counter = 1

while len(kids) > 1:
    if counter == leaving_toss:
        print(f'Removed {kids.popleft()}')
        counter = 1
    else:
        kids.rotate(-1)
        counter += 1

print(f'Last is {kids[0]}')
