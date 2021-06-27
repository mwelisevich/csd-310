""" 
Mick Welisevich
25 JUN 2021
Module 6 Assignment 3

This program updates a document within a database on MongoDB

"""
from pymongo import MongoClient
#Step 1

url = "mongodb+srv://admin:admin@cluster0.t6bdf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
#Step 2

client = MongoClient(url)
#Step 3

db = client.pytech
#Step 4

students = db.students
#Assigns students database to students

student_list = students.find({})
#Returns students in students

#Message formatted per instructions
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#Message formatted per instructions
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#Update document with student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Not Twotone"}})

#find_one() called to locate edited document
tommy = students.find_one({"student_id": "1007"})

#Message formatted per instructions
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

#Message formatted per instructions
print("  Student ID: " + tommy["student_id"] + "\n  First Name: " + tommy["first_name"] + "\n  Last Name: " + tommy["last_name"] + "\n")

#Message formatted per instructions
input("\n\n  End of program, press any key to continue...")