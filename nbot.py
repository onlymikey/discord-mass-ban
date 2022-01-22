import os, sys, requests, json, time, discord, asyncio, threading 
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token, guild = config['Bot']['token'], config['Bot']['guild']
intents, intents.members, headers = discord.Intents.all(), True
client = commands.Bot(command_prefix='q', case_insensitive=False, intents=intents)
client.remove_command('help')
membercount = 0

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
    
    async def thread(self):
        txt = open('core/botscrape.txt')
        for member in txt:
            threading.Thread(target=ban().mass(), args=(self.guild, member,)).start()
        txt.close()
        input(" [!] Finished...\n")
        exit()

    def mass(self, member):
        i = 0
        while True:
            r = requests.put(f'https://discord.com/api/v8/guilds/{guild}/bans/{member}', headers={'Authorization': f'Bot {token}'})
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    while i < membercount:
                        i+=1
                        if i == 1:
                            print(' [>] %d user has been banned'%(i))
                        else:
                            print(' [>] %d users has been banned'%(i))
                    break
                else:
                    break

if __name__ == '__main__':
    try:
        os.system('cls & mode 70, 12 & title mass ban │ by lozza (github.com/qro')
        import discord
        client.run(token)
    except ImportError:
        os.system('python -m pip install discord')
    except:
        input('\n [!] Invalid Token\n')