import os
import schedule
import datetime
import json
import discord
from dotenv import load_dotenv

ANNOUNCEMENTS_CHANNEL_ID = 835549538889891870


def check_birthday():
    load_dotenv()
    client = discord.Client()
    client.run(os.getenv('TOKEN'))

    with open('./assets/birthdays.json') as f:
        birthdays = json.load(f)
        channel = client.get_channel(ANNOUNCEMENTS_CHANNEL_ID)
        for b in birthdays:
            day, month, year = b['date'].split('/')
            bday = datetime.datetime(int(year), int(month), int(day))
            if bday == datetime.datetime.today():
                user = client.get_user(b['id'])
                channel.send("Happy Birthday {0}!".format(user.mention))


schedule.every().hour.do(check_birthday)
