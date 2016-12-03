import pymysql 
# Open database connection 
conn = pymysql.connect("localhost","root","data","TESTDB" ) 


# prepare a cursor object using cursor() method 
cur = conn.cursor() 


# Prepare SQL query to DELETE required records #sql = "DELETE FROM EMPLOYEE WHERE AGE >= '%d'" % (40) 
sql = "DELETE FROM EMPLOYEE WHERE FIRST_NAME = '%s'" % ("Jan") 

if (cur.execute(sql)):
	print ("record is deleted")
	conn.commit()
else:
	print("record does not exit")


'''
try: 
	# Execute the SQL command 
	cur.execute(sql) 
	# Commit your changes in the database 
	conn.commit() 
except: 
	# Rollback in case there is any error 
	conn.rollback()#print ("not good") 
'''
	
# disconnect from server 
conn.close()