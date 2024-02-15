from collections import deque

green_light_duration = int(input())
free_window = int(input())
command = input()
cars = deque()
total_cars = 0

while command != "END":
    if command != 'green':
        cars.append(command)

    else:
        seconds_left = green_light_duration

        while seconds_left > 0 and cars:
            current_car = cars.popleft()
            total_time = free_window + seconds_left

            if len(current_car) > total_time:
                print(f'A crash happened!\n{current_car} was hit at {current_car[total_time]}.')
                exit()

            seconds_left -= len(current_car)
            total_cars += 1

    command = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
