# api_episode_test.py

'''Purpose: Testing how to get episode information from the TVmaze api
from previous tests, i learned that currently running seasons of shows
will have null value for their number of episodes field.
To bypass this problem, i will getting a full epiosde list from the api
and looping through the result json to retrieve the information i need.
Mainly season number and episodes for that season
'''
import requests
''' Request is a great library for accessing REST api's
I don't have to do any of the headers or POST stuff, the libray handles that
for me. All i have to do is enter the correct url and check the status codes
'''


# initial query to get the shows ID number
# todo an episode list lookup for a show, the TVmaze api wants an id number
# instead of the name of the show
# to do this, i need to get the shows id by doing a 'show search'
# this will return a json with the information i need
def main():
    '''main executable function'''
    url = 'http://api.tvmaze.com/singlesearch/shows?q=family+guy'
    response = requests.get(url)

    if response.status_code == 200:
        # json objects behave just like dictonaries in python
        # so i can use the get method to get the id i need
        show_id = response.json().get('id')

        with open('show_search_json.txt', 'w+') as _file:
            # with will close the file for me
            _file.write(response.text)

        new_url = 'http://api.tvmaze.com/shows/{}/episodes'.format(show_id)
        new_response = requests.get(new_url)

        if new_response.status_code == 200:
            print('API successfully accessed!')

            with open('episode_json.txt', 'w+') as _file:
                _file.write(new_response.text)
        else:
            print('Episode list not found')

    else:
        print('Page not found')

if __name__ == '__main__':
    main()
