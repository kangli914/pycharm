import pymysql
conn = pymysql.connect("localhost","root","data","TESTDB")

cur = conn.cursor()

# EXECUTE SQL query using execute() method
cur.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method
data1= cur.fetchone();

print ("database version: %s " % data1)

conn.close()