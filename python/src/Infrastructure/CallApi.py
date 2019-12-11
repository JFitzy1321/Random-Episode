#!/usr/bin/python3
# CallApi.py
import requests


def call_api(title: str):
    title = title.replace(' ', '+')
    id = _get_id(title)
    if id == -1:
        pass  # TODO implement this later

    json_str = __get_show_info(id)
    if not json_str:  # string are 'fasly'
        pass  # TODO implement this later
    else:
        return json_str


def _get_id(title: str):
    tvmaze_url = f"http://api.tvmaze.com/singlesearch/shows?q={title}"

    try:
        response = requests.get(tvmaze_url)  # .get(url)

        if response.status_code == 200:
            # comparing the title of the show in the josn object to
            # the formatted name in the class
            _json = response.json()

            return _json.get('id')
    # if status code was not 200, then something went wrong
        else:
            return -1

    except:
        return -1


def __get_show_info(id):
    '''this method will extract the number of episode for each season from an
    api search and store it in this classes dictonary'''
    url = f'http://api.tvmaze.com/shows/{id}/episodes'

    response = requests.get(url)

    if response.status_code == 200:  # 200 = good search
        return response.json()
    else:
        return '\nID number not found.'
