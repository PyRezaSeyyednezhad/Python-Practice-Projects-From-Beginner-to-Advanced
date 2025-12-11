def student_info_dictionary(id:int, name:str, age:int, math_score:float, english_score:float, programming_score:float):
    student_info = {
        "student_id": id,
        "student_name": name,
        "student_age": age,
        "student_lessons_score": [("Math", math_score), ("English", english_score), ("Programming", programming_score)],
        "student_gpa": (math_score + english_score + programming_score) / 3
    }
    print(student_info)

student_info_dictionary(1, "Reza", 24, 17, 17, 15)
