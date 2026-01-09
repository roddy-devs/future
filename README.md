# future

Personal infrastructure for always-on automation and Discord services.

## Game Coordinator Bot

A Discord bot for coordinating gaming sessions with friends. Built with discord.py and designed to run continuously on AWS EC2.

### Features

- **Slash Command `/play`**: Coordinate gaming sessions with friends
  - Select from multiple games (Call of Duty, Overcooked)
  - Specify time for the session
  - Choose platform (PC, PlayStation, Xbox, Nintendo Switch, Cross-platform)
  - Game-specific modes (for Call of Duty: Zombies, Multiplayer, Endgame)
- **Clean Embeds**: Beautiful announcements with color-coded game information
- **Modular Design**: Easily extensible for future features like per-game notification subscriptions

### Setup

#### Prerequisites

- Python 3.8 or higher
- A Discord Bot Token ([Create one here](https://discord.com/developers/applications))
- Discord Guild (Server) ID where the bot will be used

#### Installation

1. Clone the repository:
```bash
git clone https://github.com/roddy-devs/future.git
cd future
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env and add your Discord bot token and guild ID
```

4. Run the bot:
```bash
python -m game_coordinator_bot.bot
```

### Discord Bot Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section and create a bot
4. Enable the following Privileged Gateway Intents:
   - Message Content Intent
   - Server Members Intent (optional)
5. Copy the bot token and add it to your `.env` file
6. Go to "OAuth2" > "URL Generator"
7. Select scopes: `bot` and `applications.commands`
8. Select bot permissions: `Send Messages`, `Embed Links`, `Use Slash Commands`
9. Copy the generated URL and invite the bot to your server
10. Get your Guild ID (enable Developer Mode in Discord, right-click your server, "Copy Server ID")

### AWS EC2 Deployment

#### Launch EC2 Instance

1. Choose an Amazon Linux 2 or Ubuntu AMI
2. Select instance type (t2.micro is sufficient for small servers)
3. Configure security group to allow SSH access
4. Launch and connect to your instance

#### Setup on EC2

```bash
# Update system
sudo yum update -y  # For Amazon Linux
# or
sudo apt update && sudo apt upgrade -y  # For Ubuntu

# Install Python and Git
sudo yum install python3 git -y  # For Amazon Linux
# or
sudo apt install python3 python3-pip git -y  # For Ubuntu

# Clone repository
git clone https://github.com/roddy-devs/future.git
cd future

# Install dependencies
pip3 install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # Edit with your bot token and guild ID
```

#### Run as a Service (systemd)

Create a systemd service file:

```bash
sudo nano /etc/systemd/system/game-coordinator-bot.service
```

Add the following content:

```ini
[Unit]
Description=Game Coordinator Discord Bot
After=network.target

[Service]
Type=simple
User=ec2-user
WorkingDirectory=/home/ec2-user/future
ExecStart=/usr/bin/python3 -m game_coordinator_bot.bot
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable game-coordinator-bot
sudo systemctl start game-coordinator-bot

# Check status
sudo systemctl status game-coordinator-bot

# View logs
sudo journalctl -u game-coordinator-bot -f
```

### Usage

Once the bot is running and invited to your server, use the `/play` slash command:

1. Type `/play` in any channel
2. Select the game you want to play
3. Enter when you want to play (e.g., "8pm EST", "in 2 hours", "tomorrow at 3pm")
4. Choose your platform
5. If playing Call of Duty, select a mode (Zombies, Multiplayer, or Endgame)
6. Submit, and the bot will post a clean embed announcement!

### Architecture

The bot is designed with modularity in mind:

```
game_coordinator_bot/
├── bot.py              # Main bot entry point
├── cogs/              # Command modules
│   └── game_commands.py  # Game coordination slash commands
├── utils/             # Utility modules
│   └── config.py      # Game configurations and constants
└── __init__.py
```

#### Extending the Bot

**Adding New Games:**

Edit `game_coordinator_bot/utils/config.py` and add a new game configuration:

```python
GameType.NEW_GAME = "new_game"

GAME_CONFIGS[GameType.NEW_GAME] = GameConfig(
    id=GameType.NEW_GAME,
    name="new_game",
    display_name="New Game",
    supports_modes=True,  # or False
    modes=[
        GameMode(id="mode1", name="Mode 1"),
        # ... more modes
    ],
    color=0x00FF00,  # Green
)
```

Then update the slash command choices in `game_commands.py`.

**Adding New Features:**

The modular design allows easy addition of:
- Per-game notification subscriptions (add a new cog)
- Session history tracking (add database integration)
- Role-based access control (add permission checks)
- Multiple concurrent sessions (add session management)

### Contributing

This is a personal infrastructure project, but suggestions and improvements are welcome!

### License

MIT License - See LICENSE file for details
