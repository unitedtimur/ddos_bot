import psycopg2, os

class SQL:
	con = None

	def __init__(self):
		self.con = psycopg2.connect(
			database	= os.environ['DATABASE'], 
			user		= os.environ['USER'], 
			password	= os.environ['PASSWORD'], 
			host		= os.environ['HOST'], 
			port		= os.environ['PORT'])

	def __del__(self):
		self.con.commit()
		self.con.close()

	def __create_table_users(self):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				cur.execute('''
					CREATE TABLE IF NOT EXISTS users (
					user_id INTEGER PRIMARY KEY NOT NULL, 
					level VARCHAR(10) NOT NULL
					);
				''')

	def __create_white_list(self):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				cur.execute('''
					CREATE TABLE IF NOT EXISTS white_list (
					user_id INTEGER PRIMARY KEY NOT NULL,
					number INTEGER NOT NULL,
					FOREIGN KEY (user_id) REFERENCES users (user_id)
					);
				''')

	def get_all_table_names(self):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				cur.execute("""
					SELECT table_name FROM information_schema.tables
					WHERE table_schema = 'public';
				""")

	def insert_into_user_table(self, row, table):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				cur.execute("""
					INSERT INTO {0} VALUES({1}, '{2}');
				""".format(table, row[0], row[1]))

	def insert_into_white_list(self, user_id, number):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				
				if self.find_number(number):
					return

				cur.execute(f"""INSERT INTO white_list(user_id, number) VALUES({user_id}, {number});""")

	def del_row_from_user_table(self, row):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				cur.execute(f"""
					DELETE FROM users WHERE user_id = {row};
				""")

	def del_admin_from_user_table(self, user_id):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				cur.execute(f"""
					UPDATE users SET level = 'user'
					WHERE user_id = {user_id};
				""")

	def find_admin(self, user_id):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				cur.execute(f"""SELECT level FROM users WHERE user_id = {user_id};""")
				return cur.fetchall()

	def find_number(self, number):
		with self.con:
			with self.con.cursor() as cur:
				cur = self.con.cursor()
				cur.execute(f"""SELECT number FROM white_list WHERE number LIKE '{number}';""")
				return cur.fetchall()

	def insert_into_users_if_not_exists(self, user_id):
		with self.con:
			with self.con.cursor() as cur:
				cur.execute("SELECT * FROM users WHERE user_id = %s;", (user_id, ))
				row = cur.fetchall()
				if len(row) == 0:
					cur.execute("INSERT INTO users VALUES(%s, %s);", (user_id, 'user'))

	def get_rows_from_table(self, level) -> tuple:
		with self.con:
			with self.con.cursor() as cur:
				if level.lower() == 'all':
					cur.execute("SELECT * FROM users;")
				else:
					cur.execute("SELECT * FROM users WHERE level = %s;", (level, ))
				return cur.fetchall()