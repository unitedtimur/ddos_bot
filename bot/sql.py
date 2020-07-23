import psycopg2
from log import Log
from parse_configuration import get_value_by_key

class SQL:
	con = None

	def __init__(self):
		self.con = psycopg2.connect(
			database="dbcb6tnm8m430r", 
			user="wnutffgmfmkgyv", 
			password="926a548165690ed9e50fde13e06124fab12e6904fa60659968eae5e70fa9cc4a", 
			host="ec2-54-75-244-161.eu-west-1.compute.amazonaws.com", 
			port="5432")
		Log.log_info(get_value_by_key('SQL', 'DATABASE_CONNECTED'))
		# Создаём таблицу, если не создана
		#self.__create_table_users()

	def __del__(self):
		self.con.commit()
		self.con.close()
		Log.log_info(get_value_by_key('SQL', 'DATABASE_DISCONNECTED'))

	def __create_table_users(self):
		try:
			cur = self.con.cursor()
			cur.execute('''
				CREATE TABLE IF NOT EXISTS users (
				user_id INTEGER PRIMARY KEY NOT NULL, 
				level VARCHAR(10) NOT NULL
				);
			''')
			Log.log_info(get_value_by_key('SQL', 'TABLE_INITIALIZED').format('users'))
		except Exception as e:
			Log.log_crit(e)

	def get_all_table_names(self):
		try:
			cur = self.con.cursor()
			cur.execute("""
				SELECT table_name FROM information_schema.tables
				WHERE table_schema = 'public';
			""")
			Log.log_info(get_value_by_key('SQL', 'GET_ALL_TABLE_NAMES'))
			return list(cur.fetchall())
		except Exception as e:
			Log.log_crit(e)
			return None

	def insert_into_user_table(self, row, table):
		try:
			cur = self.con.cursor()
			cur.execute("""
				INSERT INTO {0} VALUES({1}, '{2}');
			""".format(table, row[0], row[1]))
			Log.log_info(get_value_by_key('SQL', 'INSERT_INTO_USER_TABLE'))
		except Exception as e:
			Log.log_crit(e)

	def del_row_from_user_table(self, row):
		try:
			cur = self.con.cursor()
			cur.execute(f"""
				DELETE FROM users WHERE user_id = {row};
			""")
			Log.log_info(get_value_by_key('SQL', 'DEL_ROW_FROM_USER_TABLE').format(row))
		except Exception as e:
			Log.log_crit(e)

	def del_admin_from_user_table(self, user_id):
		try:
			cur = self.con.cursor()
			cur.execute(f"""
				UPDATE users SET level = 'user'
				WHERE user_id = {user_id};
			""")
			Log.log_info(get_value_by_key('SQL', 'DEL_ADMIN_FROM_USER_TABLE').format(user_id))
		except Exception as e:
			Log.log_crit(e)

	def find_admin(self, user_id):
		try:
			cur = self.con.cursor()
			cur.execute(f"""SELECT level FROM users WHERE user_id = {user_id};""")
			Log.log_info(get_value_by_key('SQL', 'FIND_ADMIN').format(user_id))
			return cur.fetchall()
		except Exception as e:
			Log.log_crit(e)

	def insert_into_users_if_not_exists(self, user_id):
		with self.con:
			with self.con.cursor() as cur:
				cur.execute("SELECT * FROM users WHERE user_id = %s;", (user_id, ))
				row = cur.fetchall()
				if len(row) == 0:
					cur.execute("INSERT INTO users VALUES(%s, %s);", (user_id, 'user'))
					Log.log_info(get_value_by_key('SQL', 'FIND_USER_AND_ADD').format(user_id))

	def get_rows_from_table(self, level) -> tuple:
		with self.con:
			with self.con.cursor() as cur:
				if level.lower() == 'all':
					cur.execute("SELECT * FROM users;")
				else:
					cur.execute("SELECT * FROM users WHERE level = %s;", (level, ))
				Log.log_info(get_value_by_key('SQL', 'GET_ROWS_FROM_TABLE'))
				return cur.fetchall()