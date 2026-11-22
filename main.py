#from DATABASES import create_table, add_student, get_all_students,
#create_table()
#add_student("FADL", 95)
#add_student("ALI", 88)

#students = get_all_students()
#for s in students:
 #   print(s)
#print("DONE SUCCESS")
#from DATABASES import add_student, get_students
#print("=== تسجيل طالب جديد ===")
#name = input("اكتب اسم الطالب")
#score = int(input("اكتب الدرجه"))
#add_student(name,score)
#print("تم الحفظ بنجاح")
#print("\n=== كل الطلاب ===")
#get_students()
##########################
from DATABASES import add_student, get_students, search_student, delete_student
while True:
    print("\n=== school system===")
    print("1 - add new student")
    print("2 - view all student")
    print("3 - search student")
    print("4 - delete student")
    print("5 - exit")
    choice = input("choce number")
    if choice == "1":
        name = input("student name: ")
        score = int(input("degree: "))
        add_student(name, score)
        print("succses save")

    elif choice == "2":
        get_students()
    elif choice == "3":
        name = input("write name to search: ")
        search_student(name)
    elif choice == "4":
        student_id = int(input("write id to delete: "))
        delete_student(student_id)
    elif choice == "5":
        print("BAY BAY FADL!!")
        break
    else:
        print("wrong choice")



        





    

