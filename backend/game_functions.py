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

#hier logic fuer funktions





cursor.execute("SELECT* FROM Soccer_Player;")
row = cursor.fetchall()

for item in row:
   print(item)
