import os, sys, requests, json, discord, asyncio, threading 
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token, guild = config.get('bottoken'), config.get('botguilid')
intents, intents.members, headers = discord.Intents.all(), True, {'Authorization': f'Bot {token}'}
client = commands.Bot(command_prefix='l', case_insensitive=False, intents=intents)
client.remove_command('help')
i, membercount= 0, 0

@client.event
async def on_ready():
    await ban().main()

class ban():
    def __init__(self):
        self.token = token
        self.guild = guild

    def main(self):
        input("working ")

if __name__ == '__main__':
    try:
        os.system('cls & mode 70, 12 & title mass ban │ by lozza (github.com/qro')
        import discord
        client.run(token)
    except ImportError:
        os.system('python -m pip install discord')
    except:
        input('\n [!] Invalid Token\n')