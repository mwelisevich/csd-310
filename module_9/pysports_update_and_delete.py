"""
Mick Welisevich
10 JUL 21
Module 9 Assignment 3
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

def show_players(cursor, title):
#Inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #Fetch players
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

db = mysql.connector.connect(**config)

cursor = db.cursor()

add_player = ("INSERT INTO player(first_name, last_name, team_id)VALUES(%s, %s, %s)")

player_data = ("Michael", "The Viking", 1)

cursor.execute(add_player, player_data)

db.commit()

show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

update_player = ("UPDATE player SET team_id = 2, first_name = 'Mick', last_name = 'The Titan' WHERE first_name = 'Michael'")

cursor.execute(update_player)

show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

delete_player = ("DELETE FROM player WHERE first_name = 'Mick'")

cursor.execute(delete_player)

show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

input("\n\n  Press any key to continue... ")

db.close()