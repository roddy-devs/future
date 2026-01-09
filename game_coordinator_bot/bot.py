"""
Game Coordinator Discord Bot

A Discord bot for coordinating gaming sessions with friends.
Supports slash commands for selecting games, times, platforms, and modes.
"""

import os
import logging
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('game_coordinator')

# Bot configuration
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """Event handler for when the bot is ready."""
    logger.info(f'{bot.user} has connected to Discord!')
    logger.info(f'Bot is in {len(bot.guilds)} guilds')
    
    # Sync slash commands
    try:
        if GUILD_ID:
            guild = discord.Object(id=int(GUILD_ID))
            await bot.tree.sync(guild=guild)
            logger.info(f'Synced commands to guild {GUILD_ID}')
        else:
            await bot.tree.sync()
            logger.info('Synced commands globally')
    except Exception as e:
        logger.error(f'Failed to sync commands: {e}')


async def load_extensions():
    """Load all cogs/extensions."""
    await bot.load_extension('game_coordinator_bot.cogs.game_commands')
    logger.info('Loaded game_commands cog')


async def main():
    """Main function to run the bot."""
    if not TOKEN:
        logger.error('DISCORD_BOT_TOKEN not found in environment variables')
        return
    
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
