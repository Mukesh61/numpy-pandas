import sqlite3

conn = sqlite3.connect('logs.db')

df = pd.read_sql('select * from emp', conn)

len(df)
