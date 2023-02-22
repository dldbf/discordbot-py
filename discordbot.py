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
        embed = discord.Embed(name="소루", description="소루", color=0xff71d9)
        embed.add_field(name="성별", value="여자", inline=False)
        embed.add_field(name="나이", value="약 16세", inline=False)
        embed.add_field(name="키", value="158cm", inline=False)
        embed.add_field(name="몸무게", value="49kg", inline=False)
        embed.add_field(name="혈액형", value="A", inline=False)
        embed.add_field(name="생일", value="2월 17일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="종아하는 음식", value="시조 컴퍼니 독점 음료", inline=False)
        embed.add_field(name="싫어하는 음식", value="피망", inline=False)
        embed.add_field(name="출생지", value="능력자도시 5구역", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="리코더불기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 아라타 母 히나", inline=False)
        embed.add_field(name="신체특징", value="핑큿빛 머리를 핑큿빛 눈을 지니고 있다\n홍조가 남들보다 더 잘드러난다\n피부가 생각보다 하얀편이다\n절벽이다", inline=False)
        embed.add_field(name="이명", value="전격 능력자\n츤데레", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C", inline=False)
        embed.add_field(name="열정", value="8", inline=False)
        embed.add_field(name="지능", value="2", inline=False)
        embed.add_field(name="협조성", value="6", inline=False)
        embed.add_field(name="행동력", value="7", inline=False)
        embed.add_field(name="외모", value="6", inline=False)
        embed.add_field(name="성격", value="5", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1076482260963962995/1076540158050058301/1e11e98d61e277c7.gif")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}샌찬':
        embed = discord.Embed(name="샌찬", description="샌찬", color=0x00b8d3)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 16세", inline=False)
        embed.add_field(name="키", value="173cm", inline=False)
        embed.add_field(name="몸무게", value="63kg", inline=False)
        embed.add_field(name="혈액형", value="O", inline=False)
        embed.add_field(name="생일", value="7월 23일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="종아하는 음식", value="사과 와플", inline=False)
        embed.add_field(name="싫어하는 음식", value="여주", inline=False)
        embed.add_field(name="출생지", value="?", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="잠자기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 트라오 母 레이 兄 제론", inline=False)
        embed.add_field(name="신체특징", value="머리가 푸른색이다\n염색을 하더라도 보통 사람보다 더 빨리 돌아오는듯 하다\n눈이 푸른색이다 하지만 밝게 보이지는 않는다", inline=False)
        embed.add_field(name="이명", value="불가역\n하늘 대가리", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="D", inline=False)
        embed.add_field(name="열정", value="3", inline=False)
        embed.add_field(name="지능", value="10", inline=False)
        embed.add_field(name="협조성", value="1", inline=False)
        embed.add_field(name="행동력", value="10", inline=False)
        embed.add_field(name="외모", value="4", inline=False)
        embed.add_field(name="성격", value="1", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}도기':
        embed = discord.Embed(name="도기", description="도기", color=0xffed2a)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 16세", inline=False)
        embed.add_field(name="키", value="175cm", inline=False)
        embed.add_field(name="몸무게", value="64kg", inline=False)
        embed.add_field(name="혈액형", value="B", inline=False)
        embed.add_field(name="생일", value="1월 25일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="종아하는 음식", value="쪽갈비", inline=False)
        embed.add_field(name="싫어하는 음식", value="쓸개즙", inline=False)
        embed.add_field(name="출생지", value="능력자도시 1구역", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="정보수집", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 세이도 母 세리아", inline=False)
        embed.add_field(name="신체특징", value="금빛 머리와 금빛 눈을 지니고 있다\n팔근육이 많다 그래서 그런지 팔뚝이 굵다", inline=False)
        embed.add_field(name="이명", value="판타지 브레이커\n환살", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="B", inline=False)
        embed.add_field(name="열정", value="9", inline=False)
        embed.add_field(name="지능", value="7", inline=False)
        embed.add_field(name="협조성", value="4", inline=False)
        embed.add_field(name="행동력", value="9", inline=False)
        embed.add_field(name="외모", value="8", inline=False)
        embed.add_field(name="성격", value="7", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}뉴비':  
        embed = discord.Embed(name="뉴비", description="뉴비", color=0xeb0000)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 19세", inline=False)
        embed.add_field(name="키", value="195cm", inline=False)
        embed.add_field(name="몸무게", value="87kg", inline=False)
        embed.add_field(name="혈액형", value="A", inline=False)
        embed.add_field(name="생일", value="4월 6일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="종아하는 음식", value="프로틴", inline=False)
        embed.add_field(name="싫어하는 음식", value="패스트푸드", inline=False)
        embed.add_field(name="출생지", value="능력자도시 4구역", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="쇠질", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 올더 母 레나 弟 켄", inline=False)
        embed.add_field(name="신체특징", value="붉은 머리를 지니고 있다 선천적으로 붉은 눈을 지녔다해서 머리는 염색한거라 한다\n굉장히 잘생겼다\n겉으로는 드러나지 않지만 신체스팩이 괴물이다", inline=False)
        embed.add_field(name="이명", value="능력자학교의 괴물\n호리호리 하지만 우락부락", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="A", inline=False)
        embed.add_field(name="열정", value="10", inline=False)
        embed.add_field(name="지능", value="1", inline=False)
        embed.add_field(name="협조성", value="10", inline=False)
        embed.add_field(name="행동력", value="10", inline=False)
        embed.add_field(name="외모", value="10", inline=False)
        embed.add_field(name="성격", value="10", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}블랙':  
        embed = discord.Embed(name="블랙", description="블랙", color=0x5f00a5)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 23세", inline=False)
        embed.add_field(name="키", value="181cm", inline=False)
        embed.add_field(name="몸무게", value="67kg", inline=False)
        embed.add_field(name="혈액형", value="O", inline=False)
        embed.add_field(name="생일", value="5월 13일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="종아하는 음식", value="연어", inline=False)
        embed.add_field(name="싫어하는 음식", value="미역줄", inline=False)
        embed.add_field(name="출생지", value="능력자도시 1구역", inline=False)
        embed.add_field(name="소속", value="아이넨", inline=False)
        embed.add_field(name="취미", value="귀중품 모으기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="신체특징", value="오만한 성격의 소유자로 보라색 머리를 가지고 있다\n오른쪽 귀에 점이있다\n평발이다", inline=False)
        embed.add_field(name="이명", value="아이넨 간부 1\n재벌집 막내아들", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C", inline=False)
        embed.add_field(name="열정", value="7", inline=False)
        embed.add_field(name="지능", value="8", inline=False)
        embed.add_field(name="협조성", value="3", inline=False)
        embed.add_field(name="행동력", value="6", inline=False)
        embed.add_field(name="외모", value="9", inline=False)
        embed.add_field(name="성격", value="2", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
