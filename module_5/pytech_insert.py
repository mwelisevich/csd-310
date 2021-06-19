"""
Mick Welisevich
19 JUN 2021
Module 5 Assignment 3
"""

from pymongo import MongoClient
#Step 1

url = "mongodb+srv://admin:admin@cluster0.t6bdf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
#Step 2

client = MongoClient(url)
#Step 3

db = client.pytech
#Step 4

print("-- Pytech Collection List --")
print(db.list_collection_names())
#Step 5

tommy = {
"student_id": "1007",
"first_name": "Tommy",
"last_name": "Twotone",
"enrollments": [
    {
        "term": "spring",
        "gpa": "4.0",
        "start_date": "03JAN21",
        "end_date": "05MAY21",
        "courses": [
            {
                "course_id": "ECON101",
                "description": "Economics 101",
                "instructor": "Alex Smith",
                "grade": "A+"
            },
            {
                "course_id": "PHYS101",
                "description": "Physics 101",
                "instructor": "Isaac Newton",
                "grade": "A+"
            },
            {
                "course_id": "ART101",
                "description": "Introduction to Visual Arts 101",
                "instructor": "Van Gogh",
                "grade": "A+"
            },
        ]
     },
     {
         "term": "summer",
         "gpa": "3.90",
         "start_date": "06MAY21",
         "end_date": "30AUG21",
         "courses": [
             {
                 "course_id": "SPAN250",
                 "description": "Spanish Grammer",
                 "instructor": "Sophia Vergara",
                 "grade": "A+"
            },
            {
                "course_id": "HIST250",
                "description": "History of the American Revolution",
                "instructor": "Alexander Hamilton",
                "grade": "A"
            },
            {
                "course_id": "PSYCH230",
                "description": "Introduction to Personality",
                "instructor": "Jordan B. Peterson",
                "grade": "A+"
            }
        ]
    }
]
}

randy = {
"student_id": "1008",
"first_name": "Randy",
"last_name": "Moss",
"enrollments": [
    {
        "term": "spring",
        "gpa": "4.0",
        "start_date": "03JAN21",
        "end_date": "05MAY21",
        "courses": [
            {
                "course_id": "ECON101",
                "description": "Economics 101",
                "instructor": "Brett Favre",
                "grade": "A+"
            },
            {
                "course_id": "PHYS101",
                "description": "Physics 101",
                "instructor": "Charles Woodson",
                "grade": "A+"
            },
            {
                "course_id": "THEATRE250",
                "description": "Touchdown Celebrations",
                "instructor": "Jerry Rice",
                "grade": "A+"
            },
        ]
     },
     {
         "term": "summer",
         "gpa": "4.0",
         "start_date": "06MAY21",
         "end_date": "30AUG21",
         "courses": [
             {
                 "course_id": "SPAN250",
                 "description": "Spanish Grammer",
                 "instructor": "Sophia Vergara",
                 "grade": "A+"
            },
            {
                "course_id": "MATH200",
                "description": "Calculus II",
                "instructor": "Isaac Newton",
                "grade": "A+"
            },
            {
                "course_id": "PSYCH300",
                "description": "Maps of Meaning",
                "instructor": "Jordan B. Peterson",
                "grade": "A+"
            }
        ]
    }
]
}

billy = {
"student_id": "1009",
"first_name": "Billy",
"last_name": "Thorton",
"enrollments": [
    {
        "term": "spring",
        "gpa": "3.5",
        "start_date": "03JAN21",
        "end_date": "05MAY21",
        "courses": [
            {
                "course_id": "ECON250",
                "description": "Micro Economics",
                "instructor": "Chevy Chase",
                "grade": "B+"
            },
            {
                "course_id": "THEATRE300",
                "description": "Principles of Acting",
                "instructor": "Laurence Olivier",
                "grade": "A+"
            },
            {
                "course_id": "ART101",
                "description": "Introdution to Visual Arts",
                "instructor": "Van Gogh",
                "grade": "A+"
            },
        ]
     },
     {
         "term": "summer",
         "gpa": "4.0",
         "start_date": "06MAY21",
         "end_date": "30AUG21",
         "courses": [
             {
                 "course_id": "SPAN250",
                 "description": "Spanish Grammer",
                 "instructor": "Sophia Vergara",
                 "grade": "A+"
            },
            {
                "course_id": "MATH100",
                "description": "College Algebra",
                "instructor": "Matthew McConaughey",
                "grade": "A+"
            },
            {
                "course_id": "PSYCH300",
                "description": "Maps of Meaning",
                "instructor": "Jordan B. Peterson",
                "grade": "A+"
            }
        ]
    }
]
}

students = db.students

#Formatted IAW requirements

print("\n  -- INSERT STATEMENTS --")

tommy_student_id = students.insert_one(tommy).inserted_id

print("  Inserted student record Tommy Twotone into the students collection with document_id " + str(tommy_student_id))

randy_student_id = students.insert_one(randy).inserted_id

print("  Inserted student record Randy Moss into the students collection with document_id " + str(randy_student_id))

billy_student_id = students.insert_one(billy).inserted_id

print("  Inserted student record Billy Thorton into the students collection with document_id " + str(billy_student_id))

input("\n\n  End of program, press any key to exit... ")