# Usage Examples

This document provides real-world examples of using the Game Coordinator Bot.

## Example 1: Call of Duty Zombies Session

**Command:**
```
/play game:Call of Duty time:8pm timezone:US Eastern platform:PC mode:Zombies
```

**Result:**
```
🎮 Gaming Session

@username wants to play!

🎯 Game: Call of Duty - Zombies
🖥️ Platform: PC
⏰ Time: Saturday, January 11, 2026 at 8:00 PM
       in 2 hours

Organized by username • US Eastern (EST/EDT)
```

**Note:** Discord automatically shows the time in each viewer's local timezone!

**Embed Color:** Dark Red

---

## Example 2: Overcooked on Nintendo Switch

**Command:**
```
/play game:Overcooked time:8:30pm timezone:US Pacific platform:Nintendo Switch
```

**Result:**
```
🎮 Gaming Session

@username wants to play!

🎯 Game: Overcooked
🖥️ Platform: Nintendo Switch
⏰ Time: Saturday, January 11, 2026 at 8:30 PM
       in 3 hours

Organized by username • US Pacific (PST/PDT)
```

**Note:** Users in different timezones will see the time converted to their local timezone automatically!

**Embed Color:** Orange

---

## Example 3: Cross-Platform Call of Duty Multiplayer

**Command:**
```
/play game:Call of Duty time:20:00 timezone:UTC platform:Cross-platform mode:Multiplayer
```

**Result:**
```
🎮 Gaming Session

@username wants to play!

🎯 Game: Call of Duty - Multiplayer
🖥️ Platform: Cross-platform
⏰ Time: Saturday, January 11, 2026 at 8:00 PM
       in 4 hours

Organized by username • UTC
```

**Note:** Users in Eastern time will see "3:00 PM EST", users in Pacific time will see "12:00 PM PST", etc.

**Embed Color:** Dark Red

---

## Example 4: Call of Duty Endgame on PlayStation

**Command:**
```
/play game:Call of Duty time:7pm timezone:Europe/London platform:PlayStation mode:Endgame
```

**Result:**
```
🎮 Gaming Session

@username wants to play!

🎯 Game: Call of Duty - Endgame
🖥️ Platform: PlayStation
⏰ Time: Saturday, January 11, 2026 at 7:00 PM
       in 5 hours

Organized by username • UK (GMT/BST)
```

**Embed Color:** Dark Red

---

## Timezone Conversion Examples

The bot's timezone feature means everyone sees the time in their own timezone:

**Example:** You schedule for `8pm US Eastern`
- **US Eastern users see:** 8:00 PM EST
- **US Pacific users see:** 5:00 PM PST
- **UK users see:** 1:00 AM GMT
- **Japan users see:** 10:00 AM JST

This eliminates confusion and makes it easy to coordinate across timezones!

---

## Common Use Cases

### Coordinating with Friends Across Timezones
```
User in New York: /play game:Overcooked time:9pm timezone:US Eastern platform:PC
Bot: [Posts embed showing 9pm EST for New York, 6pm PST for California, etc.]
Friends: Everyone sees the time in their own timezone automatically!
```

### Planning Ahead
```
User: /play game:Call of Duty time:8pm timezone:US Pacific platform:Xbox mode:Zombies
Bot: [Posts embed]
Others: See the announcement with time automatically converted to their timezone
```

### Last-Minute Sessions
```
User: /play game:Call of Duty time:20:00 timezone:UTC platform:Cross-platform mode:Multiplayer
Bot: [Posts embed]
Friends: See it in their local time and can jump in
```

---

## Time Format Guide

The bot accepts simple time formats:

### 12-Hour Format (with am/pm)
- `8pm` → 8:00 PM
- `8:30pm` → 8:30 PM
- `9:15am` → 9:15 AM

### 24-Hour Format
- `20:00` → 8:00 PM
- `14:30` → 2:30 PM
- `09:00` → 9:00 AM

**Important:** Always select your timezone so the bot can convert the time for other users!

---

## Supported Timezones

- **US Eastern (EST/EDT)** - New York, Washington DC
- **US Central (CST/CDT)** - Chicago, Dallas
- **US Mountain (MST/MDT)** - Denver, Phoenix
- **US Pacific (PST/PDT)** - Los Angeles, Seattle
- **UK (GMT/BST)** - London
- **Central Europe (CET/CEST)** - Paris, Berlin
- **Eastern Europe (EET/EEST)** - Helsinki, Athens
- **Japan (JST)** - Tokyo
- **Korea (KST)** - Seoul
- **Australia East (AEDT/AEST)** - Sydney, Melbourne
- **UTC** - Universal Coordinated Time
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
