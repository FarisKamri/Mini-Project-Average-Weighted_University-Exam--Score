# This is a mini project to calculate the weighted exam score average

number_of_exams = int(input("Enter number of exams: "))
total_credits = int(input("Enter how many credits all these exams cover: "))

average = 0
for exam in range(number_of_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input ("Enter how many credits this exam cover: "))
    average = average + score*exam_credits/total_credits
print("Your average is", average)

