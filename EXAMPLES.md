# Usage Examples

This document provides real-world examples of using the Game Coordinator Bot.

## Example 1: Call of Duty Zombies Session

**Command:**
```
/play game:Call of Duty time:8pm EST platform:PC mode:Zombies
```

**Result:**
```
🎮 Gaming Session

@username wants to play!

🎯 Game: Call of Duty - Zombies
🖥️ Platform: PC
⏰ Time: 8pm EST

Organized by username
```

**Embed Color:** Dark Red

---

## Example 2: Overcooked on Nintendo Switch

**Command:**
```
/play game:Overcooked time:tomorrow at 3pm platform:Nintendo Switch
```

**Result:**
```
🎮 Gaming Session

@username wants to play!

🎯 Game: Overcooked
🖥️ Platform: Nintendo Switch
⏰ Time: tomorrow at 3pm

Organized by username
```

**Embed Color:** Orange

---

## Example 3: Cross-Platform Call of Duty Multiplayer

**Command:**
```
/play game:Call of Duty time:in 2 hours platform:Cross-platform mode:Multiplayer
```

**Result:**
```
🎮 Gaming Session

@username wants to play!

🎯 Game: Call of Duty - Multiplayer
🖥️ Platform: Cross-platform
⏰ Time: in 2 hours

Organized by username
```

**Embed Color:** Dark Red

---

## Example 4: Call of Duty Endgame on PlayStation

**Command:**
```
/play game:Call of Duty time:Saturday 7pm platform:PlayStation mode:Endgame
```

**Result:**
```
🎮 Gaming Session

@username wants to play!

🎯 Game: Call of Duty - Endgame
🖥️ Platform: PlayStation
⏰ Time: Saturday 7pm

Organized by username
```

**Embed Color:** Dark Red

---

## Common Use Cases

### Coordinating with Friends
```
User: /play game:Overcooked time:tonight at 9pm platform:PC
Bot: [Posts embed]
Friends: React with 👍 or reply to join
```

### Planning Ahead
```
User: /play game:Call of Duty time:Friday night 8pm EST platform:Xbox mode:Zombies
Bot: [Posts embed]
Others: See the announcement days in advance
```

### Last-Minute Sessions
```
User: /play game:Call of Duty time:now platform:Cross-platform mode:Multiplayer
Bot: [Posts embed]
Friends: Jump in immediately
```

---

## Time Format Flexibility

The bot accepts any text for the time field. Here are examples that work well:

### Specific Times
- `8pm EST`
- `20:00 UTC`
- `3:30pm PST`

### Relative Times
- `in 30 minutes`
- `in 2 hours`
- `in an hour`

### Date and Time
- `tomorrow at 3pm`
- `Saturday 7pm`
- `next Friday at 8pm`
- `Jan 15 at 9pm`

### Casual Descriptions
- `tonight`
- `later today`
- `this weekend`
- `after work`

---

## Error Cases

### Missing Mode for Call of Duty

**Command:**
```
/play game:Call of Duty time:8pm EST platform:PC
```

**Result:**
```
❌ Please select a mode for Call of Duty.
```

**Fix:** Add the mode parameter:
```
/play game:Call of Duty time:8pm EST platform:PC mode:Zombies
```

---

## Tips for Best Results

1. **Be Specific with Time Zones:** Include your timezone (EST, PST, UTC) to avoid confusion
2. **Use Mode Strategically:** Each Call of Duty mode attracts different players
3. **Cross-Platform When Possible:** More players can join
4. **Plan Ahead:** Post announcements early for better turnout
5. **React to Sessions:** Use Discord reactions (👍, 🎮, ✅) to show interest

---

## Future Features (Planned)

These examples show how the bot could be extended:

### Notification Subscriptions (Future)
```
/subscribe game:Call of Duty
# Get notified whenever someone creates a Call of Duty session

/unsubscribe game:Call of Duty
# Stop notifications for Call of Duty
```

### Session History (Future)
```
/history
# View all gaming sessions you've organized

/stats
# See statistics about most played games
```

### RSVP System (Future)
```
/join [session_id]
# Officially join a gaming session

/leave [session_id]
# Leave a gaming session
```

---

For more information, see:
- [USAGE.md](USAGE.md) - Full command reference
- [README.md](README.md) - Setup and deployment
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
