import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","1234","parser" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO resume(SLno, File, Name, Email, Mobile, Designation, Education, Skills, Experience)
         VALUES (1, 'xyz', 'PV', 'sahil19893@gmail.com', 1111120000, 'ABC', 'BE', 'Py', '2 years')"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except Exception as e:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
