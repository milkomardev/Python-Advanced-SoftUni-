from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers = {
    'rose': 'rose',
    'tulip': 'tulip',
    'lotus': 'lotus',
    'daffodil': 'daffodil'
    }

while vowels and consonants:
    vow = vowels.popleft()
    con = consonants.pop()

    for flower in flowers.keys():
        flowers[flower] = flowers[flower].replace(vow, '')
        flowers[flower] = flowers[flower].replace(con, '')

        if not flowers[flower]:
            print(f"Word found: {flower}")
            break
    else:
        continue

    break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(v for v in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(v for v in consonants)}")