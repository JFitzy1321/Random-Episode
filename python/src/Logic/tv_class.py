#!/usr/bin/env python3
# tv_class.py

import sqlite3
import random
import requests
from ..Infrastructure import config

random.seed(None)


class TVShow(dict):
    '''I needed this class to inherent from the dict object because
    AttributeErrors kept popping up whenever i tried todo anything
    with the dictionary inside this class'''
    __DB_PATH__ = config.db_path
    __PIC_PATH = config.pic_path
    # I'm not entirely sure why, but I need these two arguments for
    # 'dict super()'

    def __init__(self, *args, **kwargs):
        # call to dict constructor
        super(TVShow, self).__init__(self, *args, **kwargs)
        self.name = ''  # name of the show the user inputs
        self.__format_name = ''  # name of the show for url call to api
        # api utilizes ID numbers for seasons and episode information
        self.show_id = None
        # dictionary holds number of seasons and episodes for each season
        self.__show_dict = {}
        self.__exclusion_list = []  # seasons and episode already watched
        self.__rand_se_ep = ()  # randomly chosen season and episode combo
        self.pic_url = ''  # url to jpg image from api json

        self.__check_db_exists()

    def __repr__(self):
        _str = ''
        for i in range(1, len(self.__show_dict)):
            _str += '\nSeason %s has %s Episodes.' % (i, self.__show_dict[i])

        return _str

    def __del__(self):
        import os
        os.remove(self.__PIC_PATH)
        del os

    # region 'Static methods'
    @classmethod
    def db_path(cls):
        '''This is essentially a static method to get the database path'''
        return cls.__DB_PATH__

    @classmethod
    def pic_path(cls):
        '''static method to get the picture path'''
        return cls.__PIC_PATH
    # endregion

    # region Public Methods
    def set_name(self, _name):
        '''Method takes the string the user enters and formats it into
            a url friendly string'''
        self.name = _name
        self.__format_name = _name.lower().strip(' ,.').replace(' ', '+')
        # since the user is entering a new title to search for
        # i need to recreate the exclusion list and the dictonary,
        # because the both are holding info from the previous title
        self.__show_dict.clear()
        self.__get_list_from_db()

    def get_info(self):
        '''This is the main method that the GUI will interface with
        This method will call of the other functions and either return
        a string if something went wrong, or return True if everything goes
        right'''
        flag = self.__get_id()
        if flag is not True:
            return flag

        flag = self.__get_show_info()
        if flag is not True:
            return flag

        return True

    def next_combo(self):
        if not self.__show_dict:
            return False
        '''This is the method that will spit out a random combination'''
        flag = self.__get_random_combo()
        if isinstance(flag, str) is True:
            return flag
        else:
            return self.__rand_se_ep

    def get_pic(self):
        '''using the url from the api show search to extract a jpg image
        '''
        if self.pic_url == '':
            return False
        try:
            import urllib

            urllib.request.urlretrieve(self.pic_url, self.__PIC_PATH)
            return True
        except:
            return False
        finally:
            del urllib

    def show_db(self):
        '''this method gets everything stored in the database
        if the database is empty, this method returns a None value
            '''
        try:
            conn = sqlite3.connect(self.__DB_PATH__)
            curs = conn.cursor()

            curs.execute('SELECT * FROM showsWatched')

            rows = curs.fetchall()
            conn.commit()

            if not rows:  # checking if rows is empty
                return None
            _list = []
            for row in rows:
                _name = row[0].replace('+', ' ').title()
                _str = 'Tile: %s. Episode Watched: Season %i, Episode %i\n' \
                    % (_name, row[1], row[2])
                _list.append(_str)
            return _list
        except:
            return False
        finally:
            conn.close()

    def clear_db(self):
        '''deletes everything from the database with the name stored
        in format_name'''
        if self.show_id is None:
            return "\nCan't clear a title from the database until a valid "\
                "name is entered."
        try:
            conn = sqlite3.connect(self.__DB_PATH__)
            curs = conn.cursor()

            curs.execute('DELETE FROM showsWatched WHERE name=?',
                         (self.__format_name,))
            conn.commit()
            self.__exclusion_list = []
            return True
        except sqlite3.Error as _e:
            return '\nSomething went wrong clearing the database!'
        finally:
            conn.close()

    # endregion

    # region Private Methods
    def __check_db_exists(self):
        from os.path import isfile
        from ..Infrastructure import initalize_db

        if isfile(self.__DB_PATH__):
            return
        else:
            initalize_db.main()  # initalize the database

        del isfile, initalize_db

    def __get_id(self):
        if self.__format_name == '' or self.__format_name.find(' ') > -1:
            return "\nShow Title not formatted properly"

        url = 'http://api.tvmaze.com/singlesearch/shows?q=%s'\
            % (self.__format_name)

        response = requests.get(url)

        if response.status_code == 200:
            # comparing the title of the show in the josn object to
            # the formatted name in the class
            _json = response.json()
            _title = _json.get('name')

            _title = _title.lower().strip(' ,.').replace(' ', '+')

            if _title != self.__format_name:
                return "\nBad Search results, search result title does"\
                    " not match entered title."

            self.show_id = _json.get('id')
            self.pic_url = _json['image']['medium']
            return True
        # if status code was not 200, then something went wrong
        else:
            self.show_id = None
            return '\nThe Title you enterd was not found!'

    def __get_show_info(self):
        '''this method will extract the number of episode for each season
        from an api search and store it in this classes dictonary'''
        url = 'http://api.tvmaze.com/shows/{}/episodes'.format(self.show_id)

        response = requests.get(url)

        if response.status_code == 200:  # 200 = good search

            # delete everything in the dictionary
            self.__show_dict.clear()

            json_obj = response.json()
            new_dict = {}
            for item in json_obj:
                number = item.get('season')
                # if the key already exists, increment it by one
                try:
                    new_dict[number] += item.get()
                # key does not exit, set it to 1
                except:
                    new_dict.setdefault(number, 1)
            # setting the the number of seasons into the dictionary
            new_dict['numSeasons'] = number

            # setting the newly created dictionary into the classes dictionary
            self.__show_dict.update(new_dict)
            return True
        else:
            return '\nID number not found.'

    def __get_random_combo(self):
        # utilizing a limiter to prevent an infinite loop
        limit = self.__get_limiter()
        if limit == 0:
            limit = 50
        counter = 0
        while True:
            # use random library to get a random seaosn
            # and episode from the dictonary
            rand_season = random.randint(1, self.__show_dict['numSeasons'])
            rand_episode = random.randint(1, self.__show_dict[rand_season])

            self.__rand_se_ep = (rand_season, rand_episode)
            # checking if the random combo is present within the exlcusion list
            # the exclusion list holds combos already watched
            if self.__rand_se_ep in self.__exclusion_list:
                counter += 1
                if counter == limit:
                    return 'Search limit has bee reached. Please clear the"\
                        " database.'
            else:
                self.__add_ep_to_db()
                return True

    def __get_limiter(self):
        count = 0
        for i in range(1, len(self.__show_dict)):
            count += self.__show_dict[i]
        return count

    def __get_list_from_db(self):
        try:
            conn = sqlite3.connect(self.__DB_PATH__)
            curs = conn.cursor()

            curs.execute('SELECT season, episode FROM showsWatched '
                         'WHERE name=?', (self.__format_name,))
            rows = curs.fetchall()
            conn.commit()

            if not rows:  # checking if rows is empty
                self.__exclusion_list = []
            else:
                for row in rows:
                    _tup = (row[0], row[1])
                    self.__exclusion_list.append(_tup)

            return True
        except sqlite3.Error as _e:
            return '\nSomething went wrong accessing the database.'
        finally:
            conn.close()

    def __add_ep_to_db(self):
        try:
            conn = sqlite3.connect(self.__DB_PATH__)
            curs = conn.cursor()

            curs.execute(
                '''INSERT INTO showsWatched(name, season, episode)
                VALUES ('%s', %i, %i)''' %
                (self.__format_name, self.__rand_se_ep[0],
                 self.__rand_se_ep[1]))
            conn.commit()
        except sqlite3.Error as _e:
            print(_e)
        finally:
            conn.close()

        if self.__rand_se_ep not in self.__exclusion_list:
            self.__exclusion_list.append(self.__rand_se_ep)
    # endregion
# End of class
