import sqlite3

connection = sqlite3.connect('student.db')

cursor = connection.cursor()

table_info = ''' CREATE TABLE STUDENT(NAME VARCHAR(25),
CLASS VARCHAR(25) , SECTION VARCHAR(25), MARKS INT)'''

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES('SHASHANK','Data Science','B',94) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('PRASHANT','Data Analytics','B',98) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('LUCKY','Data Engineeri','C',100) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('NIDHI','Data Science','C',64) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('DHONI','Software Engineer','  A',84) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('ROHIT','Data Managment','A',74) ''')

print('The Inserted Records are: ')
data=cursor.execute('SELECT * FROM STUDENT')
for row in data:
    print(row)

connection.commit()
connection.close()