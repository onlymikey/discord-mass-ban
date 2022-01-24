import os, requests, json, time, random, discord, asyncio, threading
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token, guild = config['Bot']['token'], config['Bot']['guild']
intents, intents.members = discord.Intents.all(), True
client = commands.Bot(command_prefix='q', case_insensitive=False, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    await ban().scrape()

class ban():
    def __init__(self):
        self.token = token
        self.guild = guild

    async def scrape(self):
        await client.wait_until_ready()
        ob = client.get_guild(int(self.guild))
        members = await ob.chunk()
        os.remove('core/botscrape.txt')

        with open('core/botscrape.txt', 'a') as txt:
            for member in members:
                txt.write(str(member.id) + '\n')
            txt.close()
            await ban().thread()
    
    async def thread(self):
        os.system('cls & mode 70, 40')
        txt = open('core/botscrape.txt')
        for member in txt:
            threading.Thread(target=self.mass, args=(self.guild, member,)).start() #error
        txt.close() # return
        input("\n [!] Finished...\n")

    async def mass(self, member):
        i, count, api = 0, 0, [6, 7, 8, 9]
        while True:
            r = requests.put(f'https://discord.com/api/v{random.choice(api)}/guilds/{self.guild}/bans/{member}', headers={'Authorization': f'Bot {token}'})
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    while i < count:
                        i+=1
                        print(' [%d] ' + member + ' has been read'%(i))
                    break
                else:
                    break # return thread()

if __name__ == '__main__':
    try:
        os.system('cls & mode 70, 12 & title mass ban │ by lozza (github.com/qro)')
        import discord
        client.run(token)
    except ImportError:
        os.system('python -m pip install discord')
        client.run(token)
    except:
        input('\n [!] Invalid Token\n')