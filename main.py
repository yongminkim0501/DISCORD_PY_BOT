from BotPykis import *
from bot import *
import discord, json

connect_pykis = get_set_connect_pykis()
connect_pykis.set_real_pykis("secret.json")

token = connect_discord("config.json")
discord_bot = set_discord()
discord_bot.set_discord_bot(connect_pykis)
discord_bot.start_client(token)
