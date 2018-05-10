# Necesitas discord.py instalado!
import discord
import asyncio

# Hecho Por: Digital Disarray
# Este bot registra mensajes de personas.

client = discord.Client()

error = '[ Error ] - '
warn =  '[ Advertencia ] -'
info =  '[ Información ] - '

f = open('./watch-list.txt')
raw = f.read()
users = raw.split(':')
content = ""

@client.event
async def on_ready():
    print(info + 'Connectado!')
    print('=====================')
    print('Usario: ' + client.user.name)
    print('Identidad de Usuario: ' + client.user.id)
    print('=====================')
    print(info + str(len(users)) + " usuarios en la lista de observación.")


@client.event
async def on_message(message):
    content = str(message.content)
    # Check if message was a command
    # TODO: Load bot prefixes from a file
    if content.startsWith(("!", "?", ".", ":")):
        cmdLogFile = open('./cmd-logs.txt', 'w')
        cmdLogFile.write(str(message.author) + " expedido " + str(message.content))
        cmdLogFile.close()
        print(info + str(message.author) + " expedido " + str(message.contents))
    
    # Check watch list
    for i in range(len(users)):
        if str(message.author) == users[i]:
            logFile = open('./logs.txt', "w")
            logFile.write(str(message.author) + " envió el mensaje " + str(message.content))
            logFile.close()
            print(info + str(message.author) + " envió el mensaje " + str(message.content))
            

client.run('pon tu ficha aquí') # Necesitas escribir tu token aquí!
