#Student grade calculator
scores = [90, 65, 78, 88, 92, 95]

passed = 0
failed = 0

print("Student Scores:")

for score in scores:
    print(score)

print()

for i, score in enumerate(scores, start=1):

    if score >= 90:
        grade = "Excellent"
        status = "Passed"
        passed += 1

    elif score >= 80:
        grade = "Very Good"
        status = "Passed"
        passed += 1

    elif score >= 75:
        grade = "Good"
        status = "Passed"
        passed += 1

    else:
        grade = "Failed"
        status = "Failed"
        failed += 1

    if status == "Passed":
        print(f"Student {i}: {score} - {grade} - Passed")
    else:
        print(f"Student {i}: {score} - Failed")

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

print()
print(f"Total Score: {total}")
print(f"Average Score: {average:g}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")