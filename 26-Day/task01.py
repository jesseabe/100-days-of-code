student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score":  [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame.head())

for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)