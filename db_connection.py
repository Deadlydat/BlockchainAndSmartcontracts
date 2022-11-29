import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'public.emmel-it.de,1533'
database = 'BlockchainAndSC'
username = 'BCandSC'
password = 'FHWS2022'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=no; UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()


# cursor.execute("CREATE TABLE TestTable(shares integer)")
# cursor.commit()



# count = cursor.execute("""
# INSERT INTO TestTable (shares)
# VALUES (?)""",
#                        1000000).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))


cursor.execute("SELECT* FROM TestTable;")
row = cursor.fetchone()
print(row[0])