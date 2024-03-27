def gather_credits(credits_needed, *args):
    enrolled_courses = {}
    result = []

    for course in args:
        if credits_needed > 0:
            if course[0] not in enrolled_courses:
                enrolled_courses[course[0]] = course[1]
                credits_needed -= course[1]
        else:
            break

    if credits_needed <= 0:
        result.append(F"Enrollment finished! Maximum credits: {sum(enrolled_courses.values())}.")
        result.append(f"Courses: {', '.join(sorted(enrolled_courses.keys()))}")

    else:
        result.append(f"You need to enroll in more courses! You have to gather {credits_needed} credits more.")

    return '\n'.join(result)


print(gather_credits(
    80,
    ("Basics", 27),
))


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
