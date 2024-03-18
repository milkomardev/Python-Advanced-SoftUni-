def students_credits(*lines):
    courses_dict = {}
    result = []

    for line in lines:
        line_args = line.split('-')
        name = line_args[0]
        max_credits, max_points, student_points = int(line_args[1]), int(line_args[2]), int(line_args[3])
        percentage = (student_points / max_points) * 100
        student_credits = max_credits * (percentage/100)
        if name not in courses_dict:
            courses_dict[name] = student_credits

    total_credits = sum(courses_dict.values())
    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    [result.append(f"{n} - {c:.1f}") for n, c in sorted(courses_dict.items(), key=lambda x: -x[1])]

    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
