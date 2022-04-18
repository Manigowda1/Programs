def Maths(Student_list):
    Highest_marks_maths = 0
    Highest_marks_scorer = ''

    for student in Student_list:
        if (student.get("Maths") > Highest_marks_maths):
            Highest_marks_maths = student.get("Maths")
            Highest_marks_scorer = student.get("Name")

    print(f"Highest maths marks - {Highest_marks_maths} ,by {Highest_marks_scorer}.")

def science(Student_list):
    Highest_marks_Science = 0
    Highest_marks_scorer = ''

    for student in Student_list:
        if (student.get("Science") > Highest_marks_Science):
            Highest_marks_Science = student.get("Science")
            Highest_marks_scorer = student.get("Name")

    print(f"Highest Science marks - {Highest_marks_Science} ,by {Highest_marks_scorer}.")



Student_1 = {
    "Name": "Mani",
    "Maths":85,
    "Science":95,
    "Social":70
}
Student_2 = {
    "Name": "Dell",
    "Maths":80,
    "Science":50,
    "Social":95
}
Student_3 = {
    "Name": "Python",
    "Maths":95,
    "Science":90,
    "Social":45
}
Student_list = [Student_1,Student_2,Student_3]

Maths(Student_list)
science(Student_list)
























