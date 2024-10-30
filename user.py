import os, requests, time, json, random, discord, asyncio
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token, guild = config['User']['token'], config['User']['guild']
print(f"Token: {token}, Guild: {guild}")  # Verificar que el token y el guild se cargan correctamente

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix='q', case_insensitive=False, self_bot=True, intents=intents)
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
        os.remove('Core/userscrape.txt')

        with open('Core/userscrape.txt', 'a') as txt:
            for member in members:
                txt.write(str(member.id) + '\n')
            txt.close()
            await ban().thread()
    
    async def thread(self):
        print('\n [>] Banning...\n')
        with open('Core/userscrape.txt') as txt:
            for member in txt:
                member_id = member.strip()
                await self.mass(member_id)
    
    async def mass(self, member):
        try:
            response = requests.put(
                f'https://discord.com/api/v{random.choice([6, 7, 8, 9])}/guilds/{self.guild}/bans/{member}',
                headers={'Authorization': f'{self.token}'}
            )
            if response.status_code == 429:  # Rate limit hit
                retry_after = response.json().get('retry_after', 1)
                print(f"Rate limit hit, retrying after {retry_after} seconds")
                await asyncio.sleep(retry_after)
            else:
                await asyncio.sleep(1)  # Cooldown de 1 segundo entre cada baneo
        except Exception as e:
            print(f"Error al banear al miembro {member}: {e}")

if __name__ == '__main__':
    try:
        print("Iniciando el bot...")  # Verificar que el bloque if __name__ == '__main__' se ejecuta
        print(f"Token: {token}, Guild: {guild}")  # Verificar que el token y el guild se imprimen
        os.system('cls')
        client.run(token)
    except ImportError:
        print("ImportError: Instalando discord.py")  # Verificar si hay un problema de importación
        os.system('python -m pip install discord')
        client.run(token)
    except Exception as e:
        print(f"Error: {e}")  # Imprimir cualquier otra excepción
        input('\n [!] Invalid Token\n')