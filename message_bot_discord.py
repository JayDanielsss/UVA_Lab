import discord
from discord.ext import commands
from LabJack_Reader import get_r1_value  

# The channel ID where the bot will respond (change to your specific channel ID)
CHANNEL_ID = ChannelID

# Create the Discord bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Command to get the R1 value
@bot.command(name='getLowerCoil')
async def get_lower_coil(ctx):
    # Check if the message is from the correct channel
    if ctx.channel.id != CHANNEL_ID:
        return  # Do nothing if the message is not from the correct channel

    try:
        # Get the R1 value from the LabJack code
        R1 = get_r1_value()
        # Send the R1 value as a message in the correct channel
        await ctx.send(f"The average value of R1 is: {R1}")
    except Exception as e:
        # Send an error message if something goes wrong
        await ctx.send(f"An error occurred: {str(e)}")

#Dont not SHARE!!!
# Run the bot with your token
bot.run('TOKEN')