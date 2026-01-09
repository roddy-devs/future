"""
Game Commands Cog

Contains slash commands for coordinating gaming sessions.
"""

import logging
from typing import Optional
import discord
from discord import app_commands
from discord.ext import commands

from game_coordinator_bot.utils.config import get_game_config
from game_coordinator_bot.utils.timezone_utils import (
    get_timezone_choices,
    parse_time_input,
    get_unix_timestamp,
)

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
        time="What time? (e.g., '8pm', '8:30pm', '20:00')",
        timezone="Your timezone",
        platform="What platform will you play on?",
        mode="Game mode (Call of Duty only)"
    )
    @app_commands.choices(game=[
        app_commands.Choice(name="Call of Duty", value="call_of_duty"),
        app_commands.Choice(name="Overcooked", value="overcooked"),
    ])
    @app_commands.choices(timezone=get_timezone_choices())
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
        timezone: app_commands.Choice[str],
        platform: app_commands.Choice[str],
        mode: Optional[app_commands.Choice[str]] = None
    ):
        """
        Slash command to coordinate a gaming session.
        
        Args:
            interaction: Discord interaction object
            game: Selected game
            time: When to play (time string)
            timezone: User's timezone
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
        
        # Parse the time with timezone
        parsed_time = parse_time_input(time, timezone.value)
        
        if not parsed_time:
            await interaction.response.send_message(
                f"❌ Could not parse time '{time}'. Please use formats like '8pm', '8:30pm', or '20:00'.",
                ephemeral=True
            )
            return
        
        # Create embed for the gaming session announcement
        embed = self._create_session_embed(
            user=interaction.user,
            game=game.name,
            game_value=game.value,
            parsed_time=parsed_time,
            timezone_name=timezone.value,
            timezone_display=timezone.name,
            platform=platform.name,
            mode=mode.name if mode else None
        )
        
        # Send the announcement
        await interaction.response.send_message(embed=embed)
        
        logger.info(
            f"Gaming session created by {interaction.user.name}: "
            f"{game.name} on {platform.name} at {time} {timezone.name}"
            + (f" ({mode.name})" if mode else "")
        )
    
    def _create_session_embed(
        self,
        user: discord.User,
        game: str,
        game_value: str,
        parsed_time,
        timezone_name: str,
        timezone_display: str,
        platform: str,
        mode: Optional[str] = None
    ) -> discord.Embed:
        """
        Create a formatted embed for a gaming session announcement.
        
        Args:
            user: User who created the session
            game: Game display name
            game_value: Game value/ID
            parsed_time: Parsed datetime object with timezone
            timezone_name: Timezone name (e.g., "US/Eastern")
            timezone_display: Timezone display name
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
        
        # Add time field with Discord timestamp (auto-converts to user's timezone)
        timestamp = get_unix_timestamp(parsed_time)
        if timestamp:
            # Discord timestamp formatting: <t:timestamp:F> shows full date/time in user's local timezone
            time_display = f"<t:{timestamp}:F>\n<t:{timestamp}:R>"
        else:
            time_display = "Time not specified"
        
        embed.add_field(name="⏰ Time", value=time_display, inline=False)
        
        # Add footer with user avatar
        embed.set_footer(
            text=f"Organized by {user.name} • {timezone_display}",
            icon_url=user.display_avatar.url
        )
        
        return embed


async def setup(bot: commands.Bot):
    """Setup function to add the cog to the bot."""
    await bot.add_cog(GameCommands(bot))
    logger.info("GameCommands cog loaded")
