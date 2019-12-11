#!/usr/bin/python3

# TVShow.py # refactored
# This class ONLY holds the season and episode pair list

import random


class TVShow():
    random.seed(None)

    def __init__(self, json_from_api):
        if len(json_from_api) <= 0:
            return
        self._season_episode_pair = {}  # equivalent to null colaesing
        self._selected_pairs = []
        self._current_pair = ()  # empty tuple
        self._length = 0
        self._total = 0

        self._create_season_episode_pairs(json_from_api)
    # end __init__

    def _create_season_episode_pairs(self, result_json):
        if not isinstance(result_json, list) or len(result_json) <= 0:
            raise TypeError("Null json string was sent to TVShow")

        self._season_episode_pair.clear()

        for item in result_json:

            if not item.get('season'):
                raise TypeError("Null in json from 'Season' lookup")
            else:
                season = item.get('season')

            try:
                self._season_episode_pair[season] += 1
                self._total += 1
            # key does not exit, set it to 1
            except:
                self._season_episode_pair.setdefault(season, 1)

        self._length = len(self._season_episode_pair)

    # end _create_season_episode_pair()

    def get_random_pair(self):
        if self._total < 0:
            return (-1, -1)

        while True:
            _rand_season = random.randint(0, self._length)
            _rand_episode = random.randint(0, self._season_episode_pair
                                           [_rand_season])

            self.__current_pair = (_rand_season, _rand_episode)

            if self.__current_pair in self._selected_pairs:
                continue
            else:
                self._selected_pairs += self.__current_pair
                return self.__current_pair

    # end get_random_pair()
