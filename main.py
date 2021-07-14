import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")

  if message.content.startswith("$D"):
    await message.channel.send("I HAVE THE BEST 'D' IN ROCKET LEAGUE!")

  if message.content.startswith("$plan"):
    await message.channel.send("All part of my master plan!")

  if message.content.startswith("$fluster"):
    await message.channel.send("DON'T FLUSTER ME! I AM ALREADY FLUSTERED!")
    
  if message.content.startswith("$home"):
    await message.channel.send("Born and raised in Alabama!")


client.run(os.environ['token'])