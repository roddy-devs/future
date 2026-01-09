"""
Timezone utilities for the Game Coordinator Bot.

Provides timezone conversion and formatting for gaming sessions.
"""

from datetime import datetime, timedelta
from typing import Optional, List, TYPE_CHECKING
import pytz
import re

if TYPE_CHECKING:
    from discord import app_commands


# Common timezones for gaming communities
COMMON_TIMEZONES = {
    "US/Eastern": "US Eastern (EST/EDT)",
    "US/Central": "US Central (CST/CDT)",
    "US/Mountain": "US Mountain (MST/MDT)",
    "US/Pacific": "US Pacific (PST/PDT)",
    "Europe/London": "UK (GMT/BST)",
    "Europe/Paris": "Central Europe (CET/CEST)",
    "Europe/Helsinki": "Eastern Europe (EET/EEST)",
    "Asia/Tokyo": "Japan (JST)",
    "Asia/Seoul": "Korea (KST)",
    "Australia/Sydney": "Australia East (AEDT/AEST)",
    "UTC": "UTC",
}


def get_timezone_choices() -> List:
    """
    Get timezone choices for slash command.
    
    Returns:
        List of app_commands.Choice objects for timezones
    """
    from discord import app_commands
    
    return [
        app_commands.Choice(name=display_name, value=tz_name)
        for tz_name, display_name in COMMON_TIMEZONES.items()
    ]


def parse_time_input(time_str: str, timezone_str: str) -> Optional[datetime]:
    """
    Parse time input string with timezone.
    
    Args:
        time_str: Time string (e.g., "8pm", "20:00", "8:30pm")
        timezone_str: Timezone name (e.g., "US/Eastern")
    
    Returns:
        datetime object with timezone, or None if parsing fails
    """
    try:
        tz = pytz.timezone(timezone_str)
        # Get current date in the specified timezone
        now = datetime.now(tz)
        
        # Parse common time formats
        time_lower = time_str.lower().strip()
        
        # Try 12-hour format first (8pm, 8:30pm)
        match_12h = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(am|pm)$', time_lower)
        if match_12h:
            hour = int(match_12h.group(1))
            minute = int(match_12h.group(2)) if match_12h.group(2) else 0
            ampm = match_12h.group(3)
            
            if ampm == 'pm' and hour < 12:
                hour += 12
            elif ampm == 'am' and hour == 12:
                hour = 0
            
            # Create datetime for today at the specified time
            parsed_time = tz.localize(datetime(
                now.year, now.month, now.day, hour, minute
            ))
            
            # If the time is in the past, assume it's for tomorrow
            if parsed_time < now:
                tomorrow = now + timedelta(days=1)
                parsed_time = tz.localize(datetime(
                    tomorrow.year, tomorrow.month, tomorrow.day, hour, minute
                ))
            
            return parsed_time
        
        # Try 24-hour format (20:00, 14:30)
        match_24h = re.match(r'^(\d{1,2}):(\d{2})$', time_str.strip())
        if match_24h:
            hour = int(match_24h.group(1))
            minute = int(match_24h.group(2))
            
            if hour > 23 or minute > 59:
                return None
            
            # Create datetime for today at the specified time
            parsed_time = tz.localize(datetime(
                now.year, now.month, now.day, hour, minute
            ))
            
            # If the time is in the past, assume it's for tomorrow
            if parsed_time < now:
                tomorrow = now + timedelta(days=1)
                parsed_time = tz.localize(datetime(
                    tomorrow.year, tomorrow.month, tomorrow.day, hour, minute
                ))
            
            return parsed_time
        
        return None
    except Exception:
        return None


def get_unix_timestamp(dt: Optional[datetime]) -> Optional[int]:
    """
    Get Unix timestamp from datetime for Discord timestamp formatting.
    
    Args:
        dt: datetime object with timezone
    
    Returns:
        Unix timestamp as integer, or None if dt is None
    """
    if not dt:
        return None
    return int(dt.timestamp())
