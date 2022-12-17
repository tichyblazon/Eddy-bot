import discord
import os
import requests
import random
import asyncio
import schedule

from replit import db
from keep_alive import keep_alive
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="e!")

client = discord.Client()
prikaz = ["maznak"]
list_prikazov = [
    "e!maznak- napíše povzbudivé slová",
    "e!play- spustí ytb odkaz",
    "e!pause- zastaví hudbu",
]
povzbudenie = [
    "Si skvelý",
    "To zvládneš poklad",
    "Si šikulkaaa",
    "Držíme ti s Biancou palce",
    "Poď ma objať",
]
dobre_rano = ["Dobré ráno", "Dobré ránko", "Aj tebe dobré ráno"]
pozdrav_input = [
    "Ahoj",
    "Ahooj",
    "ahoj",
    "ahooj",
    "Pekný deň prajem",
    "Čau",
    "čau",
    "Servus",
    "servus",
    "Čauko",
    "čauko",
    "aoj",
]

pozdrav_output = [
    "Ahoj",
    "Ahooj",
    "Pekný deň prajem",
    "Čau",
    "Servus",
    "Čauko",
]
odpovede_vyspatie = [
    "Zle som sa vyspal",
    "Dobre som spinkal",
    "Ešte by som spinkal, lebo som unavený",
    "Ni dobre, poďme ešte haji haji",
    "Nyo dalo sa a ty si sa ako vyspal?",
    "Musím ešte veľa spinkať",
]

odpovede_den = [
    "Dobrý som mal dník", "Bolo aj lepšie",
    "Lepší by bol ak by sme sa maznali", ""
]


def update_povzbudive_slova(povzbudiva_sprava):
    if "povzbudive_slova" in db.keys():
        povzbudive_slova = db["povzbudive_slova"]
        povzbudive_slova.append(povzbudiva_sprava)
        db["povzbudive_slova"] = povzbudive_slova
    else:
        db["povzbudive_slova"] = ["povzbudiva_sprava"]


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        msg = message.content
        #konverzácie
        if any(word in msg for word in pozdrav_input):
            await message.channel.send(random.choice(pozdrav_output))

        if msg.startswith("Dobré ráno"):
            await message.channel.send(random.choice(dobre_rano))

        if msg.startswith("Ako si sa vyspal?"):
            await message.channel.send(random.choice(odpovede_vyspatie))

        if msg.startswith("Aký si mal deň?"):
            await message.channel.send(random.choice(odpovede_den))

        if msg.startswith("hihi"):
            await message.channel.send("hihi")

        if msg.startswith("Dobrú noc"):
            await message.channel.send("Dobrú noc aj tebe <3")

        if msg.startswith("dobrú noc"):
            await message.channel.send("Dobrú noc aj tebe <3")

        options = povzbudenie
        if "povzbudive_slova" in db.keys():
            options = options + db["povzbudive_slova"].value

#help prikaz
        if msg.startswith("help"):
            await message.channel.send(list_prikazov)

#povzbudenie
        if any(word in msg for word in prikaz):
            await message.channel.send(random.choice(options))

        if msg.startswith("!pridat"):
            povzbudiva_sprava = msg.split("!pridat", 1)[1]
            update_povzbudive_slova("")
            await message.channel.send("Bolo pridané nové povzbudenie.")


#posielanie správ v presný čas

target_channel_id = "912084079757897758"

#obrazky

#ytb

#server veci
keep_alive()
client.run(os.getenv("TOKEN"))
