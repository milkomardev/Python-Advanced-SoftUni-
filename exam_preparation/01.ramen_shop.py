from collections import deque

bowls = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while bowls and customers:
    bowl = bowls.pop()
    cmr = customers.popleft()

    if bowl == cmr:
        continue

    elif bowl > cmr:
        bowl -= cmr
        bowls.append(bowl)

    elif cmr > bowl:
        cmr -= bowl
        customers.appendleft(cmr)

if not customers:
    print('Great job! You served all the customers.')
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")