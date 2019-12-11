# initalize__db.py
'''Purpose: create the database to hold shows alreeady watched'''


def main():
    '''main exectuable function'''
    import sqlite3
    import config

    try:
        conn = sqlite3.connect(config.db_path)
        curs = conn.cursor()

        curs.execute('''CREATE TABLE showsWatched(
                        name TEXT,
                        season INT,
                        episode INT )
                    ''')

        conn.commit()

    except sqlite3.Error as _e:
        print(_e)
    finally:
        conn.close()
        del sqlite3, config
