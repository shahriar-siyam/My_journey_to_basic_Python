mark=int(input())
if mark>=80:
    grade="A+"
    print("Your grade is ", grade)
elif mark>=75:
    grade="A"
    print("Your grade is ",grade)
elif mark >= 70:
    grade = "A-"
    print("Your grade is ", grade)
elif mark>=65:
    grade="B+"
    print("Your grade is ", grade)
else:
    print("Below the expectation")
