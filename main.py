# Students stored in a list, each student a tuple (name, marks)
# Menu repeats until Exit: 1 Add · 2 Show all · 3 Topper · 4 Average · 5 Exit
# Show all = numbered rows with name, marks, grade (90+ A, 75+ B, 60+ C, 40+ D, else Fail)
# If there are no students, print a message — do not crash
# One function per menu action
# Then push to GitHub as student-marks-manager with a README: what it does, how to run it (python main.py), sample output.
# This is your first project you can explain. It goes on your resume tonight.
"""
student = []
name = ()
marks = ()
i = 1
while(i>0):
        user = int(input("Enter 1 = Add, 2 = Show all, 3 = Topper, 4 = Average, 5 = Exit"))
            
        if user == 1:
            name  = input("Enter the name of Student: ")
            marks  = int(input("Enter the marks of Student: "))
            student+=(name)
            student+=(marks)

        elif user == 2:
            print(student)
        elif user == 3:
            t = 0
            for j in student:
                 if t < j:
                      j == 0
            print(j)          
        elif user == 4:
            
        elif user == 5:
            break
        else:
            print("wrong Input")
        """

students = []          # list of (name, marks) tuples

def grade(marks):
    """Return 'A','B','C','D' or 'Fail'. RETURN it, do not print it."""
    # YOUR CODE: if / elif ladder from Day 2
    pass

def add_student():
    name = input("Name: ")
    marks = float(input("Marks: "))
    students.append((name, marks))     # <-- THE line you were missing
    print("Student added")

def show_all():
    """Print:  1. Deepak - 87.0 - B"""
    if len(students) == 0:
        print("No students yet")
        return
    # YOUR CODE: for i, (name, marks) in enumerate(students, start=1):
    pass

def show_topper():
    if len(students) == 0:
        print("No students yet")
        return
    # YOUR CODE: best = students[0], loop, if student[1] > best[1]: best = student
    pass

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