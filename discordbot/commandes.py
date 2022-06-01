import discord 
from discord.ext import commands

client = discord.Client()

# faire le bot
@client.event
async def on_message(message):

    #Créer le message commande et le stylise avec une couleur et une image
    if message.content == ('!commandes'):
        embed = discord.Embed(title = "**Commandes**", color = 0x880808, description = "Voici quelques commandes que vous pouvez utiliser à votre guise : \n ------------------------------------------------ \n***!aide*** pour appeler du renfort \n***!question*** pour vous débarasser d un **✨soucis✨** ennuyeux \n***!reset*** pour revoir votre méthode d approche depuis le début \n***!retour*** pour revenir à l étape précédente \n ------------------------------------------------" , foot = "Passez une agréable journée et que vos entreprises soient pleines de succès ⋆ටᴗට⋆")
        embed.set_footer(text = "Passez une agréable journée et que vos entreprises soient pleines de succès ⋆ටᴗට⋆")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/15/8b/ed/158bed9819e4fccf7e18a5eeeaf79c6b.png")
        await message.channel.send(embed=embed)

    #Créer le message recette
    if message.content == ('!recette'):
        recipe = discord.Embed(title = "** Recette du Tiramisu à la mode de chez nous**", color = 0xC9822C, description = "**ÉTAPE 1** Séparer les blancs des jaunes d'oeufs. \n **ÉTAPE 2** Mélanger les jaunes avec le sucre roux et la poudre d'os. \n **ÉTAPE 3** Ajouter le mascarpone au fouet. \n **ÉTAPE 4** Monter les blancs en neige et les incorporer délicatement à la spatule au mélange précédent. Réserver. \n **ÉTAPE 5** Mouiller les doigts encore chauds dans le sang rapidement avant d'en tapisser le fond du plat. \n **ÉTAPE 6** Recouvrir d'une couche de crème au mascarpone puis répéter l'opération en alternant couche de biscuits et couche de crème en terminant par cette dernière.\n **ÉTAPE 7** Saupoudrer de cheveux. \n **ÉTAPE 8** Mettre au réfrigérateur 4 heures minimum puis déguster frais.")
        recipe.set_thumbnail(url="https://i.kym-cdn.com/entries/icons/facebook/000/021/267/swedish_chef.jpg")
        await message.channel.send(embed=recipe)
    
    #Fonction supprimer
    if message.content == "del":
        await message.channel.purge(limit=3)

    #Commande pour 
    if message.content == ('!lieux'): 
        lieux = discord.Embed(title = "**Les bonnes adresses**", color = 0x000000, description = "Voici une petite selection de notre équipe pour trouver des lieux où opérer en toute tranquillité : ")
        lieux.add_field(name = "Jardin de Salma", value = "Un coin pittoresque à l'abri des regards \n Place d'Armes, 78000 Versailles")
        lieux.add_field(name = "Tour Eiffel", value = "Pas le plus discret mais la vue est à couper le souffle \n Champ de Mars, 5 Av. Anatole France, 75007 Paris")
        lieux.add_field(name = "Triangle des Bermudes", value = "Un peu difficile d'accès, mais vous serez sûr qu'on ne le retrouvera jamais \n Océan Atlantique, quelque part")
        lieux.add_field(name = "Disneyland", value = "Même votre victime va adorer l'ambiance là bas \n Bd de Parc, 77700 Coupvray ")
        await message.channel.send(embed=lieux)

    
client.run("OTc4MjI5MjYxODg0MzM0MTgw.GZ3y-e.25LaGYzJBf6WQAmN0g8hu64QVKEyPpCMyro3ds")