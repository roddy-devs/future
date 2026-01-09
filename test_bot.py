#!/usr/bin/env python3
"""
Test script for Game Coordinator Bot

Validates the bot's core functionality without requiring a live Discord connection.
"""

import sys
from typing import Optional
from datetime import datetime
from game_coordinator_bot.utils.config import (
    GameType, Platform, GameConfig, GameMode,
    get_game_config, get_all_games, get_platform_name
)
from game_coordinator_bot.utils.timezone_utils import (
    parse_time_input,
    get_unix_timestamp,
    COMMON_TIMEZONES,
)


def test_game_configurations():
    """Test game configuration system."""
    print("\n=== Testing Game Configurations ===")
    
    # Test all games are loaded
    all_games = get_all_games()
    assert len(all_games) == 2, f"Expected 2 games, found {len(all_games)}"
    print(f"✓ Loaded {len(all_games)} game configurations")
    
    # Test Call of Duty configuration
    cod = get_game_config(GameType.CALL_OF_DUTY)
    assert cod is not None, "Call of Duty config not found"
    assert cod.display_name == "Call of Duty"
    assert cod.supports_modes is True
    assert len(cod.modes) == 3
    mode_names = {mode.id for mode in cod.modes}
    assert mode_names == {"zombies", "multiplayer", "endgame"}
    print(f"✓ Call of Duty: {len(cod.modes)} modes - {', '.join(m.name for m in cod.modes)}")
    
    # Test Overcooked configuration
    overcooked = get_game_config(GameType.OVERCOOKED)
    assert overcooked is not None, "Overcooked config not found"
    assert overcooked.display_name == "Overcooked"
    assert overcooked.supports_modes is False
    assert len(overcooked.modes) == 0
    print(f"✓ Overcooked: no modes (as expected)")
    
    # Test mode lookup
    zombies_mode = cod.get_mode_by_id("zombies")
    assert zombies_mode is not None
    assert zombies_mode.name == "Zombies"
    print(f"✓ Mode lookup: found '{zombies_mode.name}'")
    
    # Test invalid game
    invalid = get_game_config("nonexistent")
    assert invalid is None
    print(f"✓ Invalid game returns None")


def test_platform_names():
    """Test platform display names."""
    print("\n=== Testing Platform Names ===")
    
    platforms = [
        (Platform.PC, "PC"),
        (Platform.PLAYSTATION, "PlayStation"),
        (Platform.XBOX, "Xbox"),
        (Platform.SWITCH, "Nintendo Switch"),
        (Platform.CROSSPLATFORM, "Cross-platform"),
    ]
    
    for platform_id, expected_name in platforms:
        actual_name = get_platform_name(platform_id)
        assert actual_name == expected_name, f"Expected {expected_name}, got {actual_name}"
        print(f"✓ {platform_id.value} → {actual_name}")


def test_command_validation_logic():
    """Test the validation logic for slash commands."""
    print("\n=== Testing Command Validation Logic ===")
    
    # Test Call of Duty requires mode
    cod_config = get_game_config(GameType.CALL_OF_DUTY)
    if cod_config and cod_config.supports_modes:
        print(f"✓ Call of Duty requires mode selection (supports_modes=True)")
    else:
        raise AssertionError("Call of Duty should require mode selection")
    
    # Test Overcooked doesn't require mode
    overcooked_config = get_game_config(GameType.OVERCOOKED)
    if overcooked_config and not overcooked_config.supports_modes:
        print(f"✓ Overcooked doesn't require mode selection (supports_modes=False)")
    else:
        raise AssertionError("Overcooked should not require mode selection")


def test_embed_data_structure():
    """Test that embed data can be properly formatted."""
    print("\n=== Testing Embed Data Structure ===")
    
    # Simulate embed data for Call of Duty
    game_config = get_game_config(GameType.CALL_OF_DUTY)
    mode = game_config.get_mode_by_id("zombies")
    
    embed_data = {
        "game": game_config.display_name,
        "mode": mode.name if mode else None,
        "platform": "PC",
        "time": "8pm EST",
        "color": game_config.color,
    }
    
    assert embed_data["game"] == "Call of Duty"
    assert embed_data["mode"] == "Zombies"
    assert embed_data["color"] == 0x8B0000
    print(f"✓ Call of Duty embed data: {embed_data['game']} - {embed_data['mode']}")
    
    # Simulate embed data for Overcooked
    overcooked_config = get_game_config(GameType.OVERCOOKED)
    embed_data_overcooked = {
        "game": overcooked_config.display_name,
        "mode": None,
        "platform": "Nintendo Switch",
        "time": "tomorrow at 3pm",
        "color": overcooked_config.color,
    }
    
    assert embed_data_overcooked["game"] == "Overcooked"
    assert embed_data_overcooked["mode"] is None
    assert embed_data_overcooked["color"] == 0xFF8C00
    print(f"✓ Overcooked embed data: {embed_data_overcooked['game']} (no mode)")


def test_timezone_functionality():
    """Test timezone utilities."""
    print("\n=== Testing Timezone Functionality ===")
    
    # Test timezone choices data
    assert len(COMMON_TIMEZONES) > 0, "No timezone choices found"
    print(f"✓ Loaded {len(COMMON_TIMEZONES)} timezone choices")
    
    # Test that common timezones are present
    assert "US/Eastern" in COMMON_TIMEZONES
    assert "US/Pacific" in COMMON_TIMEZONES
    assert "Europe/London" in COMMON_TIMEZONES
    assert "UTC" in COMMON_TIMEZONES
    print(f"✓ Common timezones present: US/Eastern, US/Pacific, Europe/London, UTC")
    
    # Test time parsing
    test_cases = [
        ("8pm", "US/Eastern"),
        ("8:30pm", "US/Eastern"),
        ("20:00", "UTC"),
        ("9:15pm", "US/Pacific"),
    ]
    
    for time_str, tz in test_cases:
        parsed = parse_time_input(time_str, tz)
        assert parsed is not None, f"Failed to parse '{time_str}' with timezone {tz}"
        print(f"✓ Successfully parsed '{time_str}' in {tz}")
    
    # Test invalid time parsing
    invalid_parsed = parse_time_input("invalid time", "US/Eastern")
    assert invalid_parsed is None, "Should return None for invalid time"
    print(f"✓ Invalid time correctly returns None")
    
    # Test unix timestamp generation
    parsed_time = parse_time_input("8pm", "US/Eastern")
    if parsed_time:
        timestamp = get_unix_timestamp(parsed_time)
        assert timestamp is not None, "Failed to generate timestamp"
        assert isinstance(timestamp, int), "Timestamp should be an integer"
        print(f"✓ Generated Unix timestamp: {timestamp}")
    
    # Test None timestamp
    none_timestamp = get_unix_timestamp(None)
    assert none_timestamp is None, "None should return None timestamp"
    print(f"✓ None timestamp correctly returns None")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Game Coordinator Bot - Test Suite")
    print("=" * 60)
    
    try:
        test_game_configurations()
        test_platform_names()
        test_command_validation_logic()
        test_embed_data_structure()
        test_timezone_functionality()
        
        print("\n" + "=" * 60)
        print("✅ All tests passed!")
        print("=" * 60)
        return 0
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
