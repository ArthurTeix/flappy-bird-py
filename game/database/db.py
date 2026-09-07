import sqlite3


def create_table():
    connection = sqlite3.connect('./game/database/rank.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def save_score(score):
    connection = sqlite3.connect('./game/database/rank.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO matches (score) VALUES (?)", (score,)) # Os ? garantem que o sqlite3 trata o valor como dado, nunca como código SQL

    connection.commit()
    connection.close()


def get_top5_score():
    connection = sqlite3.connect('./game/database/rank.db')
    cursor = connection.cursor()

    cursor.execute("SELECT score FROM matches ORDER BY score DESC LIMIT 5")
    top5 = cursor.fetchall()

    rank = []
    for t in top5:
        rank.append(t[0])

    connection.close()
    return rank
