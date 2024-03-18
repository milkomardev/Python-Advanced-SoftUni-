from collections import deque

food = deque([int(x) for x in input().split(', ')])
stamina = deque([int(x) for x in input().split(', ')])

peaks = {
    1: ['Vihren', 80],
    2: ['Kutelo', 90],
    3: ['Banski Suhodol', 100],
    4: ['Polezhan', 60],
    5: ['Kamenitza', 70],
}

conquered = []
peak_to_climb = 1

for day in range(7):
    portion = food.pop()
    energy = stamina.popleft()
    total_sum = portion + energy

    if total_sum >= peaks[peak_to_climb][1]:
        conquered.append(peaks[peak_to_climb][0])
        if peak_to_climb == 5:
            print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
            break
        peak_to_climb += 1

else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered:
    print('Conquered peaks:')
    print('\n'.join(conquered))