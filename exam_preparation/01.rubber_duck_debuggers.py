from collections import deque


ducks = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0,
}


time_for_task = deque([int(x) for x in input().split()])
number_of_tasks = deque([int(x) for x in input().split()])

while time_for_task and number_of_tasks:
    time = time_for_task.popleft()
    tasks = number_of_tasks.pop()

    total_time = time * tasks

    if 0 <= total_time <= 60:
        ducks['Darth Vader Ducky'] += 1
    elif 61 <= total_time <= 120:
        ducks['Thor Ducky'] += 1
    elif 121 <= total_time <= 180:
        ducks['Big Blue Rubber Ducky'] += 1
    elif 181 <= total_time <= 240:
        ducks['Small Yellow Rubber Ducky'] += 1
    elif total_time > 240:
        tasks -= 2
        time_for_task.append(time)
        number_of_tasks.append(tasks)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{name}: {count}") for name, count in ducks.items()]

