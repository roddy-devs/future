"""
Configuration management for the Game Coordinator Bot.

This module provides configuration for games and their properties,
making it easy to add new games and features in the future.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum


class GameType(str, Enum):
    """Enum for supported games."""
    CALL_OF_DUTY = "call_of_duty"
    OVERCOOKED = "overcooked"


class Platform(str, Enum):
    """Enum for gaming platforms."""
    PC = "pc"
    PLAYSTATION = "playstation"
    XBOX = "xbox"
    SWITCH = "switch"
    CROSSPLATFORM = "crossplatform"


@dataclass
class GameMode:
    """Represents a game mode."""
    id: str
    name: str
    description: Optional[str] = None


@dataclass
class GameConfig:
    """Configuration for a specific game."""
    id: str
    name: str
    display_name: str
    modes: List[GameMode]
    supports_modes: bool
    color: int  # Discord color as integer
    
    def get_mode_by_id(self, mode_id: str) -> Optional[GameMode]:
        """Get a game mode by its ID."""
        for mode in self.modes:
            if mode.id == mode_id:
                return mode
        return None


# Game configurations
GAME_CONFIGS: Dict[str, GameConfig] = {
    GameType.CALL_OF_DUTY: GameConfig(
        id=GameType.CALL_OF_DUTY,
        name="call_of_duty",
        display_name="Call of Duty",
        supports_modes=True,
        modes=[
            GameMode(id="zombies", name="Zombies", description="Survive the undead hordes"),
            GameMode(id="multiplayer", name="Multiplayer", description="Classic PvP battles"),
            GameMode(id="endgame", name="Endgame", description="High-stakes endgame mode"),
        ],
        color=0x8B0000,  # Dark red
    ),
    GameType.OVERCOOKED: GameConfig(
        id=GameType.OVERCOOKED,
        name="overcooked",
        display_name="Overcooked",
        supports_modes=False,
        modes=[],
        color=0xFF8C00,  # Orange
    ),
}


def get_game_config(game_id: str) -> Optional[GameConfig]:
    """
    Get game configuration by game ID.
    
    Args:
        game_id: Game identifier
    
    Returns:
        GameConfig if found, None otherwise
    """
    return GAME_CONFIGS.get(game_id)


def get_all_games() -> List[GameConfig]:
    """Get all available game configurations."""
    return list(GAME_CONFIGS.values())


# Platform display names
PLATFORM_NAMES: Dict[str, str] = {
    Platform.PC: "PC",
    Platform.PLAYSTATION: "PlayStation",
    Platform.XBOX: "Xbox",
    Platform.SWITCH: "Nintendo Switch",
    Platform.CROSSPLATFORM: "Cross-platform",
}


def get_platform_name(platform_id: str) -> str:
    """
    Get display name for a platform.
    
    Args:
        platform_id: Platform identifier
    
    Returns:
        Display name for the platform
    """
    return PLATFORM_NAMES.get(platform_id, platform_id.title())
