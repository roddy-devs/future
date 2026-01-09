"""Quick script to check bot info and generate invite link."""
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_BOT_TOKEN')
guild_id = os.getenv('DISCORD_GUILD_ID')

# Extract application ID from token (first part before the first dot)
app_id = token.split('.')[0]

print(f"Bot Application ID: {app_id}")
print(f"Guild ID: {guild_id}")
print(f"\nInvite URL (with slash commands):")
print(f"https://discord.com/api/oauth2/authorize?client_id={app_id}&permissions=16796688&scope=bot%20applications.commands")
