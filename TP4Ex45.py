import statistics as s
student_and_grade = {"Martina": 5.35, "Bastien": 5.07, "Claire": 3.53, "Anna":
                    4.09, "Maria": 4.55, "Kim": 3.98,"Robin": 3.87, "Adriana": 5.20, "Kristina":
                    5.33, "Michael": 4.52, "Sophie": 4.54, "Sara": 4.94,"Olof": 4.61, "Tina": 5.74,
                    "Hanna": 4.42, "Mirsa": 5.55, "Sanna": 4.99, "Sally": 4.34,"Urban": 4.11,
                    "Kelly": 5.14, "Helmer": 4.53, "Joanna": 4.69, "Josephine": 4.00, "Vilma": 5.19,
                    "Martin": 5.35, "Bastiena": 5.07, "Klaire": 3.53, "Anne": 4.09, "Marie": 4.55,
                    "Kimi": 4.98,"Robina": 3.87, "Adrian": 5.20, "Kristian": 3.3, "Michaelle": 3.52,
                    "Sophia": 4.54, "Sarah": 4.94,"Olaf": 4.61, "Tino": 5.74, "Hanne": 4.42, "Mirso":
                    3.55, "Sannah": 4.99, "Sallie": 4.34,"Urbi": 4.11, "Kellian": 5.14, "Helmut": 4.53,
                    "Joan": 4.69, "Joseph": 4.00, "Vilmer": 5.19 }

grade_average = s.mean(student_and_grade.values())
students_above_avg = []
for name, grade in student_and_grade.items():
    if grade > grade_average:
        students_above_avg.append(grade)

print(grade_average)
print(len(students_above_avg))