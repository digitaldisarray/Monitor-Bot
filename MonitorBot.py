# Make sure you have discord.py and asyncio installed!
import discord
import asyncio

# Made By: Digital Disarray
# Purpose of this bot is to log messages from certain people.

client = discord.Client()

error = '[ ERROR ] - '
warn =  '[ WARN ] -'
info =  '[ INFO ] - '

f = open('./watch-list.txt')
raw = f.read()
users = raw.split(':')
content = ""

@client.event
async def on_ready():
    print(info + 'Logged In!')
    print('=====================')
    print('Username: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('=====================')
    print(info + str(len(users)) + " user(s) on the watch list.")


@client.event
async def on_message(message):
    content = str(message.content)
    # Check if message was a command
    # TODO: Load bot prefixes from a file
    if content.startsWith(("!", "?")):
        cmdLogFile = open('./cmd-logs.txt', 'w')
        cmdLogFile.write(str(message.author) + " issued " + str(message.content))
        cmdLogFile.close()
        print(info + str(message.author) + " issued " + str(message.contents))
    
    # Check watch list
    for i in range(len(users)):
        if str(message.author) == users[i]:
            logFile = open('./logs.txt', "w")
            logFile.write(str(message.author) + " sent " + str(message.content))
            logFile.close()
            print(info + str(message.author) + " sent " + str(message.content))
            

client.run('PUT YOUR TOKEN HERE') # Make sure you have added your own token!
