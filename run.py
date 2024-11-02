# run.py
from app.discord.bot_module import bot
import os
from app import create_app

def run_discord_bot():
    bot.run(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    create_app()
    run_discord_bot()