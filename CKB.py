#*********************************************************************************************************************************************************
import asyncio
from operator import index      #|
from posixpath import split     #|
from re import M                #|
from typing import Sized, Text        #|
import discord                  #|
from discord import shard       #|
from discord import file
from discord import message        #|
from discord.colour import Color #|
from discord.embeds import Embed #|
from discord.ext import commands #|
from discord.utils import get    #|
import requests                  #|
from bs4 import BeautifulSoup    #|
import praw                      #|
import os                        #|
import random                    #|
import json
from requests.models import Response    
import async_timeout
import asyncio                  #|
import datetime
import time
#*********************************************************************************************************************************************************
path = os.path.dirname(os.path.abspath(__file__))+"/"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Prefix
client = commands.Bot(command_prefix = '+')
@client.command()
@commands.has_permissions(administrator=True)
async def temizle(ctx,*,amount=5):
    await ctx.channel.purge(limit=amount)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Avatar#
@client.command()
async def avatar(ctx,member:discord.Member):
    embed = discord.Embed(color = discord.Color.dark_purple())
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name= " Ne güzel Avatar :heart_eyes: ",value=f"{member.display_name}") 
    embed.set_image(url="{}".format(member.avatar_url))
    await ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#sözler
@client.command()
async def sozler(ctx):
    with open(path+"sozler.txt",encoding="utf-8") as f:
         lines = f.readlines()
         sozler = random.choice(lines)
         sozler = sozler.split("-")
         embed = discord.Embed(color=discord.Color.red())
         embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
         embed.add_field(name=f'{sozler[0]}',value=f"~{sozler[1]}", inline= False)
         await ctx.send(embed=embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#anime sözleri
@client.command()
async def asoz(ctx):
    with open(path+"asoz.txt",encoding="utf-8") as f:
         lines = f.readlines()
         asoz = random.choice(lines)
         asoz = asoz.split("-")
         embed = discord.Embed(color=discord.Color.red())
         embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
         embed.add_field(name=f'{asoz[0]}',value=f"~{asoz[1]}", inline= False)
         await ctx.send(embed=embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#kedi
@client.command()
async def kedi(ctx):
        response = requests.get('https://aws.random.cat/meow')
        kedii = response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'Ayy  çok tatlıı :heart_eyes: ', value = "Ya da huysuz :angry: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=kedii['file'])  
        await  ctx.send(embed=embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def köpek(ctx):
        Response = requests.get("https://dog.ceo/api/breeds/image/random")
        dog = Response.json()
        embed=discord.Embed(color=discord.Color.purple())
        embed.add_field(name = 'Ayy  çok tatlıı :heart_eyes: ', value = "Ya da huysuz :angry: ", inline = False)
        embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_image(url=dog['message'])
        await  ctx.send(embed=embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def Anime(ctx):
    path = random.choice(os.listdir('animeler/'))
    await ctx.send(file=discord.File("animeler/"+path))
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, time=None,reason=None):
    if not member:
        await ctx.send("Susturmak istediğin kişiyi seçmelisin!")
    elif not time:
        await ctx.send("Süre girmek zorundasın!")
        try:
            seconds = time[:-1]
            duration = time[-1]
            if duration=="s":
             seconds=seconds*1
            elif duration=="m":
                seconds=seconds*60
            elif duration=="h":
                seconds=seconds*60*60
            elif duration=="d":
                seconds=seconds*86400
            else:
             await ctx.send("Yanlış bir süre girdin !")
            return
        except Exception as e:
            print(e)
        await ctx.send("Invalid time input")
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await member.add_roles(mutedRole, reason=reason)
        muted_embed = discord.Embed(title="Muted a user", description=f"{member.mention} Was muted by {ctx.author.mention} for {reason} to {time}")
        embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
        await ctx.send(embed=muted_embed)
        await asyncio.sleep(seconds)
        await member.remove_roles(mutedRole)
        unmute_embed = discord.Embed(title="Mute over!", description=f"{ctx.author.mention} muted to {member.mention} for {reason} is over after {time}")
        await ctx.send(embed=unmute_embed)
    #await ctx.send(embed=embed)
    #await member.add_roles(mutedRole, reason=reason)
    #await member.send(f" you have been muted from: {guild.name} reason: {reason}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def Haklısın(ctx):
     path=random.choice(os.listdir('Haklısın/'))
     await ctx.send(embedfile=discord.File("Haklısın/"+path))
#----------------------------------------------------------------------------------------------------
@client.command()
async def hmm(ctx):
    path=random.choice(os.listdir('hmm/'))
    await ctx.send(file=discord.File("hmm/"+path))
#----------------------------------------------------------------------------------------------------
@client.command()
async def Katılıyorum(ctx):
        path=random.choice(os.listdir('katılıyorum/'))
        await ctx.send(file=discord.File("katılıyorum/"+path))
#----------------------------------------------------------------------------------------------------
@client.command()
async def katılmıyorum(ctx):
        path=random.choice(os.listdir('katılmıyorum/'))
        await ctx.send(file=discord.File("katılmıyorum/"+path))
#-------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def Agif(ctx):
    path = random.choice(os.listdir('agif/'))
    await ctx.send(file=discord.File("agif/"+path))
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def Yemek(ctx):
    path=random.choice(os.listdir('yemek/'))
    await ctx.send(file=discord.File("yemek/"+path))
#------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def Rock(ctx):
    ctx.send("https://www.youtube.com/playlist?list=PL7F3KuKVrBpU_cJWW6QZy4vRcxWaGAdQj")
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
client.run('')
