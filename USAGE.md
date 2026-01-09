# Quick Reference Guide

## Using the `/play` Slash Command

### Command Format
```
/play game:<game> time:<time> timezone:<timezone> platform:<platform> [mode:<mode>]
```

### Parameters

#### game (Required)
Choose the game you want to play:
- **Call of Duty**
- **Overcooked**

#### time (Required)
Enter the time you want to play. Examples:
- `8pm`
- `8:30pm`
- `20:00`
- `9:15pm`

#### timezone (Required)
Select your timezone. Available options:
- **US Eastern (EST/EDT)**
- **US Central (CST/CDT)**
- **US Mountain (MST/MDT)**
- **US Pacific (PST/PDT)**
- **UK (GMT/BST)**
- **Central Europe (CET/CEST)**
- **Eastern Europe (EET/EEST)**
- **Japan (JST)**
- **Korea (KST)**
- **Australia East (AEDT/AEST)**
- **UTC**

**Note:** The bot automatically converts your time to everyone else's timezone when they view the announcement!

#### platform (Required)
Select your gaming platform:
- **PC**
- **PlayStation**
- **Xbox**
- **Nintendo Switch**
- **Cross-platform**

#### mode (Conditional)
**Required for Call of Duty only:**
- **Zombies** - Survive the undead hordes
- **Multiplayer** - Classic PvP battles
- **Endgame** - High-stakes endgame mode

### Examples

#### Example 1: Call of Duty - Zombies
```
/play game:Call of Duty time:8pm timezone:US Eastern platform:PC mode:Zombies
```

#### Example 2: Overcooked
```
/play game:Overcooked time:8:30pm timezone:US Pacific platform:Nintendo Switch
```

#### Example 3: Call of Duty - Multiplayer
```
/play game:Call of Duty time:20:00 timezone:UTC platform:Cross-platform mode:Multiplayer
```

### What Happens After Submitting?

The bot will post a beautiful embed announcement with:
- 🎮 Your username mentioning you want to play
- 🎯 The game (and mode if applicable)
- 🖥️ The platform
- ⏰ The time **automatically converted to each user's local timezone**
- Color-coded by game (red for Call of Duty, orange for Overcooked)

**Timezone Magic:** When you select a time and timezone, Discord automatically shows that time in each user's local timezone! No more confusion about "8pm in what timezone?"

### Tips

1. **Time Format**: Use simple formats like `8pm`, `8:30pm`, or `20:00` (24-hour)
2. **Timezone Selection**: Always select your timezone so others see the correct time
3. **Mode Requirement**: Don't forget to select a mode when choosing Call of Duty!
4. **Visibility**: The announcement is posted in the channel where you use the command
5. **Cross-platform**: Use "Cross-platform" if you're open to playing with people on different systems
6. **Time Conversion**: The bot uses Discord's timestamp feature - everyone sees the time in their own timezone automatically!

### Troubleshooting

**Problem**: Bot doesn't respond to `/play`
- Solution: Make sure the bot has been invited with the proper permissions and slash commands have been synced

**Problem**: "Please select a mode for Call of Duty" error
- Solution: Call of Duty requires a mode selection. Choose Zombies, Multiplayer, or Endgame

**Problem**: Slash command doesn't appear
- Solution: Wait a few minutes for Discord to sync commands, or try reloading Discord

---

For technical setup and deployment information, see [README.md](README.md)
