class Color:
    reset = '\u001b[0m'
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'


class BgColor:
    black = '\u001b[40m'
    red = '\u001b[41m'
    green = '\u001b[42m'
    yellow = '\u001b[43m'
    blue = '\u001b[44m'
    magenta = '\u001b[45m'
    cyan = '\u001b[46m'
    white = '\u001b[47m'


class TextStyle:
    none = ''
    bold = '\u001b[1m'
    underline = '\u001b[4m'
    reverse = '\u001b[7m'


def yesnoquestion(question):
    answer = input(question + '[y/n]').lower()
    if answer == 'yes':
        answer = True
    elif answer == 'y':
        answer = True
    elif answer == 'no':
        answer = False
    elif answer == 'n':
        answer = False
    else:
        print('Unknown response. Try yes or no!')
        yesnoquestion(question)
    return answer
