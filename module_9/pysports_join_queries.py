"""
Mick Welisevich
10 JUL 21
Module 9 Assignment 2

"""


import mysql.connector
from mysql.connector import errorcode

#Standard connection block
config = {
    "user": "pysports_user",
    "password": "5tgb7ujm%TGB&UJM",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

# Inner join query 
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

# get the results from the cursor object 
players = cursor.fetchall()

print("\n  -- DISPLAYING PLAYER RECORDS --")
    
for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

input("\n\n  Press any key to continue... ")

db.close()