# stores name, list of courses and grades. Prints out data stored.
# Author: Daniel Gonzalez

student =   {
            "Student": "Mary",
            "courses":[
                    {"CourseName": "Programming",
                    "Grade": 45,
                    },
                    {"CourseName": "History",
                    "Grade": 99
                    }
                    ]
            }
        

print('Student: {}.'.format(student["Student"]))
# Prints out student's name

for course in student["courses"]:
    print('\t{}: {}.'.format(course["CourseName"], course["Grade"]))
# Prints out student`s courses and grades




