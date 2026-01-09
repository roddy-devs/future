# Quick Reference Guide

## Using the `/play` Slash Command

### Command Format
```
/play game:<game> time:<time> platform:<platform> [mode:<mode>]
```

### Parameters

#### game (Required)
Choose the game you want to play:
- **Call of Duty**
- **Overcooked**

#### time (Required)
Enter when you want to play. Examples:
- `8pm EST`
- `in 2 hours`
- `tomorrow at 3pm`
- `Saturday 7pm`

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
/play game:Call of Duty time:8pm EST platform:PC mode:Zombies
```

#### Example 2: Overcooked
```
/play game:Overcooked time:tomorrow at 3pm platform:Nintendo Switch
```

#### Example 3: Call of Duty - Multiplayer
```
/play game:Call of Duty time:in 2 hours platform:Cross-platform mode:Multiplayer
```

### What Happens After Submitting?

The bot will post a beautiful embed announcement with:
- 🎮 Your username mentioning you want to play
- 🎯 The game (and mode if applicable)
- 🖥️ The platform
- ⏰ The time you specified
- Color-coded by game (red for Call of Duty, orange for Overcooked)

### Tips

1. **Time Format**: The time field accepts any text, so be as specific as you need
2. **Mode Requirement**: Don't forget to select a mode when choosing Call of Duty!
3. **Visibility**: The announcement is posted in the channel where you use the command
4. **Cross-platform**: Use "Cross-platform" if you're open to playing with people on different systems

### Troubleshooting

**Problem**: Bot doesn't respond to `/play`
- Solution: Make sure the bot has been invited with the proper permissions and slash commands have been synced

**Problem**: "Please select a mode for Call of Duty" error
- Solution: Call of Duty requires a mode selection. Choose Zombies, Multiplayer, or Endgame

**Problem**: Slash command doesn't appear
- Solution: Wait a few minutes for Discord to sync commands, or try reloading Discord

---

For technical setup and deployment information, see [README.md](README.md)
