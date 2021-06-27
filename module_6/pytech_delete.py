""" 
Mick Welisevich
25 JUN 2021
Module 6 Assignment 2

This program adds and then deletes a test document from a MongoDB database
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

#Contents of student formatted per instructions
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#Test document that will be added and then deleted. 
test_doc = {
    "student_id": "1010",
    "first_name": "Naught",
    "last_name": "Reelle"
}

# insert the test document 
test_doc_id = students.insert_one(test_doc).inserted_id

#Message formatted per instructions
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# find_one() method calling student_id 1010
student_test_doc = students.find_one({"student_id": "1010"})

#Message formatted per instructions
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

#Deletes test doc using delete_one()
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

#Assigns all student documents to new_student_list 
new_student_list = students.find({})

#Message formatted per instructions
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#Contents of student formatted per instructions
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#Program end prompt
input("\n\n  End of program, press any key to continue...")