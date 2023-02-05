from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import asyncio
import pytz
import datetime
from discord.ext import commands
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()
intents = discord.Intents.all()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("문의는 Sina#4229"))

@client.event
async def on_member_join(member):
    if member.dm_channel:
        channel = member.dm_channel
    else:
        channel = await member.create_dm()
    name = member.name
    await channel.send(f"{name}님, 안녕하세요! 클랜 Signus 디스코드에 오신걸 환영합니다.")
        
@client.event
async def on_message(message):
    if message.content.startswith ("!인증 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. Sina#4229")
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '클랜원')
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
