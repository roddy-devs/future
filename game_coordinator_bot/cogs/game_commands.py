"""
Game Commands Cog

Contains slash commands for coordinating gaming sessions.
"""

import logging
from typing import Optional
import discord
from discord import app_commands
from discord.ext import commands

from game_coordinator_bot.utils.config import get_game_config, GameType

logger = logging.getLogger('game_coordinator.commands')


class GameCommands(commands.Cog):
    """Cog for game coordination commands."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(
        name="play",
        description="Coordinate a gaming session with friends"
    )
    @app_commands.describe(
        game="Choose the game you want to play",
        time="When do you want to play? (e.g., '8pm EST', 'in 2 hours', 'tomorrow at 3pm')",
        platform="What platform will you play on?",
        mode="Game mode (Call of Duty only)"
    )
    @app_commands.choices(game=[
        app_commands.Choice(name="Call of Duty", value="call_of_duty"),
        app_commands.Choice(name="Overcooked", value="overcooked"),
    ])
    @app_commands.choices(platform=[
        app_commands.Choice(name="PC", value="pc"),
        app_commands.Choice(name="PlayStation", value="playstation"),
        app_commands.Choice(name="Xbox", value="xbox"),
        app_commands.Choice(name="Nintendo Switch", value="switch"),
        app_commands.Choice(name="Cross-platform", value="crossplatform"),
    ])
    @app_commands.choices(mode=[
        app_commands.Choice(name="Zombies", value="zombies"),
        app_commands.Choice(name="Multiplayer", value="multiplayer"),
        app_commands.Choice(name="Endgame", value="endgame"),
    ])
    async def play_command(
        self,
        interaction: discord.Interaction,
        game: app_commands.Choice[str],
        time: str,
        platform: app_commands.Choice[str],
        mode: Optional[app_commands.Choice[str]] = None
    ):
        """
        Slash command to coordinate a gaming session.
        
        Args:
            interaction: Discord interaction object
            game: Selected game
            time: When to play
            platform: Gaming platform
            mode: Game mode (optional, required for Call of Duty)
        """
        # Get game configuration
        game_config = get_game_config(game.value)
        
        # Validate Call of Duty requires a mode
        if game_config and game_config.supports_modes and mode is None:
            await interaction.response.send_message(
                f"❌ Please select a mode for {game_config.display_name}.",
                ephemeral=True
            )
            return
        
        # Create embed for the gaming session announcement
        embed = self._create_session_embed(
            user=interaction.user,
            game=game.name,
            game_value=game.value,
            time=time,
            platform=platform.name,
            mode=mode.name if mode else None
        )
        
        # Send the announcement
        await interaction.response.send_message(embed=embed)
        
        logger.info(
            f"Gaming session created by {interaction.user.name}: "
            f"{game.name} on {platform.name} at {time}"
            + (f" ({mode.name})" if mode else "")
        )
    
    def _create_session_embed(
        self,
        user: discord.User,
        game: str,
        game_value: str,
        time: str,
        platform: str,
        mode: Optional[str] = None
    ) -> discord.Embed:
        """
        Create a formatted embed for a gaming session announcement.
        
        Args:
            user: User who created the session
            game: Game display name
            game_value: Game value/ID
            time: When to play
            platform: Gaming platform
            mode: Game mode (optional)
        
        Returns:
            discord.Embed: Formatted embed
        """
        # Get game configuration for color
        game_config = get_game_config(game_value)
        color = discord.Color(game_config.color) if game_config else discord.Color.blue()
        
        # Create embed
        embed = discord.Embed(
            title="🎮 Gaming Session",
            description=f"{user.mention} wants to play!",
            color=color
        )
        
        # Add game field
        game_display = game
        if mode:
            game_display = f"{game} - {mode}"
        embed.add_field(name="🎯 Game", value=game_display, inline=True)
        
        # Add platform field
        embed.add_field(name="🖥️ Platform", value=platform, inline=True)
        
        # Add time field
        embed.add_field(name="⏰ Time", value=time, inline=True)
        
        # Add footer with user avatar
        embed.set_footer(
            text=f"Organized by {user.name}",
            icon_url=user.display_avatar.url
        )
        
        # Add thumbnail based on game
        if game == "Call of Duty":
            # Using a generic gaming controller emoji as thumbnail
            embed.set_thumbnail(url=user.display_avatar.url)
        
        return embed


async def setup(bot: commands.Bot):
    """Setup function to add the cog to the bot."""
    await bot.add_cog(GameCommands(bot))
    logger.info("GameCommands cog loaded")
