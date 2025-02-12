import discord
import json
from BotPykis import *
# config.json 파일에서 토큰 읽기
def connect_discord(path):
    with open(path) as f:
        config = json.load(f)
        TOKEN = config['token']
    return TOKEN

class set_discord:
    def __init__(self):
        self.intents = None
        self.client = None
        self.pykis = None
        self.stock_data = None

    def set_discord_bot(self, connect_pykis):
        self.pykis = connect_pykis
        self.intents = discord.Intents.all()
        self.client = discord.Client(intents = self.intents)

        @self.client.event
        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return        
            # message.content로 메시지 내용만 전달
            stock_data = self.pykis.search_stock_name(message.content)
            self.stock_data = stock_data
            await message.channel.send(f"Stock data: {stock_data}")
    
    def get_stock_data(self):
        return self.stock_data

    def start_client(self, TOKEN):
        self.client.run(TOKEN)