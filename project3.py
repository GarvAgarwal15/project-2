name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print(name, result)