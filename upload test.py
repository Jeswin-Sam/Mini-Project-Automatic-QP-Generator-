from upload_function import *

for i in ("CSE", "ECE", "EEE", "MECH", "CIVIL"):
    for j in ("1st Year", "2nd Year", "3rd Year", "4th Year"):
        for k in ("Subject 1", "Subject 2", "Subject 3"):
            for l in range(1,6):
                selected_department = i
                selected_year = j
                selected_subject = k
                selected_unit = str(l)
                selected_part = "B"
                file_path = "C:\\Users\\Admin\\Desktop\\Auto QP Generator\\Program\\Unit-1 Part B.xlsx"

                upload_questions(selected_department, selected_year, selected_subject, selected_unit, selected_part, file_path)