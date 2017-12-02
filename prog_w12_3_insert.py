''' any way to connect sql not from PyMySQL but through mysql.connector ''' 
import pymysql 
conn = pymysql.connect("localhost","root","data","TESTDB") 

cur = conn.cursor()
sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, GENDER, SALARY) 
					  VALUES ('Mac', 'Mohan', 20, 'M', 2000),
					  ('Jan', 'Lucy', 40, 'F', 2555)"""
					  
try: 
	# Execute the SQL command 
	cur.execute(sql) 
	# Commit your changes in the database 
	conn.commit() 
	
except: 
# Rollback in case there is any error c
	onn.rollback() 
	
	
# disconnect from server
conn.close()