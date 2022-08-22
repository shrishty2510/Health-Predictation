# # Import required modules
# import csv
# import sqlite3

# # Connecting to the geeks database
# connection = sqlite3.connect('health_prediction.db')

# # Creating a cursor object to execute
# # SQL queries on a database table
# cursor = connection.cursor()

# # Table Definition
# create_table = '''CREATE TABLE symptom_precaution(
				
# 				Disease TEXT ,
# 				Precaution_1 TEXT,
#                 Precaution_2 TEXT,
#                 Precaution_3 TEXT,
#                 Precaution_4 TEXT);
# 				'''

# # Creating the table into our
# # database
# cursor.execute(create_table)

# # Opening the person-records.csv file
# file = open('symptom_precaution.csv')

# # Reading the contents of the
# # person-records.csv file
# contents = csv.reader(file)

# # SQL query to insert data into the
# # person table
# insert_records = "INSERT INTO symptom_precaution (Disease,Precaution_1,Precaution_2,Precaution_3,Precaution_4) VALUES(?,?,?,?,?)"

# # Importing the contents of the file
# # into our person table
# cursor.executemany(insert_records, contents)

# # SQL query to retrieve all data from
# # the person table To verify that the
# # data of the csv file has been successfully
# # inserted into the table
# select_all = "SELECT * FROM symptom_precaution"
# rows = cursor.execute(select_all).fetchall()

# # Output to the console screen
# for r in rows:
# 	print(r)

# # Committing the changes
# connection.commit()

# # closing the database connection
# connection.close()
