# Architecture Documentation

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AWS EC2 Instance                      │
│                                                           │
│  ┌────────────────────────────────────────────────────┐ │
│  │           Game Coordinator Bot (Python)            │ │
│  │                                                     │ │
│  │  ┌──────────────────────────────────────────────┐ │ │
│  │  │         bot.py (Main Entry Point)            │ │ │
│  │  │  • Initializes Discord client                │ │ │
│  │  │  • Loads cogs/extensions                     │ │ │
│  │  │  • Handles event lifecycle                   │ │ │
│  │  └──────────────────────────────────────────────┘ │ │
│  │                       │                            │ │
│  │                       ▼                            │ │
│  │  ┌──────────────────────────────────────────────┐ │ │
│  │  │        cogs/game_commands.py                 │ │ │
│  │  │  • /play slash command                       │ │ │
│  │  │  • Input validation                          │ │ │
│  │  │  • Embed creation                            │ │ │
│  │  └──────────────────────────────────────────────┘ │ │
│  │                       │                            │ │
│  │                       ▼                            │ │
│  │  ┌──────────────────────────────────────────────┐ │ │
│  │  │         utils/config.py                      │ │ │
│  │  │  • Game configurations                       │ │ │
│  │  │  • Platform definitions                      │ │ │
│  │  │  • Color schemes                             │ │ │
│  │  │  • Mode definitions                          │ │ │
│  │  └──────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                           │
│  ┌──────────────────┐          ┌──────────────────────┐ │
│  │  .env (Config)   │          │  systemd Service     │ │
│  │  • Bot Token     │          │  • Auto-restart      │ │
│  │  • Guild ID      │          │  • Logging           │ │
│  └──────────────────┘          └──────────────────────┘ │
└─────────────────────────────────────────────────────────┘
                        │
                        │ Discord API
                        ▼
        ┌───────────────────────────────┐
        │      Discord Server           │
        │  • Receives slash commands    │
        │  • Displays embeds            │
        │  • Notifies users             │
        └───────────────────────────────┘
```

## Data Flow

### Slash Command Execution Flow

```
1. User types /play in Discord channel
                │
                ▼
2. Discord sends interaction to bot
                │
                ▼
3. Bot receives interaction in game_commands.py
                │
                ▼
4. Validate inputs (game, time, platform, mode)
                │
                ├─ If Call of Duty & no mode → Error response
                │
                ▼
5. Retrieve game config from utils/config.py
                │
                ▼
6. Create formatted embed with:
   • User mention
   • Game & mode
   • Platform
   • Time
   • Color scheme
                │
                ▼
7. Send embed to Discord channel
                │
                ▼
8. Users see beautiful announcement
```

## Component Responsibilities

### `bot.py`
- **Purpose**: Main entry point and bot lifecycle management
- **Responsibilities**:
  - Initialize Discord bot with proper intents
  - Load environment variables
  - Register and sync slash commands
  - Load cog extensions
  - Handle bot startup events

### `cogs/game_commands.py`
- **Purpose**: Implements the `/play` slash command
- **Responsibilities**:
  - Define slash command parameters and choices
  - Validate user inputs (especially mode requirement for Call of Duty)
  - Coordinate with config to get game information
  - Create formatted Discord embeds
  - Send responses to users
  - Log command usage

### `utils/config.py`
- **Purpose**: Centralized configuration for games and platforms
- **Responsibilities**:
  - Define game types and their properties
  - Store game modes for each game
  - Provide color schemes for embeds
  - Platform definitions and display names
  - Utility functions for config lookups

## Extension Points for Future Features

### 1. Per-Game Notification Subscriptions
**Location**: New cog `cogs/notifications.py`

```python
# Future implementation structure
class NotificationsCog(commands.Cog):
    @app_commands.command(name="subscribe")
    async def subscribe_game(self, game: str):
        """Subscribe to notifications for a specific game"""
        # Store subscription in database
        # Notify user when /play is used for their subscribed game
```

### 2. Session History Tracking
**Location**: New module `utils/database.py`

```python
# Future implementation structure
class SessionDatabase:
    def save_session(self, user, game, time, platform):
        """Save gaming session to history"""
    
    def get_user_history(self, user):
        """Get all sessions organized by a user"""
```

### 3. Role-Based Game Communities
**Location**: Extend `game_commands.py`

```python
# Future feature
# Automatically mention users with specific roles
# e.g., @CallOfDutyPlayers when someone creates a CoD session
```

## Configuration Management

### Environment Variables
- `DISCORD_BOT_TOKEN`: Discord bot authentication token
- `DISCORD_GUILD_ID`: Optional guild ID for command syncing

### Game Configuration
Games are configured in `utils/config.py` using the `GameConfig` dataclass:

```python
GameConfig(
    id="game_id",
    name="internal_name",
    display_name="Display Name",
    supports_modes=True/False,
    modes=[GameMode(...)],  # List of available modes
    color=0xHEXCOLOR,  # Discord embed color
)
```

### Adding New Games
1. Add game enum to `GameType`
2. Create `GameConfig` entry in `GAME_CONFIGS`
3. Update slash command choices in `game_commands.py`

### Adding New Platforms
1. Add platform enum to `Platform`
2. Update `PLATFORM_NAMES` mapping
3. Update slash command choices in `game_commands.py`

## Deployment Architecture

### systemd Service Management
The bot runs as a systemd service on AWS EC2:
- **Auto-restart**: Automatically restarts if it crashes
- **Logging**: Logs to journalctl for easy debugging
- **Startup**: Starts automatically on system boot

### Monitoring and Logs
```bash
# View real-time logs
sudo journalctl -u game-coordinator-bot -f

# Check service status
sudo systemctl status game-coordinator-bot

# Restart service
sudo systemctl restart game-coordinator-bot
```

## Security Considerations

1. **Token Management**: Bot token stored in `.env` file (not in git)
2. **Input Validation**: All user inputs validated before processing
3. **No SQL Injection**: No database yet, future implementations should use parameterized queries
4. **Rate Limiting**: Discord API handles rate limiting automatically
5. **Permissions**: Bot only requests necessary Discord permissions

## Performance Considerations

1. **Async/Await**: All Discord operations use async/await for non-blocking execution
2. **Cog Loading**: Commands loaded dynamically as cogs for modularity
3. **Config Caching**: Game configs stored in memory for fast access
4. **Minimal Dependencies**: Only essential packages (discord.py, python-dotenv)

## Testing Strategy

### Current Tests (`test_bot.py`)
- Game configuration validation
- Platform name lookups
- Command validation logic
- Embed data structure verification

### Future Test Additions
- Integration tests with Discord test guild
- Mock interaction testing
- Database operation tests (when implemented)
- Notification system tests (when implemented)

## Scalability Considerations

### Current Scale
- Designed for single server (guild) deployment
- Can handle multiple concurrent users
- No database for simplicity

### Future Scaling Options
1. **Multi-Guild Support**: Remove guild ID restriction
2. **Database**: Add PostgreSQL for session history and subscriptions
3. **Caching**: Add Redis for frequently accessed data
4. **Load Balancing**: Deploy multiple instances with shared database

## Maintenance

### Regular Tasks
- Monitor bot uptime and logs
- Update dependencies for security patches
- Backup configuration and data (when database is added)
- Review and respond to user feedback

### Update Process
```bash
# On EC2 instance
cd /home/ec2-user/future
git pull origin main
sudo systemctl restart game-coordinator-bot
```
