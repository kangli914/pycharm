import pymysql 
conn = pymysql.connect("localhost","root","data","TESTDB") 
cur = conn.cursor() 
cur.execute("DROP TABLE IF EXISTS EMPLOYEE") 
sql = """CREATE TABLE EMPLOYEE ( 
			FIRST_NAME CHAR(20) NOT NULL, 
			LAST_NAME CHAR(20), 
			AGE INT, 
			GENDER CHAR(1), 
			SALARY FLOAT )"""
try: 
	# Execute the SQL command 
	cur.execute(sql) 
	# Commit your changes in the database 
	conn.commit() 
except: 
	# Rollback in case there is any error 
	conn.rollback() 
	
# disconnect from server 
conn.close()