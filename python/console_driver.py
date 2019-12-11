#!/usr/bin/python3
# console_ui.py

from src.Infrastructure.CallApi import call_api
from src.Logic.TVShow import TVShow


def main():
    try:
        call_api_Flag, loopAgain = (True, True)
        session_show = TVShow('')

        while loopAgain:
            if call_api_Flag:
                title = input("Enter a TVShow: ")
                json = call_api(title)
                session_show = TVShow(json)
            else:
                pass

            print(f'Random Season and Episode for {title}: '
                  f'{session_show.get_random_pair()}')

            while True:
                text = input('Would you like to get another pair for the '
                             'same show, search a new show, or exit? enter '
                             '(same, new, exit): ')

                if text not in ['', 'same', 'new', 'exit']:
                    print('Invalid Input, try again!')
                    continue

                if text in ('', 'same'):
                    call_api_Flag = False
                elif text == 'new':
                    call_api_Flag = True
                else:
                    loopAgain = False

                break
    except Exception as exc:
        print(exc)

    print('GoodBye ~')
# end main()


if __name__ == '__main__':
    main()
