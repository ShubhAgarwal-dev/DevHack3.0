import email
import sqlite3
from os.path import isfile


class user_db():

    def __init__(self, db_path: str = r'../database/user.db') -> None:
        self.db_path = db_path
        if not isfile(path=db_path):
            self._make_database(self.db_path)

    @staticmethod
    def _make_database(db_path):
        connection = sqlite3.connect(db_path)
        connection.execute("""
            CREATE TABLE "users"(
	            "name"	TEXT,
	            "dob"	INTEGER,
	            "email"	TEXT,
	            "img"	INTEGER,
	            "password"	TEXT,
	            PRIMARY KEY("name")
            );
        
        """)
        connection.commit()
        connection.close()

    def add_user(self, user_name: str, dob: int, email: str, img_block_index: int, password: str):
        connection = sqlite3.connect(self.db_path)
        connection.execute(
            """
            INSERT INTO "users"("name","dob","email","img","password") VALUES(?,?,?,?,?)
            """, [str(user_name), int(dob), str(email), int(img_block_index), str(password)])
        connection.commit()
        connection.close()

    def check_user_img(self, user_name, password):
        connection = sqlite3.connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT "img" FROM "users" WHERE "name" = ? AND "password" = ?
        """, str(user_name), str(password))
        result = cursor.fetchall()
        return result[0][0]

    def check_user_img2(self, user_name):
        connection = sqlite3.connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT "img" FROM "users" WHERE "name" = ?
        """, str(user_name))
        result = cursor.fetchall()
        return result[0][0]


if __name__ == "__main__":
    user_database = user_db()
    name = 'AnuragGoel'
    dob = 19092003
    email_id = 'anuragoel@gmail.com'
    img_block_index = 1
    password = 12345678

    user_database.add_user('',)
