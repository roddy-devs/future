# Quick Start Guide

This guide will get your Game Coordinator Bot up and running in under 10 minutes.

## Prerequisites Checklist

- [ ] Discord account
- [ ] Discord bot created at [Discord Developer Portal](https://discord.com/developers/applications)
- [ ] Bot token copied
- [ ] Bot invited to your Discord server
- [ ] Python 3.8+ installed (check with `python3 --version`)
- [ ] Git installed

## 5-Minute Local Setup

### Step 1: Clone and Setup (2 minutes)

```bash
# Clone the repository
git clone https://github.com/roddy-devs/future.git
cd future

# Copy environment template
cp .env.example .env
```

### Step 2: Configure Bot (1 minute)

Edit `.env` file and add your credentials:

```bash
# Open with your favorite editor
nano .env

# Add your values:
DISCORD_BOT_TOKEN=your_actual_bot_token_here
DISCORD_GUILD_ID=your_guild_id_here  # Optional but recommended for faster command sync
```

**How to get Guild ID:**
1. Enable Developer Mode in Discord (Settings → Advanced → Developer Mode)
2. Right-click your server name
3. Click "Copy Server ID"

### Step 3: Run the Bot (2 minutes)

```bash
# Option A: Use the run script (recommended)
./run_bot.sh

# Option B: Manual installation
pip3 install -r requirements.txt
python3 -m game_coordinator_bot.bot
```

### Step 4: Test It!

1. Go to your Discord server
2. Type `/play` in any channel
3. Select a game, time, and platform
4. If you chose Call of Duty, also select a mode
5. Submit and see your beautiful embed! 🎮

## AWS EC2 Deployment (10 minutes)

### Prerequisites
- AWS EC2 instance running (Amazon Linux 2 or Ubuntu)
- SSH access to your instance

### Deployment Steps

```bash
# 1. Connect to your EC2 instance
ssh -i your-key.pem ec2-user@your-instance-ip

# 2. Install dependencies
sudo yum install python3 git -y  # Amazon Linux
# OR
sudo apt install python3 python3-pip git -y  # Ubuntu

# 3. Clone repository
git clone https://github.com/roddy-devs/future.git
cd future

# 4. Configure environment
cp .env.example .env
nano .env  # Add your bot token and guild ID

# 5. Install Python dependencies
pip3 install -r requirements.txt

# 6. Test the bot manually first
python3 -m game_coordinator_bot.bot
# Press Ctrl+C after verifying it connects successfully

# 7. Set up as a service
sudo cp game-coordinator-bot.service /etc/systemd/system/
sudo nano /etc/systemd/system/game-coordinator-bot.service
# Update the User and WorkingDirectory paths if needed

# 8. Start the service
sudo systemctl daemon-reload
sudo systemctl enable game-coordinator-bot
sudo systemctl start game-coordinator-bot

# 9. Verify it's running
sudo systemctl status game-coordinator-bot
```

### Useful Commands

```bash
# View logs
sudo journalctl -u game-coordinator-bot -f

# Restart bot
sudo systemctl restart game-coordinator-bot

# Stop bot
sudo systemctl stop game-coordinator-bot

# Check status
sudo systemctl status game-coordinator-bot
```

## Discord Bot Setup (If Not Done Already)

### Creating the Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Give it a name (e.g., "Game Coordinator")
4. Go to "Bot" section
5. Click "Add Bot"
6. Under "Privileged Gateway Intents", enable:
   - Message Content Intent ✓
7. Copy the bot token (you'll need this for `.env`)

### Inviting the Bot

1. Go to "OAuth2" → "URL Generator"
2. Select scopes:
   - `bot` ✓
   - `applications.commands` ✓
3. Select bot permissions:
   - Send Messages ✓
   - Embed Links ✓
   - Use Slash Commands ✓
4. Copy the generated URL
5. Open it in your browser
6. Select your server and authorize

## Troubleshooting

### Bot doesn't respond to `/play`

**Issue**: Commands not showing up

**Solutions**:
- Wait 5-10 minutes for Discord to sync commands
- Make sure `DISCORD_GUILD_ID` is set correctly in `.env`
- Restart the bot: `sudo systemctl restart game-coordinator-bot`
- Try logging out and back into Discord

### "Module not found" errors

**Issue**: Dependencies not installed

**Solution**:
```bash
pip3 install -r requirements.txt
```

### Bot keeps crashing

**Issue**: Invalid token or permissions

**Solutions**:
- Verify `DISCORD_BOT_TOKEN` is correct in `.env`
- Check bot has proper permissions in Discord server
- View logs: `sudo journalctl -u game-coordinator-bot -n 50`

### "Please select a mode" error

**Issue**: Call of Duty requires mode selection

**Solution**:
- This is expected! Call of Duty requires you to select Zombies, Multiplayer, or Endgame
- Just select one of the three modes when using `/play` with Call of Duty

## Next Steps

- Read [USAGE.md](USAGE.md) for detailed command usage
- Check [ARCHITECTURE.md](ARCHITECTURE.md) to understand how to extend the bot
- See [README.md](README.md) for comprehensive documentation

## Getting Help

If you encounter issues:
1. Check the logs: `sudo journalctl -u game-coordinator-bot -f`
2. Verify your `.env` configuration
3. Make sure the bot has proper Discord permissions
4. Check that your Python version is 3.8 or higher

## Success Checklist

- [ ] Bot shows as "online" in Discord
- [ ] `/play` command appears when typing in a channel
- [ ] Can successfully create a gaming session
- [ ] Embed appears with correct information
- [ ] Call of Duty requires mode selection
- [ ] Overcooked doesn't require mode selection

---

**Estimated Total Setup Time**: 5-10 minutes for local, 15-20 minutes for AWS EC2

Enjoy coordinating your gaming sessions! 🎮
