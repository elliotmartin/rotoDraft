import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import datetime
import roto_model


def initialize_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = initialize_logger()

load_dotenv()
BOT_TOKEN = os.environ.get('CUBING_DISCORD_TOKEN')
CHANNEL_ID = os.environ.get('CUBING_CHANNEL_ID')
# Create an instance of the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

bot_roto = None

# Event that runs when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send("hello!")


@bot.command()
async def start_roto(ctx):
    bot_roto = roto_model.Roto(['a', 'b', 'c'], '/Users/elliotmartin/Downloads/EastBayCubingPeasantRotisserieDraft.txt')
    await ctx.send(str(bot_roto))

@bot.command()
async def pick(ctx, player, card):
    if not bot_roto:
        await ctx.send("oops, no draft started")
    bot_roto.pick(player, card)
    await ctx.send(f'{player} picked {card}')


# Event that runs when a message is received
@bot.event
async def on_message(message):
    # Check if the message is from the specific channel you want to read
    if message.channel.id == int(CHANNEL_ID):
        print("foo")
        # Process the message here
        print(message)
        print(message.content)

    # Allow other event listeners to process the message
    await bot.process_commands(message)


# Run the bot with your bot token
bot.run(BOT_TOKEN)
