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
		# Creating the tables if not exists
		self.__create_table_users()

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
			Log.log_info(get_value_by_key('SQL', 'TABLE_CREATED').format('users'))
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

	def get_rows_from_table(self, table) -> tuple:
		try:
			cur = self.con.cursor()
			cur.execute(f"""SELECT * FROM {table};""")
			return cur.fetchall()
		except Exception as e:
			Log.log_crit(e)
			return None
