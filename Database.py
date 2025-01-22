import pymssql

conn = pymssql.connect(server="localhost", database="MyDb")
try:
    cursor = conn.cursor()  
    cursor.execute("SELECT TOP 10 * FROM CityType")
    print(cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
        row = cursor.fetchone()
finally:
    conn.close()
    
print("\n==================================================\n")