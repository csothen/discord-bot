from cmds import *
import datetime
import json

ALLOWED_CHANNELS = ['bots']


def isAllowedChannel(channel):
    return channel.name in ALLOWED_CHANNELS


async def handle_message(message):
    command = message.content.split('$')[1].lower().split(' ')[0]

    switcher = {
        'hello': cmd_hello,
        'bday': cmd_bday
    }

    await message.channel.send(switcher.get(command, default)(message))


def isValidDate(day, month, year):
    date = datetime.datetime(int(year), int(month), int(day))
    return date <= datetime.datetime.today()


def append_json(filename, obj):
    with open(filename, 'r') as f:
        data = json.load(f)
        data.append(obj)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
