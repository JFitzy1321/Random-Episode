# console_test.py
''' This module is to test the functionality of the TVShow class in a console
    This is not the main executable, use main_gui.py as "__main__"
'''

from myLib.tv_class import TVShow, sqlite3

def menu():
    '''print header info to user'''
    print('Joseph Fitzgibbons, FitzgibbonsP13, Final Project')
    print('Welcome to my SUPER AMAZING EPISODE SHUFFLER!!!!')
    # instructions and commands

def show_db():
    '''get everything from the database and show to user'''
    try:
        path = TVShow.db_path() # this is a call to a "static" class method
        conn = sqlite3.connect(path)
        curs = conn.cursor()

        curs.execute('SELECT * FROM showsWatched')
        rows = curs.fetchall()
        conn.commit()

        print()
        if not rows:
            print('Database is empty.')
        for row in rows:
            # printing the show name, season and episode already watched
            print('Show: {} Season {}, Episode {}'.format(row[0].replace('+', ' '), row[1], row[2]))

    except sqlite3.Error as _e:
        print(str(_e))
    except Exception as _e:
        print(str(_e))
    finally:
        conn.close()
def full_clear_db():
    try:
        path = TVShow.db_path()
        conn = sqlite3.connect(path)
        curs = conn.cursor()

        curs.execute('DELETE FROM showsWatched')
        conn.commit()
    except sqlite3.Error as _e:
        print(_e)
    finally:
        conn.close()
def main():
    '''main executable function'''
    menu()

    show = TVShow()

    answer = 'yes'
    while answer == 'yes' or answer == 'y':

        print('\nEnter that name of a show to watch, or enter "clear" to '\
                'delete show from database,\n"show list" to see '\
                'everything in the database, or "exit".'
        )
        user_input = input('>>>> ')

        if user_input == 'show list':
            show_db()
            continue

        elif user_input == 'clear':
            flag = show.clear_db()
            if isinstance(flag, str):
                print(flag)
            else:
                print('Show successfully cleared from the database!')
            continue

        elif user_input == 'delete':
            full_clear_db()
            continue

        elif user_input == 'exit':
            break

        show.set_name(user_input)

        # this function will return a string if something went wrong getting everything
        flag = show.get_info()
        if isinstance(flag, str) is True:
            print(flag)
            continue

        combo = show.next_combo()
        if isinstance(combo, str) is True:
            print(combo)
            continue
        else:
            print('Goto Season %s Episode %s' % (combo[0], combo[1]))

        answer = input('Do another? y/n: ')

    print('Goodbye. ~ Joe Fitzgibbons')

if __name__ == '__main__':
    main()
