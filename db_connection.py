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


# user table create und füllen
# cursor.execute("CREATE TABLE Users(user_id integer NOT NULL PRIMARY KEY, name varchar(15), user_name varchar(15), coins integer)")
# cursor.commit()

# count = cursor.execute("""
# INSERT INTO Users (user_id, name, user_name, coins) VALUES (?,?,?,?)""",1,"Peter Lustig","pLustig", 4000).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))

# count = cursor.execute("""
# INSERT INTO Users (user_id, name, user_name, coins) VALUES (?,?,?,?)""",2,"Max Musterman","musterm", 6000).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))



# cursor.execute("CREATE TABLE Team(team_id integer NOT NULL PRIMARY KEY, name varchar(25), points integer)")
# cursor.commit()

# count = cursor.execute("""
# INSERT INTO Team (team_id, name, points) VALUES (?,?,?)""",1,"Würzburg kicker", 20000).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))
#
# count = cursor.execute("""
# INSERT INTO Team (team_id, name, points) VALUES (?,?,?)""",2,"TSV Grombühl", 16000).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))


# cursor.execute("CREATE TABLE Soccer_Player(soccer_player_id integer NOT NULL PRIMARY KEY, name varchar(25), team_id integer, position integer, points integer)")
# cursor.commit()

#Hier muss noch für die Position eine Zahl festgelegt werden 1=torwart etc
# count = cursor.execute("""
# INSERT INTO Soccer_Player (soccer_player_id, name, team_id, position, points) VALUES (?,?,?,?,?)""", 1, "Walter", 2, 1, 50).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))
#
# count = cursor.execute("""
# INSERT INTO Soccer_Player (soccer_player_id, name, team_id, position, points) VALUES (?,?,?,?,?)""", 2, "Dieter", 2, 3, 70).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))
#
# count = cursor.execute("""
# INSERT INTO Soccer_Player (soccer_player_id, name, team_id, position, points) VALUES (?,?,?,?,?)""", 3, "Helmut", 1, 1, 60).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))



# cursor.execute("CREATE TABLE Statistics(statistics_id integer NOT NULL PRIMARY KEY, player_id integer, stakes integer, start_elf integer, yellow_cards integer, goals integer, assists integer)")
# cursor.commit()




cursor.execute("SELECT* FROM Soccer_Player;")
row = cursor.fetchall()

for item in row:
   print(item)

