# Authors:      Andreas Arnet, Mick Welisevich, Michael Lohr, Shawn Roberts, Walter Dipping
# Date:         July 11, 2021
# Title:        Module 10 - Milestone #2
# Description:  Create tables; insert data; display data

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "echo_user",
    "password": "Colin",
    "host": "127.0.0.1",
    "database": "echo",
    "raise_on_warnings": True
}
try: 
    # Create connection
    db = mysql.connector.connect(**config)  
    cursor = db.cursor()

    # Drop tables  
    Sql0 ='''DROP TABLE IF EXISTS client, transaction, invoice, employee, asset_under_management;'''
    cursor.execute(Sql0, params=None, multi=False)

    # Create tables
    Sql1 ='''CREATE TABLE Client(
    client_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    address VARCHAR(40) NOT NULL,
    phone VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    relationship_manager INT NOT NULL,
    account_creation_date DATE NOT NULL,
    status VARCHAR(6) NOT NULL,
    PRIMARY KEY(client_id));
    '''

    cursor.execute(Sql1, params=None, multi=False)

    Sql2 ='''
    CREATE TABLE Transaction(
    transaction_id INT NOT NULL AUTO_INCREMENT,
    client_id INT NOT NULL,
    currency VARCHAR(3) NOT NULL,
    amount   INT NOT NULL,
    transaction_date DATE NOT NULL,
    status VARCHAR(6) NOT NULL,
    PRIMARY KEY(transaction_id));
    '''
    cursor.execute(Sql2, params=None, multi=False)

    Sql3 ='''
    CREATE TABLE Invoice(
    invoice_id INT NOT NULL AUTO_INCREMENT,
    client_id INT NOT NULL,
    currency VARCHAR(3) NOT NULL,
    amount   INT NOT NULL,
    date DATE NOT NULL,
    status VARCHAR(6) NOT NULL,
    PRIMARY KEY(invoice_id));
    '''
    cursor.execute(Sql3, params=None, multi=False)
    
    Sql4 ='''
    CREATE TABLE Employee(
    employee_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    position VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    phone INT NOT NULL,
    CFA_license_ID VARCHAR(10),
    status VARCHAR(6) NOT NULL,
    DB_privileges VARCHAR(10) NOT NULL,
    PRIMARY KEY(employee_id));
    '''
    cursor.execute(Sql4, params=None, multi=False)
    
    Sql5='''
    CREATE TABLE Asset_under_management(
    asset_id INT NOT NULL AUTO_INCREMENT,
    client_id INT NOT NULL,
    type VARCHAR(10) NOT NULL,
    currency VARCHAR(3) NOT NULL,
    amount INT NOT NULL,
    transaction_date DATE NOT NULL,
    status VARCHAR(6) NOT NULL,
    PRIMARY KEY(asset_id));
    '''
    cursor.execute(Sql5, params=None, multi=False)


    # Insert Statements to populate tables
    insert_employees = """
    INSERT INTO 
	`employee`(name, position, email, phone, CFA_license_ID, status, DB_privileges) VALUES
	('Jake Willson', 'CEO', 'jake@willson.com', '123456781', 1212121, 'active', 'SU'),
	('Ned Willson', 'CEO', 'ned@willson.com', '123456782', 1212122, 'active', 'SU'),
	('Phoenix Two Star', 'Assistant', 'phoenix@willson.com', '123456783', NULL, 'active', 'SU')
    """
    cursor.execute(insert_employees)
    
    insert_clients = """
    INSERT INTO Client(name, address, phone, email, relationship_manager,account_creation_date, status) VALUES
        ('Chandler', '1 Street', '888-888-8888', 'chandler@mail.com', 1, '20210610', 'Active'),
        ('Phoebe', '2 Street', '888-888-8888', 'Phoebe@mail.com', 2, '20210710', 'Active'),
        ('Rachel', '3 Street', '888-888-8888', 'Rachel@mail.com', 1, '20210410', 'Active'),
        ('Ross', '4 Street', '888-888-8888', 'Ross@mail.com', 1, '20210210', 'Active'),
        ('Monica', '5 Street', '888-888-8888', 'Monica@mail.com', 2, '20210913', 'Active'),
        ('Joey', '6 Street', '888-888-8888', 'Joey@mail.com', 1, '20210415', 'Active')
        ;"""
    cursor.execute(insert_clients)

    insert_transactions = """
    INSERT INTO `transaction`(client_id, currency, amount, transaction_date, status) VALUES
	(1,'USD', 1000, '2021-05-05', 'OK'),
	(2,'USD', 1300, '2021-05-06', 'OK'),
	(3,'USD', 2100, '2021-05-07', 'OK'),
	(4,'USD', 2200, '2021-05-08', 'OK'),
	(5,'USD', 3000, '2021-05-09', 'OK'),
	(6,'USD', 5000, '2021-05-10', 'OK');
    """
    cursor.execute(insert_transactions)

    insert_AuM = """
    INSERT INTO `asset_under_management`(client_id, currency, type, amount, transaction_date, status) VALUES
	(1,'USD', 'stocks', 500, '2021-05-06', 'OK'),
	(2,'USD', 'stocks',650, '2021-05-07', 'OK'),
	(3,'USD', 'commodity',1050, '2021-05-08', 'OK'),
	(4,'USD', 'ETF',1100, '2021-05-09', 'OK'),
	(5,'USD', 'crypto',1500, '2021-05-10', 'OK'),
	(6,'USD', 'stocks',2500, '2021-05-11', 'OK')
    """
    cursor.execute(insert_AuM)

    insert_invoices = """
    INSERT INTO `invoice`(client_id, currency, amount, date, status) VALUES
	(1,'USD', 120, '2021-06-06', 'paid'),
	(2,'USD', 150, '2021-06-07', 'paid'),
	(3,'USD', 550, '2021-06-08', 'unpaid'),
	(4,'USD', 100, '2021-06-09', 'unpaid'),
	(5,'USD', 200, '2021-06-10', 'unpaid'),
	(6,'USD', 250, '2021-06-11', 'unpaid')
    """
    cursor.execute(insert_invoices)
    
    # Alter table to add foreign keys
    Sql7 ='''
    ALTER TABLE Transaction
    ADD FOREIGN KEY(client_id)
    REFERENCES Client(client_id);
    '''
    cursor.execute(Sql7, params=None, multi=False)

    Sql8 ='''
    ALTER TABLE Asset_under_management
    ADD FOREIGN KEY(client_id)
	REFERENCES client(client_id);
    '''
    cursor.execute(Sql8, params=None, multi=False)

    # Query and display data
    print("===== EMPLOYEES =====")
    cursor.execute("SELECT * FROM Employee;")
    employees = cursor.fetchall()
    for employee  in employees:
        print(f"Employee ID: {employee[0]}")
        print(f"Name: {employee[1]}")
        print(f"Position: {employee[2]}")
        print(f"Email: {employee[3]}")
        print(f"Phone: {employee[4]}")
        print(f"CFA License ID: {employee[5]}")
        print(f"Status: {employee[6]}")
        print("")

    print("===== CLIENTS =====")
    cursor.execute("""SELECT client.*, employee.`name` as 'RM' FROM client
	INNER JOIN employee	ON client.relationship_manager = employee.employee_id""")
    clients = cursor.fetchall()
    for client_id, name, address, phone, email, relationship_manager, account_creation_date, status, RM  in clients:
        print("Client ID: {}".format(client_id))
        print("Name: {}".format(name))
        print("Address: {}".format(address))
        print("Phone: {}".format(phone))
        print("Email: {}".format(email))
        print(f"Relationship Manager: {relationship_manager} ({RM})")
        print("Account Creation Date: {}".format(account_creation_date))
        print("Status: {}".format(status))
        print("")

    print("===== TRANSACTIONS =====")
    cursor.execute("SELECT * FROM Transaction;")
    transactions = cursor.fetchall()
    for transaction_id, client_id, currency, amount, transaction_date, status  in transactions:
        print("Transaction ID: {}".format(transaction_id))
        print("Client ID: {}".format(client_id))
        print("Currency: {}".format(currency))
        print("Amount: {}".format(amount))
        print("Transaction Date: {}".format(transaction_date))
        print("Status: {}".format(status))
        print("")

    print("===== ASSET UNDER MANAGEMENT =====")
    cursor.execute("SELECT * FROM Asset_under_management;")
    asset_under_management = cursor.fetchall()
    for asset_id, client_id, type, currency, amount, transaction_date, status  in asset_under_management:
        print("Asset ID: {}".format(asset_id))
        print("Client ID: {}".format(client_id))
        print("Type: {}".format(type))
        print("Currency: {}".format(currency))
        print("Amount: {}".format(amount))
        print("Transaction Date: {}".format(transaction_date))
        print("Status: {}".format(status))
        print("")

    print("===== INVOICES =====")
    cursor.execute("SELECT * FROM Invoice;")
    invoices = cursor.fetchall()
    for invoice_id, client_id, currency, amount, date, status  in invoices:
        print("Invoice ID: {}".format(invoice_id))
        print("Client ID: {}".format(client_id))
        print("Currency: {}".format(currency))
        print("Amount: {}".format(amount))
        print("Date: {}".format(transaction_date))
        print("Status: {}".format(status))
        print("")
        
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