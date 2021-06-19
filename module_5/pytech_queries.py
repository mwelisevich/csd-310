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

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

print("-- Pytech Collection List --")
print(db.list_collection_names())
#Step 5

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
tommy = students.find_one({"student_id": "1007"})

 
# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + tommy["student_id"] + "\n  First Name: " + tommy["first_name"] + "\n  Last Name: " + tommy["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")