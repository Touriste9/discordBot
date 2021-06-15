# bot.py


import discord
import random
import os

TOKEN = 'ODUzOTY2NDY4ODAyOTM2ODQz.YMdEQA.N_zBA6UuDeLem9hOOYCfBhUodKQ'
GUILD = 'Great USSR'

client = discord.Client()

insultes = ['marcher sur des Légos', 'gredin', 'tête de têtard', 'sac à puces', "espèce d'épinard", 'patate', 'patate douce', 'banane', 'saucisse', 'fils/fille de mouette', 'capitaine de bateau-lavoir', 'cornichon', 'paltoquet', 'philistin', 'terrine', 'foutriquet', 'scélérat', 'mauviette', 'malotru', 'goujat', 'vil faquin', 'maraud', 'désembouteillé des alpages', 'crétin des Alpes', 'Parisien', 'bourgeois', 'peigne-zizi', 'peigne-cul', 'protozoaire', 'ectoplasme', 'cloporte', 'coprophage', "trou duc'", 'fils/fille de colon', 'coprolithes', 'fécalomes', 'enfoiré', 'raclure de bidet', 'classique', 'pelle à brin', 'balai à chiotte', 'fumier', 'matière à compost', 'Va te faire composter', "puisque tu ne sers à rien, va donc pourrir sur un tas de détritus et te faire grignoter par les vers dont les déjections seront plus utiles pour nourrir mes tomates que tout le bien que tu pourrais faire pour l'Humanité", 'un déchet non recyclable', 'sac de boue', 'une ordure', 'pourriture', 'moisissure', 'fond de benne', "je n'ai pas envie de t'insulter, j'ai peur de salir l'insulte", 'au niveau bagage intellectuel, tu voyages léger', 'patient zéro de la connerie', 'bête à bêcher de la flotte', 'pas inventé la machine à courber les bananes', 'bête comme une valise sans poignée', 'internet explorer', 'PNJ mal codé', 'fils de yack', 'yack', 'une vache avec du style', 'macroniste', 'filloniste', 'lepéniste', 'mélenchoniste', 'sarkozyste', 'capitaliste', 'homéopathe', 'antivax', 'banquier', 'consultant', 'président de BDE', 'trader', 'fils de trader', 'négociant de F-35', 'journaliste', 'moule à gaufre', 'escogriffe', 'andouille', 'tocard', 'bouffon', 'zigoto', 'saltimbanque', 'termaji', 'branquignole', 'enclume', 'allez bien vous faire cuire le cul', 'takezen', 'torr penn', 'casse-gonades', 'pimfle', 'caillou', 'goulamas', 'gougnafier', 'pouffre', 'poulpe', 'figure de pain sucé', "figure d'angoisse", "front d'endive", 'tronc de figuier', 'guit']
membres = []


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    idd = '400981533156179978'
    print(client.get_user(idd))

    

@client.event
async def on_member_join(member):
    await member.send('Bienvenue sur le serveur')

@client.event
async def on_message(message):
    
    if 'OncheBot' in str(message.author):
        return
    
    print(message.content)
    print(message.author)
    print(message.author.id)
    print(membres)
    if len(membres) > 0:
        print(type(membres[0]))
    print('-------------------')
       
    #await message.author.send('MODE NUCLEAIRE ACTIVE')
    if message.author in membres:
        f=0
    else:
        membres.append(message.author)
        membres.append(message.author.id)
    
    if message.content.startswith('!insultemp'):
        trouve = False
        for w in range(len(membres)):
            print(membres[w], 'onche')
            if str(membres[w]) in message.content and w%2 == 1:
                trouve = True
                msg = insultes[random.randint(0, len(insultes)-1)]
                await membres[w - 1].send(msg)
        if trouve == False:
            await message.channel.send("désolé, cette personne n'a encore jamais envoyé de message depuis que je suis connecté")
    elif message.content.startswith('!insulte'):
        trouve = False
        for w in range(len(membres)):
            print(membres[w], 'onche')
            if str(membres[w]) in message.content and w%2 == 1:
                trouve = True
                msg = insultes[random.randint(0, len(insultes)-1)]
                await message.channel.send("@" + str(membres[w - 1]) + " " + msg)
        if trouve == False:
            await message.channel.send("désolé, cette personne n'a encore jamais envoyé de message depuis que je suis connecté, petit tricheur :)")
            
        
    if message.content.startswith('!help'):
        await message.channel.send("""```m
!insulte (personne) sert à insulter quelqu'un devant la face du monde
```""")
        await message.channel.send("""```m
!insultemp (personne) sert à insulter quelqu'un en mp ^^
```""")
        await message.channel.send("""```m
!onchage (texte) sert à embellir vos textes de onche
```""")

        
    if message.content.startswith('!onchage'):
        
        
        if len(message.content)>9:
            mess = message.content[9:]
        else:
            mess = message.content[8:]
        final = []
        for mot in mess.split(" "):
            print(mot)
            if len(mot) > 5:
                cons = False
                consonnes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
                for h in range(len(mot)-1):
                    if mot[len(mot)-1-h] in consonnes:
                        if cons == False:
                            final.append(mot[:(len(mot)-h)] + 'onche')
                            final.append(" ")
                        cons = True
                if cons == False:
                    final.append(mot)
                    final.append(" ")
            else:
                final.append(mot)
                final.append(" ")
        finalm = ''
        for w in final:
            finalm = finalm + w
            
        await message.channel.send("""```py
""" + str(finalm) + """
```""")
        
    elif 'onche onche party nucleaire' in message.content:
        await message.channel.send('MODE NUCLEAIRE ACTIVE')
        for x in range(100):
            await message.channel.send("""```py
onche
```""")

client.run(TOKEN)