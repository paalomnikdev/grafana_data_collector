import os
from dotenv import load_dotenv
import click
import pymysql.cursors
import discord
import asyncio
from etcmc import Etcmc
from pprint import pprint as pp

load_dotenv()

connection = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    database=os.getenv('DB_NAME'),
)

class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        
        guild = self.get_guild(int(os.getenv('SERVER_ID')))
        if not guild:
            print("Guild (server) not found.")
            await self.close()
            return

        channel = guild.get_channel(int(os.getenv('ETC_CHANNEL_ID')))
        if not channel:
            print("Channel not found.")
            await self.close()
            return

        await channel.send(os.getenv('message'))
        await self.close()

@click.group()
def cli():
    pass

@cli.command()
def health():
    print('health')

@cli.command()
def count_etcmc_nodes():
    Etcmc(connection).store_nodes_count()

@cli.command
def discord_update():
    etcmc = Etcmc(connection)
    os.environ['message'] = etcmc.get_discord_message()
    client = DiscordClient(intents=discord.Intents.default())
    asyncio.run(client.start(os.getenv('DISCORD_TOKEN')))

if __name__ == '__main__':
    cli()
