
scores = [85, 92, 78, 90, 88]


total_score = sum(scores)
num_tests = len(scores)
average_score = total_score // num_tests


if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"


if average_score % 10 >= 5:
    grade += "+"


check_score = 90
if check_score in scores:
    print(f"The score {check_score} exists in the list.")
else:
    print(f"The score {check_score} does not exist in the list.")

scores_copy = scores
if scores is scores_copy:
    print("The scores and scores_copy are the same object.")
else:
    print("The scores and scores_copy are different objects.")


bitwise_result = scores[0] & scores[1]
print(f"Bitwise AND of the first two scores: {bitwise_result}")


print(f"The student's average score is {average_score} and their grade is {grade}.")