import psycopg2

from src import config


class SQL:
    def __init__(self):
        self.con = psycopg2.connect(database="bot-test",
                                    host="localhost",
                                    user="postgres",
                                    password="masterkey",
                                    port=5433)
        self.con.autocommit = True

    def __del__(self):
        self.con.close()

    def init_tables(self):
        self.__create_users_table()
        self.__create_white_list_table()
        print("Tables has been initialized...")

    def __create_users_table(self):
        with self.con, self.con.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY NOT NULL, 
				level VARCHAR(10) NOT NULL);''')

    def __create_white_list_table(self):
        with self.con, self.con.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS white_list (
                id SERIAL PRIMARY KEY NOT NULL,
                number VARCHAR(30) NOT NULL);''')

    def get_rows_from_table(self, table: str):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table};")
            return cur.fetchall()

    def set_row_to_users(self, user_id: str, level: str):
        if level.lower() in config.levels:
            with self.con, self.con.cursor() as cur:
                cur.execute(f"SELECT EXISTS(SELECT 1 FROM users WHERE user_id = {user_id});")
                if cur.fetchone()[0] == False:
                    cur.execute(f"INSERT INTO users(user_id, level) VALUES('{user_id}', '{level.lower()}');")

    def del_row_from_users(self, user_id):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"DELETE FROM users WHERE user_id = {user_id};")

    def set_row_to_white_list(self, number):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"INSERT INTO white_list(number) VALUES({number});")

    def del_row_from_white_list(self, number):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"DELETE FROM white_list WHERE number LIKE '{number}';")

    def change_level_in_users(self, user_id: str, newlevel: str):
        if newlevel.lower() in config.levels:
            with self.con, self.con.cursor() as cur:
                cur.execute(f"UPDATE users SET level = '{newlevel.lower()}' WHERE user_id = {user_id};")

    def get_rows_from_users(self, level: str = "all"):
        with self.con, self.con.cursor() as cur:
            if level.lower() in config.levels:
                cur.execute(f"SELECT * FROM users WHERE level LIKE '{level.lower()}';")
            else:
                cur.execute("SELECT * FROM users;")
            return cur.fetchall()

    def get_user_from_users(self, user_id: str):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"SELECT * FROM users WHERE user_id = {user_id};")
            return cur.fetchone()