students = []

def grade(marks):
    if student >= 90:
        print("A")
    elif student >=75:
        print("B")
    elif student >=60:
        print("C")
    elif student >=40:
        print("D")
    else:
        print("Fail")


def add_student():
    name = input("Name: ")
    marks = float(input("Marks: "))
    students.append((name, marks))  
    print("Student added")

def show_all():
    """Print:  1. Deepak - 87.0 - B"""
    if len(students) == 0:
        print("No students yet")
    else:
        print(students)

def show_topper():
    if len(students) == 0:
        print("No students yet")
    else:
        best = students[0]
        for i in len(students):
            if students[i] > best[1]:
                best = students[i]
        print(best)
    

def show_average():
    if len(students) == 0:
        print("No students yet")
        return
    # YOUR CODE: total = 0, loop, total += marks, then round(total/len(students), 2)
    pass

while True:
    print("\n1 Add  2 Show all  3 Topper  4 Average  5 Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        show_all()
    elif choice == '3':
        show_topper()
    elif choice == '4':
        show_average()
    elif choice == '5':
        print("Bye")
        break
    else:
        print("Invalid choice")
