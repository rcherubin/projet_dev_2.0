import sqlite3
connection = sqlite3.connect('gameDB.db')

cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Highscores
  (
        PlayerName    TEXT,
        PlayerScore    INT
  ); 
    '''
    )
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS ConfigurationP2
#   (
#         Player2Name    TEXT,
#         Player2Lives    INT,
#         Player2HP    INT,
#         Player2Dmg    INT,
#         Player2AtkSpeed    INT,
#         Player2Speed    INT
#   ); 
#     '''
#     )
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS ConfigurationP1
#   (
#         Player1Name    TEXT,
#         Player1Lives    INT,
#         Player1HP    INT,
#         Player1Dmg    INT,
#         Player1AtkSpeed    INT,
#         Player1Speed    INT
#   );
#     '''
#     )
def insertWinner(player):
    connection = sqlite3.connect('gameDB.db')
    cursor = connection.cursor()
    Game = (player.name,player.score)
    cursor.execute('INSERT INTO Highscores VALUES (?,?)', Game)
    connection.commit()
def getScores():
    connection = sqlite3.connect('gameDB.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Highscores order by PlayerScore DESC")
    record = cursor.fetchall()
    connection.close()
    return record

