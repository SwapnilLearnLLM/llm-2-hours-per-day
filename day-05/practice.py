#  For loop
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

student_scores = [150, 142, 128, 185, 120, 196, 175, 111, 100, 145]
total_exam_score = sum(student_scores)
max = 0
for score in student_scores:
    if score > max:
        max = score
print(f"The highest score in the class is: {max}")

# Range Function
total = 0
for number in range(1, 101):
    total +=number
print(total)

