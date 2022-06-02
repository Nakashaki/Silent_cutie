import discord
from discord.ext import commands


class Node:
    def __init__(self,keyword,question):
        self.question = question
        self.keyword = keyword
        self.list_Node = []

    def insert_node(self,question,next_node):
        global child
        if self.question == question:
            self.list_Node.append(next_node)

        for child in self.list_Node:
            child.insert_node(question,next_node)

def GenerateNode():
    Root = Node("","Est il vraiment mort ?")

    Root.insert_node( "Est il vraiment mort ?",Node("oui","est ce que quelqu'un vous a vu faire votre affaire ?"))
    Root.insert_node( "Est il vraiment mort ?",Node("non","voulez vous de l'aide pour terminer le travail ?"))

    Root.insert_node( "voulez vous de l'aide pour terminer le travail ?",Node("oui","Des Individus ont besoin de votre aide <@&939084927184556063>"))
    Root.insert_node( "voulez vous de l'aide pour terminer le travail ?",Node("non","est ce que quelqu'un vous a vu faire votre affaire ?"))

    Root.insert_node( "est ce que quelqu'un vous a vu faire votre affaire ?",Node("oui","https://tenor.com/bR26J.gif"))
    Root.insert_node( "est ce que quelqu'un vous a vu faire votre affaire ?",Node("non","Avez vous fait le travail tout seul ?"))

    Root.insert_node( "Avez vous fait le travail tout seul ?",Node("oui","fait il jour ou nuit ?"))
    Root.insert_node( "Avez vous fait le travail tout seul ?",Node("non","pouvez vous portez le corps ?"))

    Root.insert_node( "pouvez vous portez le corps ?",Node("oui","Portez le cadavre tous ensemble"))
    Root.insert_node( "pouvez vous portez le corps ?",Node("non","Avez vous un objet coupant ?"))

    Root.insert_node( "Avez vous un objet coupant ?",Node("oui","Couper les articulations et enterrez-le"))
    Root.insert_node( "Avez vous un objet coupant ?",Node("non","Trouver de quoi faire fondre le corps"))

    Root.insert_node( "fait il jour ou nuit ?",Node("jour","Attendez la nuit du coup"))
    Root.insert_node( "fait il jour ou nuit ?",Node("nuit","Privilegiez entre 4h et 5h pour agir"))

    return Root


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_command_error(ctx, error):
    print(error)
    await ctx.send(error)

@bot.command()
async def commandes(ctx):
    """A better vizualized help menu"""
    embed = discord.Embed(title = "**Commandes**", color = 0x880808, description = "Voici quelques commandes que vous pouvez utiliser à votre guise : \n ------------------------------------------------ \n***!aide*** pour appeler du renfort \n***!question*** pour vous débarasser d un **✨soucis✨** ennuyeux \n***reset*** pour revoir votre méthode d approche depuis le début \n***return*** pour revenir à l étape précédente \n***break*** pour arrêter la discussion \n ------------------------------------------------" , foot = "Passez une agréable journée et que vos entreprises soient pleines de succès ⋆ටᴗට⋆")
    embed.set_footer(text = "Passez une agréable journée et que vos entreprises soient pleines de succès ⋆ටᴗට⋆")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/15/8b/ed/158bed9819e4fccf7e18a5eeeaf79c6b.png")
    await ctx.message.channel.send(embed=embed)

@bot.command()
async def recette(ctx):
    """A better vizualized help menu"""
    recipe = discord.Embed(title = "** Recette du Tiramisu à la mode de chez nous**", color = 0xC9822C, description = "**ÉTAPE 1** Séparer les blancs des jaunes d'oeufs. \n **ÉTAPE 2** Mélanger les jaunes avec le sucre roux et la poudre d'os. \n **ÉTAPE 3** Ajouter le mascarpone au fouet. \n **ÉTAPE 4** Monter les blancs en neige et les incorporer délicatement à la spatule au mélange précédent. Réserver. \n **ÉTAPE 5** Mouiller les doigts encore chauds dans le sang rapidement avant d'en tapisser le fond du plat. \n **ÉTAPE 6** Recouvrir d'une couche de crème au mascarpone puis répéter l'opération en alternant couche de biscuits et couche de crème en terminant par cette dernière.\n **ÉTAPE 7** Saupoudrer de cheveux. \n **ÉTAPE 8** Mettre au réfrigérateur 4 heures minimum puis déguster frais.")
    recipe.set_thumbnail(url="https://i.kym-cdn.com/entries/icons/facebook/000/021/267/swedish_chef.jpg")
    await ctx.message.channel.send(embed=recipe)

@bot.command()
async def lieux(ctx):
    """A better vizualized help menu"""
    lieux = discord.Embed(title = "**Les bonnes adresses**", color = 0x000000, description = "Voici une petite selection de notre équipe pour trouver des lieux où opérer en toute tranquillité : ")
    lieux.add_field(name = "Jardin de Salma", value = "Un coin pittoresque à l'abri des regards \n Place d'Armes, 78000 Versailles")
    lieux.add_field(name = "Tour Eiffel", value = "Pas le plus discret mais la vue est à couper le souffle \n Champ de Mars, 5 Av. Anatole France, 75007 Paris")
    lieux.add_field(name = "Triangle des Bermudes", value = "Un peu difficile d'accès, mais vous serez sûr qu'on ne le retrouvera jamais \n Océan Atlantique, quelque part")
    lieux.add_field(name = "Disneyland", value = "Même votre victime va adorer l'ambiance là bas \n Bd de Parc, 77700 Coupvray ")
    await ctx.message.channel.send(embed=lieux)


@bot.command()
async def say(ctx, *, msg):
    """Say something i repeat after you"""
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def question(ctx):
    def Check(m: discord.Message):
        return ctx.message.author.id == m.author.id and ctx.message.channel.id == m.channel.id

    current_node = GenerateNode()
    list_past = []
    run = True
    await ctx.send(current_node.question)
    message = await bot.wait_for('message', check=Check)
    while run:
        if message.content == "break":
            await ctx.send("Finished !")
            run = False
        elif message.content == "reset":

            list_past.clear()

            current_node = GenerateNode()

            await ctx.send(current_node.question)
        elif message.content == "return":


            current_node = list_past[-1]
            list_past.pop()

            await ctx.send(current_node.question)
        for child in current_node.list_Node:
            if message.content in child.keyword:
                list_past.append(current_node)
                current_node = child   

                await ctx.send(current_node.question) 
                break
        
        message = await bot.wait_for('message', check=Check)
    

@bot.event
async def on_message(message):
    if message.content == "del":
        await message.channel.purge(limit=3)
    await bot.process_commands(message)

    
# faire le bot
bot.run("OTc4MjI5MjM5OTQzOTQ2MjYx.GESbcU.YnIdBnwxtZznDRamedDVLHCa7tq47-npARYK7E")