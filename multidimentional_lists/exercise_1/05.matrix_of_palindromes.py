rows, cols = [int(x) for x in input().split()]

for r in range(ord('a'), ord('a') + rows):
    for c in range(cols):
        print(f"{chr(r)}{chr(r + c)}{chr(r)}", end=' ')
    print()