from cmath import log
from distutils.sysconfig import PREFIX
import discord, asyncio
from dotenv import load_dotenv
import os
load_dotenv()

client = discord.Client()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')
        
    if message.content == f'{PREFIX}소루':
        embed = discord.Embed(name="소루", description="여자", color=0x00ff00)
        
        embed.add_field(name="나이", value="약 16세", inline=False)
        embed.add_field(name="키", value="158cm", inline=False)
        embed.add_field(name="몸무게", value="49kg", inline=False)
        embed.add_field(name="혈액형", value="A", inline=False)
        embed.add_field(name="생일", value="2월 17일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="종아하는 음식", value="시조 컴퍼니 독점 음료", inline=False)
        embed.add_field(name="싫어하는 음식", value="피망", inline=False)
        embed.add_field(name="출생지", value="능력자도시 5구역", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="리코더불기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 아라타 母 히나", inline=False)
        embed.add_field(name="신체특징", value="핑큿빛 머리를 핑큿빛 눈을 지니고 있다, 홍조가 남들보다 더 잘드러난다, 피부가 생각보다 하얀편이다, 절벽이다", inline=False)
        embed.add_field(name="이명", value="전격 능력자, 츤데레", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C", inline=False)
        embed.add_field(name="열정", value="8", inline=False)
        embed.add_field(name="지능", value="2", inline=False)
        embed.add_field(name="협조성", value="6", inline=False)
        embed.add_field(name="행동력", value="7", inline=False)
        embed.add_field(name="외모", value="6", inline=False)
        embed.add_field(name="성격", value="5", inline=False)
        
        embed.set_thumbnail(url="")
        
    if message.content.startswith(f'{PREFIX}샌찬'):
        await message.channel.send('```cs\n샌찬\n\n성별:남자\n나이:약 16세\n키:173cm\n몸무게:63kg\n혈액형:O\n생일:7월 23일\n종족:능력자\n종아하는 음식:사과 와플\n싫어하는 음식:여주\n출생지:?\n소속:능력자 학교 3학년\n취미:잠자기\n국적:능력자도시\n\n[가족관계]\n\n父 트라오\n母 레이\n兄 제론\n\n[신체특징]\n\n머리가 푸른색이다. 염색을 하더라도 보통 사람보다 더 빨리 돌아오는듯 하다\n눈이 푸른색이다 하지만 밝게 보이지는 않는다\n\n[이명]\n\n불가역\n하늘 대가리\n\n[능력치]\n\n평가 : D\n\n열정 : 3\n지능 : 8\n협조성 : 1\n행동력 : 10\n외모 : 4\n성격 : 1\n```')
    
    if message.content.startswith(f'{PREFIX}도기'):
        await message.channel.send('```cs\n도기\n\n성별:남자\n나이:약 16세\n키:175cm\n몸무게:64kg\n혈액형:B\n생일:1월 25일\n종족:능력자\n종아하는 음식:쪽갈비\n싫어하는 음식:쓸개즙\n출생지:능력자도시 1구역\n소속:능력자 학교 3학년\n취미:정보수집\n국적:능력자도시\n\n[가족관계]\n\n父 세이도\n母 세리아\n\n[신체특징]\n\n금빛 머리와 금빛 눈을 지니고 있다.\n팔근육이 많다 그래서 그런지 팔뚝이 굵다\n\n[이명]\n\n판타지 브레이커\n환살\n\n[능력치]\n\n평가 : B\n\n열정 : 9\n지능 : 7\n협조성 : 4\n행동력 : 9\n외모 : 8\n성격 : 7\n```')
        
    if message.content.startswith(f'{PREFIX}뉴비'):   
        await message.channel.send('```cs\n뉴비\n\n성별:남자\n나이:약 19세\n키:195cm\n몸무게:87kg\n혈액형:A\n생일:4월 6일\n종족:능력자\n종아하는 음식:프로틴\n싫어하는 음식:패스트푸드\n출생지:능력자도시 4구역\n소속:능력자 학교 3학년\n취미:쇠질\n국적:능력자도시\n\n[가족관계]\n\n父 올더\n母 레나\n弟 켄\n\n[신체특징]\n\n붉은 머리를 지니고 있다 선천적으로 붉은 눈을 지녔다해서 머리는 염색한거라 한다\n굉장히 잘생겼다\n겉으로는 드러나지 않지만 신체스팩이 괴물이다\n\n[이명]\n\n능력자학교의 괴물\n호리호리 하지만 우락부락\n\n[능력치]\n\n평가 : A\n\n열정 : 10\n지능 : 1\n협조성 : 10\n행동력 : 10\n외모 : 10\n성격 : 10\n```')

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
