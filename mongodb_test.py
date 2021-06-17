"""
Mick Welisevich
17 JUN 2021
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
print("\nEnd of program, press any key to exit...")
#Step 5