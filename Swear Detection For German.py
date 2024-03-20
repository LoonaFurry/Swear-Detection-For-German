import discord
from discord.ext import commands
import asyncio
import re

# Define the list of swear words
swear_words = [
    "abschaum", "affenschwanz", "ah du schwein", "alter muschi", "alter wichser", "am blitz geleckt haben",
    "analritter", "arsch", "arschficker", "arschfotze", "arschgeige", "arschgesicht", "arschkeks", "arschkriecher",
    "arschlecker", "arschloch", "auberfeiger", "aufgeilen", "backpfeifengesicht", "bastard", "bimbo", "blöde gans",
    "blöde stinkpot", "blödmann", "blödsinn", "bloede kuh", "blutige sau", "blvde fotze", "bonze", "bratze", "bruchbude",
    "bumsen", "das arschloch", "das ist mir scheißegal", "das miststück", "das schwein", "depp", "der dreckskerl",
    "der fotzenlecker", "der mist", "der mistkerl", "der wichser", "die drecksau", "die sau", "die verarsche", "dödel",
    "donnerwetter", "dreckige hure", "drecksack", "drecksau", "dreckskerl", "drecksnest", "du bastard", "du blöde kuh",
    "du fickfehler", "du hurensohn", "du Hurensohn", "du kannst mich mal", "du sau", "du schwein", "du weichei", "dummbatz",
    "dumme", "dumme kuh", "dumme nuss", "dummkopf", "dumpfbacke", "erarschen", "fahr zur holle", "feigling", "fick",
    "fick deine mutter", "fick dich", "fick dich arschloch", "fick dich in knie", "ficke", "ficken", "ficker", "filzlaus",
    "flachwichser", "flittchen", "fotze", "fratze", "geh zum teufel", "gottverdammt", "hackfresse", "halt deinen mund",
    "halt die fotze", "halt die klappe", "hat jemand dir ins gehirn geschissen", "hirnrissig", "homo", "hosenscheisser",
    "huhrensohn", "hure", "huren", "huren sohn", "hurensohn", "ich ficke deine mutter", "ich ficke deine schwester",
    "ich hasse dich", "ich will dich ficken", "ich will ficken", "idiot", "ische", "kackbratze", "kacke", "kacken",
    "kackwurst", "kampflesbe", "kanake", "kimme", "klugscheißer", "küss meinen arsch", "küss meinen arsch", "lech mien arsch",
    "leck mich", "leck mich am arsch", "lesbe", "lick", "lms", "lümmel", "lusche", "lutsch mein' schwanz", "lutsch' meine eier",
    "lutschen", "milf", "mist", "miststück", "möpse", "morgenlatte", "möse", "mufti", "muschi", "muschi lecker", "mutterficker"
]

# Initialize the bot
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} hat sich mit Discord verbunden!')
    await bot.change_presence(activity=discord.Game(name="Dein persönlicher Assistent für Discord"))
    while True:
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="Bereit, deine Fragen zu beantworten"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="Hier, um deine Discord-Erfahrung zu verbessern"))

# Event for when a message is sent
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message contains any swear words
    for word in swear_words:
        if word in message.content.lower():
            error_message = await message.channel.send(f"{message.author.mention}, deine Nachricht enthält unangemessene Sprache. Bitte verwende keine solchen Wörter.")
            await message.delete()
            await asyncio.sleep(10)
            await error_message.delete()
            return

    # Check for more subtle swear words using regular expressions
    pattern = r'\b\w*f\*\w*\b|\b\w*h\*\w*\b|\b\w*m\*\w*\b|\b\w*s\*\w*\b|\b\w*f\*t\w*\b|\b\w*w\*\w*\b|\b\w*s\*u\w*\b|\b\w*a\*\w*\b|\b\w*\*f\w*\b|\b\w*\*h\w*\b|\b\w*\*m\w*\b|\b\w*\*s\w*\b|\b\w*\*f\*t\w*\b|\b\w*\*w\w*\b|\b\w*\*s\*u\w*\b|\b\w*\*a\w*\b|\b\w*f\*\*\w*\b|\b\w*h\*\*\w*\b|\b\w*m\*\*\w*\b|\b\w*s\*\*\w*\b|\b\w*f\*t\*\*\w*\b|\b\w*w\*\*\w*\b|\b\w*s\*u\*\*\w*\b|\b\w*a\*\*\w*\b'
    if re.search(pattern, message.content.lower()):
        error_message = await message.channel.send(f"{message.author.mention}, deine Nachricht enthält unangemessene Sprache. Bitte verwende keine solchen Wörter.")
        await message.delete()
        await asyncio.sleep(10)
        await error_message.delete()

    await bot.process_commands(message)
bot.run('Your-Token-Here')