# Student Grade Analyzer - Dictionary, Tuple, and Sorting Version

# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    # Test records for Part F (guardian conditions).
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A: Parse and organize the records.
for record in raw_records:
    # Split the record into fields.
    fields = record.split(",")

    # Guardian condition: a valid record must have exactly 4 fields
    # (1 name + 3 scores).
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    # Store the student's name.
    name = fields[0]

    # Convert the score fields to numbers safely.
    scores = []
    valid_scores = True
    for score_text in fields[1:]:
        try:
            scores.append(int(score_text))
        except ValueError:
            valid_scores = False
            break

    if not valid_scores:
        print(f"Skipped invalid record: {record}")
        continue

    # Add the name and scores to student_scores.
    student_scores[name] = scores


# PART B: Display records alphabetically.
print("\nORGANIZED STUDENT RECORDS")

for name in sorted(student_scores):
    print(f"{name}: {student_scores[name]}")


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate the student results.
for name, scores in student_scores.items():
    # Guard against an empty score list (avoids division by zero).
    if not scores:
        continue

    # Calculate total, average, highest, and lowest.
    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    # Determine the student's remark.
    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    # Add the average to sum_of_averages.
    sum_of_averages += average

    # Append the result tuple to ranking.
    ranking.append((average, name, highest_score, lowest_score, remark))


# PART D: Sort and display the ranking (highest average first).
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

for rank, (average, name, highest_score, lowest_score, remark) in enumerate(ranking, start=1):
    print(f"{rank:<5} {name:<10} {average:<8.2f} {highest_score:<8} {lowest_score:<7} {remark}")


# PART E: Display the class summary.
total_students = len(ranking)

# Calculate the class average safely.
class_average = sum_of_averages / total_students if total_students > 0 else 0

print("\nCLASS SUMMARY")
print(f"Number of Students: {total_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")

if ranking:
    top_average, top_name, _, _, _ = ranking[0]
    bottom_average, bottom_name, _, _, _ = ranking[-1]
    print(f"Highest: {top_name} - {top_average:.2f}")
    print(f"Lowest: {bottom_name} - {bottom_average:.2f}")