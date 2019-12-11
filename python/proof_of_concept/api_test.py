# api_test.py

'''Purpose: testing the request library and how to
access the api i'm using for this project'''

# api for tv shows: api.tvmaze.com
# link to documentation is in source.txt
import requests

'''Addendum: A problem arose during my initial queries of the tvmaze api
If a season is still being aired, then the season json query will set a null
valuefor the number of episode for that still running season.

To fix this, i will have to query the full episode list for the tv show
'''


def seasons(_show_id):
    '''get the seasons information for a show from TVmaze api'''
    # this request should return a json with a list of seasons and number of
    # episodes per season
    _url = 'http://api.tvmaze.com/shows/{}/seasons'.format(_show_id)
    _response = requests.get(_url)
    with open('seasons_json.txt', 'w+') as _file:
        _file.write(_response.text)

    show_json = _response.json()
    for item in show_json:
        print('Season: %s Episode: %s' % (item.get('number'),
                                          item.get('episodeOrder')))


def main():
    '''main exectuable function'''
    # doing a "singlesearch" request to get the shows id
    url = 'http://api.tvmaze.com/singlesearch/shows?q=family+guy'
    response = requests.get(url)

    if response.status_code == 200:
        show_id = response.json().get('id')
        seasons(show_id)

    else:
        print('Page not found')

if __name__ == "__main__":
    main()
