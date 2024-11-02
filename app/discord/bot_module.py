# app/discord/bot_module.py
import discord
from discord.ext import commands
import logging

log = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    log.info(f"Logged in as {bot.user.name} ({bot.user.id})")

def get_bot():
    return bot
