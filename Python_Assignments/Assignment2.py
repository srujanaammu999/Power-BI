university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

##  Print all student names and their majors
for student_id, info in university_data.items():
    print(f"{info['name']} - {info['major']}")
print()

## Average score per course per student
for student_id, info in university_data.items():
    print(f"{info['name']}")
    for course, scores in info['courses'].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course}: {avg:.2f}")
    print()

## Find students who scored >90 in final of Python101
for student_id, info in university_data.items():
    courses = info['courses']
    if 'Python101' in courses and courses['Python101']['final'] > 90:
        print(info['name'])
    
## Add new course AI101 for student S101
university_data["S101"]["courses"]["AI101"] = {"midterm": 82, "final": 89, "project": 95}
print('\nUpdated new course for S101')

## Print average for each course
course_averages = {}
for student_id, info in university_data.items():
    for course, scores in info['courses'].items():
        if course not in course_averages:
            course_averages[course] = []
        avg = sum(scores.values()) / len(scores)
        course_averages[course].append(avg)
        print(f"{course}: {avg:.2f}")
print('\nAverage for each course:')
for course, scores in course_averages.items():
    avg = sum(scores) / len(scores)
    print(f"{course}: {avg:.2f}")




