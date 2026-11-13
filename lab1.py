name = input(" enter the student name: ")
n = int(input("enter the no of subject: "))
total = 0
for i in range(1,n+1):
    mark = float(input(f'enter mark fpr the subject{i}:' ))
    total += mark
    percentage = total/n
    if percentage >= 90:
        grade = "A+"
        performence = "outstanding"
    elif percentage >= 80:
        grade = "A"
        performence = "excellent"
    if percentage >= 70:
        grade = "B"
        performence = "very good"
    if percentage >= 60:
        grade = "C"
        performence = "good"
    if percentage >= 50:
        grade = "D"
        performence = "average"
    else:
        grade = "f"
        performence = "need improvement"
print("/n --- academic performance ---")
print("student")
print("")            
print("")
print("")
print("performance:",performence)