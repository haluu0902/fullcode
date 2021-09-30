import discord
import asyncio
import time
loop = False
def send():
    token = "ODY2NzEwOTI4NDYzNzU3Mzcy.YPWhdA.pVc8QBjryyMgam8iUq43twiLVtM"

    client = discord.Client()

    @client.event
    async def on_reply():
        print("We have logged in as {0.user}".format(client))    

    @client.event
    async def on_ready():
        print("Success!")

    @client.event
    async def on_message(message):
        if(message.author == client.user):
            return
        if message.content.startswith("$last"):
            temp = ""
            ra = open("./data/history_dice.txt", "r")
            dataRa = ra.read()
            dataRa = dataRa.split("\n")
            ra.close()
            for i in range(len(dataRa) -20,len(dataRa)):
                temp +=dataRa[i]+"\n"
            await message.channel.send(temp)
        if message.content.startswith("$all"):
            temp = ""
            ra = open("./data/history_dice.txt", "r")
            dataRa = ra.read()
            dataRa = dataRa.split("\n")
            ra.close()
            for i in range(len(dataRa)-60,len(dataRa)):
                temp +=dataRa[i]+"\n"
            await message.channel.send(temp)
        if message.content.startswith("$file"):
            await message.channel.send("Here", file= discord.File("./data/history_dice.txt"))

    client.run(token)