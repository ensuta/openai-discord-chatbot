import discord
import chat
import time


intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
bot.event
async def on_ready():
    print("----------------------")
    print("Logged in as")
    print(f"USERNAME : {bot.user.name}")
    print(f"I   D : {bot.user.id}")
    print("---------------------")

@bot.event
async def on_message(message):
    if bot.user.mention in message.content:
        response = chat.chatting(message.content[21:])
        print("-"*10)
        print(time.strftime(f'%m-%d-%H:%M:%S', time.localtime(time.time())),"\n", message.content)
        print(response)
        await message.channel.send(response)

bot.run('TOKEN IS HERE') 