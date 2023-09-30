from sys import stdout

import disnake
from disnake.ext import commands
import requests
import random
from dotenv import load_dotenv
import os
from loguru import logger

VERSION = "1.1.0"

# Load environment variables from .env file
load_dotenv()
GIPHY_API_KEY = os.getenv("GIPHY_API_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# remove default logger
logger.remove(0)

# Initialize logger
logger.add(stdout, colorize=True, format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>", level="DEBUG")

# Initialize bot
bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user}")

@bot.slash_command(description="here is kitty of type")
async def prrr(ctx, words: str):
    try:
        # Defer the interaction to prevent timeout
        await ctx.defer()
        # Check if the user has permission (replace "Admin" with the role you want to check)
        if "no cats" not in [role.name for role in ctx.author.roles]:
            logger.debug("User has permission to execute the command.")

            # Append random cat word to the search query
            random_word = random.choice(["cat", "kitty", "kitten"])
            search_query = f"{words} {random_word}"
            logger.debug(f"Search query generated: {search_query}")

            # Search for GIF using GIPHY API
            url = f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={search_query}&limit=1"
            response = requests.get(url).json()
            gif_url = response['data'][0]['images']['original']['url']
            logger.debug(f"GIF URL fetched: {gif_url}")

            # Send GIF as an attachment
            embed = disnake.Embed()
            embed.set_image(url=gif_url)
            await ctx.send(embeds=[embed])
            logger.info("GIF sent successfully.")
        else:
            await ctx.send("sorry you can't have any cats idk why i don't make the rules")
            logger.warning(f"User \"{ctx.author.username}\" does not have permission to execute /prrr.")
    except disnake.errors.InteractionTimedOut:
        logger.error("Interaction timed out. Please try again.")
        await ctx.send("oopsie something took too long, try again", ephemeral=True)
    except disnake.errors.ClientException as e:
        logger.error(f"Client exception occurred: {e}")
        await ctx.send("Client exception when looking for your cat! Sorry.", ephemeral=True)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        await ctx.send("I have no idea what happened here please don't bring it up", ephemeral=True)

if __name__ == "__main__":
    # Run bot
    bot.run(DISCORD_BOT_TOKEN)
