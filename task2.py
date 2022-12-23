import requests
enable_game = dict()
str = 'USD'
def handle_game_proc(message):
    # global enable_game
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    lst = list(res['Valute'])
    try:
        # if enable_game[message.chat.id] and lst.count(message) > 0:
        if lst.count(message) > 0:
            return True
        else:
            return False
    except KeyError:
        enable_game[message.chat.id] = False

        # if enable_game[message.chat.id] and lst.count(message) > 0:
        if lst.count(message) > 0:
            return True
        else:
            return False

print(handle_game_proc(str))