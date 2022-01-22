import os, sys, requests, json, discord, asyncio, threading 
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token, guild = config['Bot']['token'], config['Bot']['guild']
intents, intents.members, headers = discord.Intents.all(), True, {'Authorization': f'Bot {token}'}
client = commands.Bot(command_prefix='q', case_insensitive=False, intents=intents)
client.remove_command('help')
i, membercount= 0, 0

@client.event
async def on_ready():
    await ban().main()

class ban():
    def __init__(self):
        self.token = token
        self.guild = guild
        self.membercount = membercount

    async def guild(self): # scrape
        await client.wait_until_ready()
        ob = client.get_guild(self.guild)
        members = await ob.chunk()
        os.remove('core/botscrape.txt')

        with open('core/botscrape.txt', 'a') as txt:
            for member in members:
                txt.write(str(member.id) + '\n')
            txt.close()
            await ban().thread()
    
    async def thread():
        txt = open('core/botscrape.txt')
        for member in txt:
            threading.Thread(target=mass, args=(guild, member,)).start()
        txt.close()
        
if __name__ == '__main__':
    try:
        os.system('cls & mode 70, 12 & title mass ban │ by lozza (github.com/qro')
        import discord
        client.run(token)
    except ImportError:
        os.system('python -m pip install discord')
    except:
        input('\n [!] Invalid Token\n')