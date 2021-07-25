# Authors:      Andreas Arnet, Mick Welisevich, Michael Lohr, Shawn Roberts, Walter Dipping
# Date:         July 25, 2021
# Title:        Module 12 - Milestone #5
# Description:  Several Reports

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "password",
    "host": "127.0.0.1",
    "database": "echogroup",
    "raise_on_warnings": True
}
try: 
    # Create connection
    db = mysql.connector.connect(**config)  
    cursor = db.cursor()

       # Report 1
    query1 ='''
    SELECT
	client.client_id,
	client.`name`,
	client.account_creation_date,
	month(account_creation_date) as 'account_creation_month',
	client.`status`
    FROM
	client
	INNER JOIN employee ON client.relationship_manager = employee.employee_id 
    WHERE
	client.`status` = 'active' 
	AND client.account_creation_date > CURRENT_DATE () - INTERVAL 6 MONTH
    ORDER BY account_creation_date
    '''
    query2 ='''
    SELECT
        count( client.client_id ) AS 'count_clients',
        date_format( account_creation_date, '%M %Y' ) 
    FROM
        client
        INNER JOIN employee ON client.relationship_manager = employee.employee_id 
    WHERE
        client.`status` = 'active' 
        AND client.account_creation_date > CURRENT_DATE () - INTERVAL 6 MONTH 
    GROUP BY
        date_format( account_creation_date, '%M %Y' ) 
    ORDER BY
        date_format( account_creation_date, '%M %Y' )
    '''

    print("===== Report 1 =====")
    print("How many clients have been added for each of the past six months?")
    cursor.execute(query2)
    query2 = cursor.fetchall()
    for results  in query2:
        print(f"{results[1]}:\t {results[0]}")

    cursor.execute(query1)
    report1 = cursor.fetchall()
    print("TOTAL:\t\t",cursor.rowcount,"\n")
    for results  in report1:
        print(f"Client ID:            {results[0]}")
        print(f"Client Name:          {results[1]}")
        print(f"Account Creation:     {results[2]}")
        print(f"Status:               {results[3]}")
        print(f"Relationship Manager: {results[4]}\n")




    # Report 2
    query =    '''
    SELECT
	asset_under_management.`status`, 
	asset_under_management.currency, 
	avg(asset_under_management.amount) as 'TOTAL'
    FROM
	invoice,
	asset_under_management
    WHERE asset_under_management.status = 'OK'
    GROUP BY currency
    '''
    
    print("===== Report 2=====")
    print("What is the average amount of assets (in currency) for the entire client list?")
    cursor.execute(query)
    report2 = cursor.fetchall()
    for results  in report2:
        print(f"Answer: {results[1]} ${str(round(results[2],2))} \n")


    # Report 3
    query ='''
    SELECT
	`transaction`.client_id,
	client.`name`,
	count( `transaction`.client_id ) AS count 
    FROM
	`transaction`
	INNER JOIN client ON client.client_id = `transaction`.client_id 
    WHERE
	( transaction_date < CURRENT_DATE () - INTERVAL 1 MONTH ) 
	AND ( TRANSACTION.`status` = 'OK' ) 
    GROUP BY
	client_id 
    HAVING
	count( TRANSACTION.client_id ) > 10
    '''
    print("===== Report 3=====")
    print("How many clients have a high number (more than 10 a month) of transactions?")
    cursor.execute(query)
    report3 = cursor.fetchall()
    print("Answer: ",cursor.rowcount," clients\n")

 
# Managing connection exceptions and close DB connection
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied user name or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()