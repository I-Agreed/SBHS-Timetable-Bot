import discord
import time
import asyncio

client = discord.Client()
monday = {(9, 0):"Period 1 is about to start", (10, 5):"Period 1 has finished, period 2 will begin shortly",
          (11, 10):"Period 2 has finished, it is now lunch 1", (11, 30):"It is now lunch 2", (11,47):"Lunch 2 is over, period 3 will begin shortly",
          (12,50): "Period 3 is over, period 4 will begin shortly", (13,55): "Period 4 is over, it is now recess", (14,12): "Recess is over, period 5 will begin shortly",
          (15, 15):"End of the school day"}

wednesday = {(9, 0):"Period 1 is about to start",  (10, 5):"Period 1 has finished, period 2 will begin shortly",
             (11, 10):"Period 2 has finished, it is now recess", (11, 27):"Recess is over, period 3 will begin shortly",
             (12, 30):"Period 3 is over, it is now lunch 1", (12, 50):"It is now lunch 2",
             (13, 7):"Lunch 2 is over, period 4 will begin shortly", (14, 10):"Period 4 is over, period 5 will begin shortly",
             (15, 15):"End of the school day"}

friday = {(9, 28):"Period 1 is about to start", (10, 25):"Period 1 has finished, period 2 will begin shortly",
          (11, 25):"Period 2 has finished, it is now recess", (11, 42):"Recess is over, period 3 will begin shortly",
          (12, 40):"Period 3 is over, it is now lunch 1", (13, 0):"Lunch 1 is over, it is now lunch 2", (13, 17):"Lunch is over, period 4 will begin shortly",
          (14, 15):"Period 4 is over, period 5 will begin shortly", (15, 15):"End of the school day"}

channelId = 1 #Enter channel id
roleName = "" #Enter role name exactly
token = ""    #Enter bot token

async def task():
    await client.wait_until_ready()
    channel = client.get_channel(channelId)
    server = channel.guild
    role = None
    for i in server.roles:
        if i.name == roleName:
            role = i
    while client.is_closed:
        
        cTime = tuple([int(i) for i in time.ctime().split()[3].split(":")[:2]])
        day = time.ctime().split()[0]
        message = "``` ``` {}. "+role.mention
        if day == "Mon":
            if cTime in monday:
                await channel.send(message.replace("{}", monday[cTime]))
                await asyncio.sleep(60)
        elif day == "Tue":
            if cTime in monday:
                await channel.send(message.replace("{}", monday[cTime]))
                await asyncio.sleep(60)
        elif day == "Wed":
            if cTime in wednesday:
                await channel.send(message.replace("{}", wednesday[cTime]))
                await asyncio.sleep(60)
        elif day == "Thu":
            if cTime in wednesday:
                await channel.send(message.replace("{}", wednesday[cTime]))
                await asyncio.sleep(60)
        elif day == "Fri":
            if cTime in friday:
                await channel.send(message.replace("{}", friday[cTime]))
                await asyncio.sleep(60)
        await asyncio.sleep(1)

            
  
client.loop.create_task(task())
client.run(token)
