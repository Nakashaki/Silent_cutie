# mettre l'id de l'utilisateur qui a entré le premier message avec !question dans une list_Node
# faire le parcours classique avec la list_Node et la list_past
# comparer l'id de l'utilisateur à chaque message:
#     si c'est le même qui a mit en premier !question: continuer la boucle
#     si un autre utilisateur rentre un message: 
#         si message.content == !question:
#             créer d'autre listes (ex: liste_Node2 et list_past2) et faire la boucle avec ses nouvelles listes
#         si message.content 




# member.display_name

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


current_node = Root
list_past = []
client = commands.Bot(command_prefix="!")


# renvoyer le message entier de l'utilisateur 
@client.command()
async def question(ctx):
    global current_node
    await ctx.send(current_node.question)

@client.command()
async def retour(ctx):
    global current_node
    global list_past
    current_node = list_past[-1]
    list_past.pop()
    await ctx.send(current_node.question)

@client.command()
async def reset(ctx):
    global current_node
    global list_past
    list_past.clear()
    current_node = Root
    await ctx.send(current_node.question)


@client.event
async def on_message(message):
    global current_node
    global list_past
    message.content = message.content.lower()
    for child in current_node.list_Node:
        if message.content in child.keyword:
            print(child.question + " " + child.keyword)
            print("----")
            list_past.append(current_node)
            current_node = child   
            await message.channel.send(current_node.question) 
            break
              
    await client.process_commands(message)

    

# faire le bot
client.run("OTc4MjI5MjM5OTQzOTQ2MjYx.GESbcU.YnIdBnwxtZznDRamedDVLHCa7tq47-npARYK7E")