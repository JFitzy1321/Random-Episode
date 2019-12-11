# db_test.py

'''Purpose: testing various database scenarios'''

import sqlite3
from os.path import isfile
from src.config import db_path

if not isfile(db_path):
    from src.Infrastructure import initalize_db
    initalize_db.main()
    del initalize_db

conn = sqlite3.connect(db_path)
curs = conn.cursor()

curs.execute('SELECT * FROM showsWatched WHERE name=?', ('no name',))

rows = curs.fetchall()  # rows will have an empty list if query fails
conn.commit()

conn.close()

if not rows:  # checking if sequence is empty
    print('Empty list')
else:
    print(rows)
