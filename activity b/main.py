# "Connie"
# "ISQA 3900 Web Application Development"
# "Data: 2/14/2021"
# "calculate grade"


# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter '-1' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0
list_number = []

while True:
    try:
        test_score = int(input("Enter test score (-1 to quit): "))
        if 0 <= test_score <= 100:
            score_total += test_score
            counter += 1
            list_number.append(test_score)
        else:
            print("You must enter integer value >= 0 and <= 100 or -1 to quit. Try again.")

    except ValueError:
        print("You must enter integer value >= 0 and <= 100 or -1 to quit. Try again.")
    if test_score != -1:
        test_score = int(test_score)
    else:
        break

# calculate average score
average_score = round(score_total / counter, 2)

# the letter grade
if 92.5 <= average_score <= 100:
    grade = "A"
elif 88.5 <= average_score <= 92.49:
    grade = "B+"
elif 82.5 <= average_score <= 88.49:
    grade = "B"
elif 77.5 <= average_score <= 82.49:
    grade = "C+"
elif 72.5 <= average_score <= 77.49:
    grade = "C"
elif 59.5 <= average_score <= 72.49:
    grade = "D"
else:
    grade = "F"

# format and display the result
print("======================")
print("Scores:", list_number,
      "\nTotal Score:", score_total,
      "\nAverage Score:", average_score,
      "\nLetter Grade:", grade)
print()
print("Bye")