### This is student_grade_analyzer.py


def classify_grade(grade):
    if grade>= 90:
        return "Excellent", "Passed"
    elif grade >= 85:
        return "Very Good", "Passed"
    elif grade >= 80:
        return "Good", "Passed"
    elif grade >= 75:
        return "Satisfactory", "Passed"
    else:
        return "Needs improvement", "Failed"

def load_students(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                fields = line.split(',')
                if len(fields) != 3:
                    continue
                student_number, name, grade_str = fields
                try:
                    grade = float(grade_str)
                    if 0 <= grade <= 100:
                        students.append({
                            'student_number': student_number,
                            'name': name,
                            'grade': grade
                        })
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    return students    

def calculate_statistics(students):
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student['grade']
        total_grade += grade
        if grade >= 75:
            passed_count += 1
        else:
            failed_count += 1
        if grade > highest_student['grade']:
            highest_student = student
        if grade < lowest_student['grade']:
            lowest_student = student

    average_grade = total_grade / len(students)
    return {
        'average': average_grade,
        'passed': passed_count,
        'failed': failed_count,
        'highest': highest_student,
        'lowest': lowest_student
    }
def display_students(students):
    print(f"{'Student Number':<15} {'Name':<20} {'Grade':<10} {'Classification':<20} {'Status':<10}")
    print("-" * 75)
    for student in students:
        classification, status = classify_grade(student['grade'])
        print(f"{student['student_number']:<15} {student['name']:<20} {student['grade']:<10.2f} {classification:<20} {status:<10}")

def display_statistics(statistics):
    if statistics is None:
        print("No statistics available.")
        return
    print(f"Average Grade: {statistics['average']:.2f}")
    print(f"Number of Students Passed: {statistics['passed']}")
    print(f"Number of Students Failed: {statistics['failed']}")
    print(f"Highest Grade: {statistics['highest']['grade']:.2f} (Student Number: {statistics['highest']['student_number']}, Name: {statistics['highest']['name']})")
    print(f"Lowest Grade: {statistics['lowest']['grade']:.2f} (Student Number: {statistics['lowest']['student_number']}, Name: {statistics['lowest']['name']})")

def search_student(students, keyword):
    matches = []
    keyword = keyword.strip().lower()
    for student in students:
        if keyword in student['student_number'].lower() or keyword in student['name'].lower():
            matches.append(student)
    return matches

def save_report(students, statistics, filename):
    try:
        with open(filename, 'w') as file:
            file.write(f"{'Student Number':<15} {'Name':<20} {'Grade':<10} {'Classification':<20} {'Status':<10}\n")
            file.write("-" * 75 + "\n")
            for student in students:
                classification, status = classify_grade(student['grade'])
                file.write(f"{student['student_number']:<15} {student['name']:<20} {student['grade']:<10.2f} {classification:<20} {status:<10}\n")
            file.write("\nClass Statistics:\n")
            if statistics is not None:
                file.write(f"Average Grade: {statistics['average']:.2f}\n")
                file.write(f"Number of Students Passed: {statistics['passed']}\n")
                file.write(f"Number of Students Failed: {statistics['failed']}\n")
                file.write(f"Highest Grade: {statistics['highest']['grade']:.2f} (Student Number: {statistics['highest']['student_number']}, Name: {statistics['highest']['name']})\n")
                file.write(f"Lowest Grade: {statistics['lowest']['grade']:.2f} (Student Number: {statistics['lowest']['student_number']}, Name: {statistics['lowest']['name']})\n")
    except OSError as e:
        print(f"Error: Could not write to file {filename}. {e}")

def main():
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nStudent Grade Analyzer Menu:")
        print("1. Display all student records")
        print("2. Display class statistics")
        print("3. Search for a student")
        print("4. Save report to file")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_students(students)
        elif choice == '2':
            display_statistics(statistics)
        elif choice == '3':
            keyword = input("Enter student number or name to search: ")
            matches = search_student(students, keyword)
            if matches:
                display_students(matches)
            else:
                print("No matching student records found.")
        elif choice == '4':
            filename = input("Enter the filename to save the report: ")
            save_report(students, statistics, filename)
            print(f"Report saved to {filename}.")
        elif choice == '5':
            print("Exiting the Student Grade Analyzer.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
