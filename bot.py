import discord
import os
from discord.ext import commands

# Get token from Railway's environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

# Your verify command
@bot.command()
async def verify(ctx):
    await ctx.send("Click the button to verify!")

# Load the view with the button
class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__()
        # Replace with your actual hosted HTML page URL
        self.add_item(discord.ui.Button(label="Verify", url="https://your-verified-site.netlify.app", style=discord.ButtonStyle.link))

@bot.command()
async def start_verify(ctx):
    view = VerifyView()
    await ctx.send("Click below to verify:", view=view)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Verifying Users"))

bot.run(TOKEN)
