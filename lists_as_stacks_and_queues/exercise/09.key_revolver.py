from collections import deque

bullet_price = int(input())
mag_size = int(input())
bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])
value = int(input())

bullets_in_mag = mag_size
bullets_shot = 0

while bullets and locks:

    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print('Bang!')

    else:
        print('Ping!')
        locks.appendleft(lock)

    bullets_shot += 1
    bullets_in_mag -= 1

    if bullets_in_mag == 0 and bullets:
        print('Reloading!')
        bullets_in_mag = min(mag_size, len(bullets))

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    reward = value - (bullets_shot*bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${reward}")