
'''
    Invex-Improved v0.1 (beta) by 1LIA5

    Original Invex written by steelinferno
    Python 3 needed for Invex-Improved
'''

from sys import argv, exit
import requests
from json import decoder
from datetime import timedelta
import os
import platform
import pyperclip

VIEWS = '👀'
LENGTH = '⏱ '
PROMPT = '>> '
URL = 'https://invidious.osi.kr/'
# declare variables for the search result loop
NUM = []  # reference number to the URL on the printed list
TITLE = []  # title of the reference
k = -1  # reference number
PREFIX = ' '  # to align results evenly

#Macbook
def mac():
    try:
        if os.system(f"mpv {NUM[int(PICK)]}") != 0:
            mpv_install = input(f"{PROMPT}MPV not installed. Install MPV? ")
            if mpv_install.upper() == "Y":
                print(f"{PROMPT}MPV being installed with Brew..")
                os.system(' /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" ')
                os.system('brew install mpv')

            elif mpv_install.upper() == "N":
                exit()
            else:
                print("Invalid input")

    except:
        exit()

#Windows
def win():
    return 0

#Linux
def linux():
    return 0

if __name__ == "__main__":
    print('Invex - Invidious URL grabber')
    # Get user input
    if len(argv) > 1:
        ARGS = ' '.join(argv[1:])
        ISQ = ARGS.replace(' ', '+')  # ISQ = input search query
    else:
        print('\nInput search query:')
        ISQ = input(PROMPT).replace(' ', '+')

    # Get search query (SQ) URL
    SQ = URL + 'search?q=' + ISQ  # SQ = search query
    # Get API URL
    API = URL + 'api/v1/search?q=' + ISQ

    # Get API in json and check connection to API
    try:
        j = requests.get(API).json()
    except requests.exceptions.ConnectionError:  # no internet
        print('cannot connect to "' + URL + '", please try again later.')
        exit()
    except decoder.JSONDecodeError:  # invidious api is down
        print('Service is currently unavailable, please try again later.')
        exit()

    # Search trough json file and format
    for i in j:
        if k < 9:
            PREFIX = ' '
        else:
            PREFIX = ''
        k += 1
        print(PREFIX + str(k) + ' %s ' % (i['title']) + VIEWS + '%s ' % format(i['viewCount'], 'n') + LENGTH + '%s' % (
            str(timedelta(seconds=i['lengthSeconds']))))
        # index the URLs and titles to a number that can be called on later
        NUM.append(str(URL + 'watch?v=%s' % (i['videoId'])))
        TITLE.append(str(i['title']))

    print('\nPick a number to copy URL and play in MPV:')
    PICK = input(PROMPT)

    if platform.system() == "Darwin":
        pyperclip.copy(NUM[int(PICK)])
        mac()
    else: print("This application is not yet available or your system.")


