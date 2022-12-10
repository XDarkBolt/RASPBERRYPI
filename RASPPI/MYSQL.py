import mysql.connector

mydb = mysql.connector.connect(
  host="94.73.151.62",
  user="u9737940_r_pi_4",
  database="u9737940_pi4",
  password="TZaq04G4HKdl53G"
)

# creating database_cursor to perform SQL operation
db_cursor = mydb.cursor()
# executing cursor with execute method and pass SQL query
#db_cursor.execute("INSERT INTO `test_pi`(`ID`, `NAME`, `VAR1`, `VAR2`) VALUES (5,'SAM',1,1)")
db_cursor.execute("SELECT (VAR1) FROM `test_pi` WHERE (NAME) = 'GIMLI'")
#print all databases
for db in db_cursor:
    if db[0] == 1: print("SS")
    else:
        print(db)