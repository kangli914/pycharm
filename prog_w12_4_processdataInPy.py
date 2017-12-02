import pymysql 
# Open database connection 
conn = pymysql.connect("localhost","root","data","TESTDB" ) 

# prepare a cursor object using cursor() method 
cur = conn.cursor() 

# Prepare SQL query to INSERT a record into the database. 
sql = "SELECT * FROM EMPLOYEE"

try: 
	# Execute the SQL command 
	cur.execute(sql) 
	# Fetch all the rows in a list of lists. 
	resultset = cur.fetchall()
	
	count= cur.rowcount 
	print (resultset, count)
	for row in resultset: 
		fname = row[0]
		lname = row[1] 
		age = row[2] 
		gen = row[3] 
		sal = row[4] 
		# Now print fetched result 
		print ("fname=%s,lname=%s,age=%d,gen=%s,sal=%d" % (fname, lname, age, gen, sal))
except: 
	print ("Error: unable to fecth data") 

# disconnect from server 
conn.close()