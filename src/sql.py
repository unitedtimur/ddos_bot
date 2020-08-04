import psycopg2


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

    def set_row_to_users(self, row):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"SELECT EXISTS(SELECT 1 FROM users WHERE user_id = '{row[0]}');")
            if cur.fetchone()[0] == False:
                cur.execute(f"INSERT INTO users(user_id, level) VALUES('{row[0]}', '{row[1]}');")

    def del_row_from_users(self, user_id):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"DELETE FROM users WHERE user_id = {user_id};")

    def set_row_to_white_list(self, number):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"INSERT INTO white_list(number) VALUES({number});")

    def del_row_from_white_list(self, number):
        with self.con, self.con.cursor() as cur:
            cur.execute(f"DELETE FROM white_list WHERE number LIKE '{number}';")