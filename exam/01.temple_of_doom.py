from collections import deque

tools = deque([int(x)for x in input().split()])
substances = deque([int(x)for x in input().split()])

challenges = [int(x)for x in input().split()]

while tools and substances:

    tool = tools.popleft()
    substance = substances.pop()
    total = tool * substance

    if total in challenges:
        challenges.remove(total)

    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance > 0:
            substances.append(substance)

    if len(challenges) == 0:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(t) for t in tools])}")
if substances:
    print(f"Substances: {', '.join([str(s) for s in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(c) for c in challenges])}")