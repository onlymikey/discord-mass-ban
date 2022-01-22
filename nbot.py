import os, sys, requests, json, discord, asyncio, threading 

with open('config,json') as f:
    config = json.load(f)

token, guild = config.get('bottoken'), config.get('botguilid')
intents, intents.members, headers = discord.Intents.all(), True, {'Authorization': f'Bot {token}'}
client = commands.Bot(command_prefix='l', case_insensitive=False, intents=intents)
client.remove_command('help')
i, membercount= 0, 0

class ban():
    def __init__(self):
        self.token = token
        self.guild = guild

if __name__ == '__name__':
    try:
        import discord
        from discord.ext import commands
    except ImportError:
        os.system('python -m pip install discord')