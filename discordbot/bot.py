import discord

client = discord.Client()

# #faire le bot


@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return
    #Appel d'un modérateur en cas de besoin
    if message.content == ('$aide'):
        await message.channel.send('Des Individus ont besoin de votre aide ''<@&939084927184556063>')









#ID du bot de Raphaël
client.run("OTc4MjI5Mjg1MjUwODEzOTUy.G1dvQN.QCDgRUzDMETutawEzuXg8MXm-jBcNwCUsx6WUU")
