# coding=utf-8
import discord
import asyncio
import random
import datetime



client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------------")
    await  client.change_presence(game=discord.Game(name='무언가를', type=1))

@client.event
async def on_message(message, await=None):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요")

    if message.content.startswith('!주사위'):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0])+1):
            dice = dice + random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))

    if message.content.startswith('!골라'):
        choice = message.content.split(" ")
        choicenember = random.randint(1, len(choice)-1)
        choicersult = choice[choicenember]
        await client.send_message(message.channel, choicersult)

    if message.content.startswith('!뭐먹지'):
        food = "짜장면 짬뽕 라면 밥 굶기 족발 치킨 햄버거 집에있는거 김밥"
        foodchoice = food.split(" ")
        foodnember = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnember-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith("!팀나누기"):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await client.send_message(message.channel, person[i] + "-->" + teamname[i])

    if message.content.startswith("!명령어"):
        await client.send_message(message.channel, ".!안녕 .!주사위 .!골라 .!뭐먹지 .!팀나누기 ")

    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)﻿
        embed = discord.Embed(color=0x00B0FF)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year +  "년" + str(date.month +  "월" + str(date.day +  "일"), inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avator_ulr)
        await client.send_message(message.channel, embed=embed)








client.run('NTM2NzIwMDM2ODg3MjY1Mjkw.DybAoQ.dVF9cwdvJMhL8GTtLG844aEAMK8')

