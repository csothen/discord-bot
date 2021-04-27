import json
import datetime
import utils


def cmd_hello(message):
    if message.author.id == 659356013773979648:
        return 'Bonjour {0.author.display_name}!'.format(message)
    else:
        return 'Hello {0.author.display_name}!'.format(message)


def cmd_bday(message):
    args = parse_args(message)
    if len(args) == 0:
        return 'You must provide your birthday date after the command'
    try:
        day, month, year = args[0].split('/')

        if utils.isValidDate(day, month, year):
            birthday = json.dumps({
                'id': message.author.id,
                'date': args[0]
            })
            utils.append_json('./assets/birthdays.json', birthday)
            return 'Your birthday was registered'
        else:
            return "The birthday date cant be set in the future (use the date you were born)"
    except Exception as e:
        print(e)
        return 'The birthday date must follow the format dd/MM/yyyy'


def default(message):
    command = message.content.split('$')[1].split(' ')[0]
    return 'Invalid command `{0}`'.format(command)


def parse_args(message):
    return message.content.split('$')[1].lower().split(' ')[1:]
