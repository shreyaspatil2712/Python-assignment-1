def read_student_data(filename):
    try:
        students = []
        with open(filename, 'r') as file:
            for line in file:
                try:
                    name, score = line.strip().split(',')
                    score = float(score)  
                    students.append((name, score))
                except ValueError:
                    print(f"Warning: Invalid data format in line: {line.strip()}")
        return students

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def avg(students):
    if not students:
        return 0
    total_score = sum(score for name, score in students)
    return total_score / len(students)

def above_avg(students, average_score):
    print(f"\nStudents who scored above the average score of {average_score:.2f}:\n")
    for name, score in students:
        if score > average_score:
            print(f"{name}: {score:.2f}")

def analyze_student_performance(filename):
    students = read_student_data(filename)
    if students is None:
        return

    average_score = avg(students)

    above_avg(students, average_score)


filename = 'scores.txt'  
analyze_student_performance(filename)
