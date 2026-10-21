# Week 5 - Hands-On Exercise: Student Grade Analyzer Version 3

**Course:** Python Programming  

 *Prepared by: Jackson S. Soriano, MIT*


## Scenario

Create a **Student Grade Analyzer** Version 3. The program receives student records written as comma-separated strings. It must convert the records into organized Python data, calculate each student's average, determine whether the student passed or failed, and display the students from highest to lowest average.

The passing average is **75**.

---

## Input Data

Use the following list in your program:

```python
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
]
```

Each string follows this format:

```text
StudentName,Score1,Score2,Score3
```

---

# Main Programming Tasks

## Part A – Parse and Organize the Records

Create an empty dictionary named `student_scores`.

For every string in `raw_records`:

1. Use `split(",")` to divide the string into fields.
2. Store the first field as the student's name.
3. Convert the remaining fields from strings to numbers.
4. Store the name and scores in `student_scores`.

The resulting dictionary should follow this structure:

```python
{
    "Ana": [88, 92, 90],
    "Ben": [70, 72, 74],
    # Remaining records...
}
```

### Required Concepts

- List traversal
- `split()`
- List slicing
- Numeric conversion
- Dictionary assignment

---

## Part B – Display the Organized Records

Loop through `student_scores` using `items()` and display each student and the corresponding score list.

Example format:

```text
Ana: [88, 92, 90]
Ben: [70, 72, 74]
```

Do not depend on the original dictionary order. Sort the names alphabetically before displaying them.

---

## Part C – Calculate Student Results

Create an empty list named `ranking`.

For every student:

1. Calculate the total using `sum()`.
2. Determine the number of scores using `len()`.
3. Calculate the average.
4. Determine the highest score using `max()`.
5. Determine the lowest score using `min()`.
6. Determine the remark:
   - `Passed` when the average is at least `75`
   - `Failed` when the average is below `75`
7. Create a tuple with this structure:

```python
(average, name, highest_score, lowest_score, remark)
```

8. Append the tuple to `ranking`.

### Required Concepts

- Dictionary traversal
- Built-in list functions
- Conditional statements
- Tuple creation
- `append()`

---

## Part D – Sort and Display the Ranking

Sort `ranking` from the highest average to the lowest average.

Use tuple unpacking to display each record.

Required table format:

```text
STUDENT GRADE REPORT
Rank  Name   Average  Highest  Lowest  Remark
1     Cara   93.33    95       91      Passed
2     Ana    90.00    92       88      Passed
3     Ella   87.00    89       85      Passed
4     Dan    78.00    80       76      Passed
5     Ben    72.00    74       70      Failed
```

Use `round(average, 2)` or formatted strings to display two decimal places.

---

## Part E – Display the Class Summary

After displaying the ranking, print:

- Number of students
- Number of students who passed
- Number of students who failed
- Class average
- Highest-ranked student and average
- Lowest-ranked student and average

Expected summary based on the given records:

```text
CLASS SUMMARY
Number of Students: 5
Passed: 4
Failed: 1
Class Average: 84.07
Highest: Cara - 93.33
Lowest: Ben - 72.00
```

---

## Part F – Add Guardian Conditions

Modify the program so that it safely handles incomplete or invalid records.

Add the following test records one at a time:

```python
"Fred,90,85"
"Gina"
"Henry,90,eighty,85"
"Ivy,"
```

Your program must:

1. Check whether a record has exactly four fields before accessing its score fields.
2. Skip incomplete records using `continue`.
3. Use `try` and `except ValueError` when converting scores.
4. Display a short message identifying the skipped record.
5. Continue processing all remaining valid records.

Example message:

```text
Skipped invalid record: Henry,90,eighty,85
```

---

# Starter Code

Complete every section marked `TODO`.

```python
# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A: Parse and organize the records.
for record in raw_records:
    # TODO: Split the record into fields.
    fields = []

    # TODO: Add a guardian condition for an invalid field count.

    # TODO: Store the student's name.
    name = ""

    # TODO: Convert the score fields to numbers safely.
    scores = []

    # TODO: Add the name and scores to student_scores.


# PART B: Display records alphabetically.
print("ORGANIZED STUDENT RECORDS")

# TODO: Sort the names and display every student and score list.


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate the student results.
for name, scores in student_scores.items():
    # TODO: Guard against an empty score list.

    # TODO: Calculate total, average, highest, and lowest.
    total = 0
    average = 0
    highest_score = 0
    lowest_score = 0

    # TODO: Determine the student's remark.
    remark = ""

    # TODO: Update the passed or failed counter.

    # TODO: Add the average to sum_of_averages.

    # TODO: Append the result tuple to ranking.


# PART D: Sort and display the ranking.
# TODO: Sort ranking from highest to lowest average.

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

# TODO: Use enumerate() and tuple unpacking to display the ranking.


# PART E: Display the class summary.
# TODO: Calculate the class average safely.

# TODO: Use ranking[0] and ranking[-1] safely.

print("\nCLASS SUMMARY")

# TODO: Display all required summary information.
```

---

# Program Requirements

Your program must use all of the following:

- At least one list
- At least one dictionary
- At least one tuple
- `for` loops
- `split()`
- List slicing
- `append()`
- `sum()`, `len()`, `max()`, and `min()`
- `items()`
- Tuple unpacking
- Sorting
- `if`, `else`, and `continue`
- `try` and `except ValueError`

Do not use external libraries such as Pandas.

---

# Testing Checklist

Before submitting, verify the following:

- [ ] All five valid students appear in the report.
- [ ] Cara appears at rank 1.
- [ ] Ben appears at rank 5.
- [ ] Ben is marked `Failed`.
- [ ] The other four students are marked `Passed`.
- [ ] All averages are correct and displayed to two decimal places.
- [ ] Invalid records are skipped without stopping the program.
- [ ] The class summary matches the processed valid data.
- [ ] The program contains meaningful comments.
- [ ] The program runs without syntax or runtime errors.

---





# Submission Requirements

Submit the following:

1. `student_grade_analyzer.py` or `.txt`
2. Screenshot showing the complete console output (1-3 pictures)
3. Youtube Link of Video Demo (max of 3 minutes)
4. A short reflection the challenges and learnings in accomplishing the exercise.


Use this filename format:

```text
Lastname_Firstname_StudentGradeAnalyzer.py
```

---

# Scoring Rubric

| Criterion | Points |
|---|---:|
| Correct parsing and dictionary construction | 15 |
| Accurate totals, averages, highest, and lowest scores | 15 |
| Correct tuples, sorting, and ranking display | 15 |
| Correct class summary and pass/fail counts | 10 |
| Guardian conditions and error handling | 10 |
| Code organization, naming, and comments | 5 |
| Reflection answers | 5 |
| **Total** | **75** |




