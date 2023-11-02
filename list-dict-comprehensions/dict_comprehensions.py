import random
import pandas as pd

# practice
names = ["Tobias", "Belén", "Maria", "Felipe", "Estanislao"]
students_scores = {students: random.randint(1, 10) for students in names}
passed_students = {student: score for student,
                   score in students_scores.items() if score > 5}
passed_students2 = {student_key: students_scores[student_key]
                    for student_key in students_scores if students_scores[student_key] > 5}

# Ex 1
sentence = "What is the Airspeed Velocity of an Unlanden Swallow?"
word_list = sentence.split(' ')
word_list_result = {word: len(word) for word in word_list}

# Ex 2
celcius_dict = {"Monday": 12, "Tuesday": 14, "Wednesday": 15,
                "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
far_dict = {day: temp * 9/5 + 32 for day, temp in celcius_dict.items()}

# Ex 3
students_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

students_df = pd.DataFrame(students_dict)
# Loopear el dataframe entero
# for key, value in students_df.items():
#     print(value)

#Loopear las filas del dataframe
# for index, data in students_df.iterrows():
#     Cada fila trae un objeto cual puedo acceder a su valor en base al nombre de su columna.
#     print(data.student, data.score)

# df_to_dict = {data.student:data.score for index, data in students_df.iterrows()}
# print(df_to_dict)