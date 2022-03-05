import sqlite3
from os.path import isfile


class user_db():

    def __init__(self, db_path: str = r'database/user.db') -> None:
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

    def check_user(self, user_name, password):
        connection = sqlite3.connect()
        cursor = connection.cursor()
        cursor.execute("""

        """)
        # Just have to do some work
