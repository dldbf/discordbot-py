from cmath import log
from distutils.sysconfig import PREFIX
from discord.ext import commands
from discord.ext.commands import Bot
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
        embed.add_field(name="좋아하는 음식", value="시조 컴퍼니 독점 음료", inline=False)
        embed.add_field(name="싫어하는 음식", value="피망", inline=False)
        embed.add_field(name="출생지", value="능력자도시 5구역", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="리코더불기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 아라타 母 히나", inline=False)
        embed.add_field(name="특징", value="핑큿빛 머리를 핑큿빛 눈을 지니고 있다\n홍조가 남들보다 더 잘드러난다\n피부가 생각보다 하얀편이다\n절벽이다", inline=False)
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
        embed.add_field(name="좋아하는 음식", value="사과 와플", inline=False)
        embed.add_field(name="싫어하는 음식", value="여주", inline=False)
        embed.add_field(name="출생지", value="?", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="잠자기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 트라오 母 레이 兄 제론", inline=False)
        embed.add_field(name="특징", value="머리가 푸른색이다\n염색을 하더라도 보통 사람보다 더 빨리 돌아오는듯 하다\n눈이 푸른색이다 하지만 밝게 보이지는 않는다", inline=False)
        embed.add_field(name="이명", value="불가역\n하늘 대가리", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="D+", inline=False)
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
        embed.add_field(name="좋아하는 음식", value="쪽갈비", inline=False)
        embed.add_field(name="싫어하는 음식", value="쓸개즙", inline=False)
        embed.add_field(name="출생지", value="능력자도시 1구역", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="정보수집", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 세이도 母 세리아", inline=False)
        embed.add_field(name="특징", value="금빛 머리와 금빛 눈을 지니고 있다\n팔근육이 많다 그래서 그런지 팔뚝이 굵다", inline=False)
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
        embed.add_field(name="좋아하는 음식", value="프로틴", inline=False)
        embed.add_field(name="싫어하는 음식", value="패스트푸드", inline=False)
        embed.add_field(name="출생지", value="능력자도시 4구역", inline=False)
        embed.add_field(name="소속", value="능력자 학교 3학년", inline=False)
        embed.add_field(name="취미", value="쇠질", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 올더 母 레나 弟 켄", inline=False)
        embed.add_field(name="특징", value="붉은 머리를 지니고 있다 선천적으로 붉은 눈을 지녔다해서 머리는 염색한거라 한다\n굉장히 잘생겼다\n겉으로는 드러나지 않지만 신체스팩이 괴물이다", inline=False)
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
        embed.add_field(name="좋아하는 음식", value="연어", inline=False)
        embed.add_field(name="싫어하는 음식", value="미역줄기", inline=False)
        embed.add_field(name="출생지", value="능력자도시 1구역", inline=False)
        embed.add_field(name="소속", value="아이넨", inline=False)
        embed.add_field(name="취미", value="귀중품 모으기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="오만한 성격의 소유자로 보라색 머리를 가지고 있다\n오른쪽 귀에 점이있다\n평발이다", inline=False)
        embed.add_field(name="이명", value="아이넨 간부 1\n재벌집 막내아들", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C+", inline=False)
        embed.add_field(name="열정", value="7", inline=False)
        embed.add_field(name="지능", value="8", inline=False)
        embed.add_field(name="협조성", value="3", inline=False)
        embed.add_field(name="행동력", value="6", inline=False)
        embed.add_field(name="외모", value="9", inline=False)
        embed.add_field(name="성격", value="2", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}플라워':  
        embed = discord.Embed(name="플라워", description="플라워", color=0x00855f)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 21세", inline=False)
        embed.add_field(name="키", value="176cm", inline=False)
        embed.add_field(name="몸무게", value="70kg", inline=False)
        embed.add_field(name="혈액형", value="B", inline=False)
        embed.add_field(name="생일", value="9월 10일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="고기", inline=False)
        embed.add_field(name="싫어하는 음식", value="채소", inline=False)
        embed.add_field(name="출생지", value="능력자도시 13구역", inline=False)
        embed.add_field(name="소속", value="아이넨", inline=False)
        embed.add_field(name="취미", value="소녀점프 읽기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="광기넘치는 성격을 가진 미친 남자이다\n다양한 표정을 가지고있다\n목소리가 3옥타브까지 올라간 전적이 있다\n강하다", inline=False)
        embed.add_field(name="이명", value="아이넨 간부 2\n붉은 꽃밭", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C", inline=False)
        embed.add_field(name="열정", value="9", inline=False)
        embed.add_field(name="지능", value="3", inline=False)
        embed.add_field(name="협조성", value="3", inline=False)
        embed.add_field(name="행동력", value="10", inline=False)
        embed.add_field(name="외모", value="5", inline=False)
        embed.add_field(name="성격", value="2", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
    if message.content == f'{PREFIX}미나토 타다요시':  
        embed = discord.Embed(name="미나토 타다요시", description="미나토 타다요시", color=0x474747)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 32세", inline=False)
        embed.add_field(name="키", value="187cm", inline=False)
        embed.add_field(name="몸무게", value="75kg", inline=False)
        embed.add_field(name="혈액형", value="O", inline=False)
        embed.add_field(name="생일", value="8월 30일", inline=False)
        embed.add_field(name="종족", value="무능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="광어회", inline=False)
        embed.add_field(name="싫어하는 음식", value="양갱", inline=False)
        embed.add_field(name="출생지", value="?", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="뜨개질", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="회색 눈을 가지고 있다\n능력자도시의 몇 없는 흑발이다\n시력이 좋지 않아 평소에는 렌즈를 착용하는걸로 보인다", inline=False)
        embed.add_field(name="이명", value="최강의 무능력자\n미나토", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="A", inline=False)
        embed.add_field(name="열정", value="8", inline=False)
        embed.add_field(name="지능", value="10", inline=False)
        embed.add_field(name="협조성", value="8", inline=False)
        embed.add_field(name="행동력", value="8", inline=False)
        embed.add_field(name="외모", value="8", inline=False)
        embed.add_field(name="성격", value="8", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}능도 스토커':
        embed = discord.Embed(name="능도 스토커", description="능도 스토커", color=0xffffff)
        embed.add_field(name="성별", value="?", inline=False)
        embed.add_field(name="나이", value="?", inline=False)
        embed.add_field(name="키", value="?", inline=False)
        embed.add_field(name="몸무게", value="?", inline=False)
        embed.add_field(name="혈액형", value="?", inline=False)
        embed.add_field(name="생일", value="?", inline=False)
        embed.add_field(name="종족", value="?", inline=False)
        embed.add_field(name="좋아하는 음식", value="?", inline=False)
        embed.add_field(name="싫어하는 음식", value="?", inline=False)
        embed.add_field(name="출생지", value="?", inline=False)
        embed.add_field(name="소속", value="?", inline=False)
        embed.add_field(name="취미", value="스토킹", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="?", inline=False)
        embed.add_field(name="이명", value="능도 스토커", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="SSSSSSSSSSSSSSSSSSSSSSSSSS", inline=False)
        embed.add_field(name="열정", value="?", inline=False)
        embed.add_field(name="지능", value="?", inline=False)
        embed.add_field(name="협조성", value="?", inline=False)
        embed.add_field(name="행동력", value="?", inline=False)
        embed.add_field(name="외모", value="?", inline=False)
        embed.add_field(name="성격", value="?", inline=False)
        embed.add_field(name="스토킹", value="1000000000000000000000000000000000000000000000000000000000000", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}이알':
        embed = discord.Embed(name="이알", description="이알", color=0x6fa9de)
        embed.add_field(name="성별", value="여자", inline=False)
        embed.add_field(name="나이", value="약 16세", inline=False)
        embed.add_field(name="키", value="155cm", inline=False)
        embed.add_field(name="몸무게", value="46kg", inline=False)
        embed.add_field(name="혈액형", value="A", inline=False)
        embed.add_field(name="생일", value="2월 22일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="초콜렛", inline=False)
        embed.add_field(name="싫어하는 음식", value="커피", inline=False)
        embed.add_field(name="출생지", value="능력자도시 2구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="그림그리기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 로스 母 에리나", inline=False)
        embed.add_field(name="특징", value="하프 트윈테일의 머리카락을 가지고 있다\n물의 능력자이기 때문에 머리가 금방 마른다\n부끄러움을 많이 타는 성격이지만 자존심은 세다\n~인것이에요 같은 말투를 쓴다\n겁이 많지만 지능적이다", inline=False)
        embed.add_field(name="이명", value="없음", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C+", inline=False)
        embed.add_field(name="열정", value="6", inline=False)
        embed.add_field(name="지능", value="8", inline=False)
        embed.add_field(name="협조성", value="8", inline=False)
        embed.add_field(name="행동력", value="6", inline=False)
        embed.add_field(name="외모", value="7", inline=False)
        embed.add_field(name="성격", value="4", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)

    if message.content == f'{PREFIX}엑스트라':
        embed = discord.Embed(name="엑스트라", description="엑스트라", color=0x000000)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 16세", inline=False)
        embed.add_field(name="키", value="178cm", inline=False)
        embed.add_field(name="몸무게", value="71kg", inline=False)
        embed.add_field(name="혈액형", value="B", inline=False)
        embed.add_field(name="생일", value="7월 20일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="핫초코", inline=False)
        embed.add_field(name="싫어하는 음식", value="우유", inline=False)
        embed.add_field(name="출생지", value="능력자도시 9구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="잠자기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="엑스트라라는 소리를 듣는걸 극도로 싫어한다\n더위를 많이 안탄다\n곱슬머리를 가지고 있다", inline=False)
        embed.add_field(name="이명", value="Extra", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="D", inline=False)
        embed.add_field(name="열정", value="3", inline=False)
        embed.add_field(name="지능", value="2", inline=False)
        embed.add_field(name="협조성", value="5", inline=False)
        embed.add_field(name="행동력", value="6", inline=False)
        embed.add_field(name="외모", value="6", inline=False)
        embed.add_field(name="성격", value="2", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}로원':
        embed = discord.Embed(name="로원", description="로원", color=0x7e5935)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 16세", inline=False)
        embed.add_field(name="키", value="176cm", inline=False)
        embed.add_field(name="몸무게", value="69kg", inline=False)
        embed.add_field(name="혈액형", value="AB", inline=False)
        embed.add_field(name="생일", value="5월 20일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="커피 , 콜라", inline=False)
        embed.add_field(name="싫어하는 음식", value="샐러드", inline=False)
        embed.add_field(name="출생지", value="능력자도시 3구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="장난치기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 母 兄", inline=False)
        embed.add_field(name="특징", value="갈색머리를 가지고 있으며 곱슬머리이다\n머리카락으로 한쪽눈을 가리고 있다\n가끔 살점이 보이지않는다", inline=False)
        embed.add_field(name="이명", value="토막시체", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C+", inline=False)
        embed.add_field(name="열정", value="7", inline=False)
        embed.add_field(name="지능", value="6", inline=False)
        embed.add_field(name="협조성", value="8", inline=False)
        embed.add_field(name="행동력", value="6", inline=False)
        embed.add_field(name="외모", value="4", inline=False)
        embed.add_field(name="성격", value="7", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}리차드':
        embed = discord.Embed(name="리차드", description="리차드", color=0x631500)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 44세", inline=False)
        embed.add_field(name="키", value="185cm", inline=False)
        embed.add_field(name="몸무게", value="72kg", inline=False)
        embed.add_field(name="혈액형", value="AB", inline=False)
        embed.add_field(name="생일", value="10월 2일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="양갱", inline=False)
        embed.add_field(name="싫어하는 음식", value="홍어", inline=False)
        embed.add_field(name="출생지", value="능력자도시 2구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="서적읽기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="붉은 계열의 갈색머리를 가지고 있다\n자신만의 정의를 추구하는 이상자이다\n심장 지병을 앓고 있다\n전투력이 파밀리아리스와도 뒤치지 않는다\n다크서클이 있다", inline=False)
        embed.add_field(name="이명", value="언페이드\n양의 탈을 쓴 늑대", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="B", inline=False)
        embed.add_field(name="열정", value="7", inline=False)
        embed.add_field(name="지능", value="8", inline=False)
        embed.add_field(name="협조성", value="4", inline=False)
        embed.add_field(name="행동력", value="9", inline=False)
        embed.add_field(name="외모", value="9", inline=False)
        embed.add_field(name="성격", value="4", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
    
    if message.content.startswith(f'{PREFIX}에런 이즈라엘'):
        embed = discord.Embed(name="WARNING", description="이 문서는 조작된 문서입니다", color=0x3a6f99)
        embed.add_field(name="이름", value="에런 이즈라엘", inline=False)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="?", inline=False)
        embed.add_field(name="키", value="183cm", inline=False)
        embed.add_field(name="몸무게", value="81kg", inline=False)
        embed.add_field(name="혈액형", value="O", inline=False)
        embed.add_field(name="생일", value="?", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="?", inline=False)
        embed.add_field(name="싫어하는 음식", value="?", inline=False)
        embed.add_field(name="출생지", value="?", inline=False)
        embed.add_field(name="소속", value="?", inline=False)
        embed.add_field(name="취미", value="?", inline=False)
        embed.add_field(name="국적", value="?", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="하늘색 머리를 지닌 장발\n왼쪽눈의 찔린듯한 상처가 있는걸로 보임\n밤하늘의 초계반에서만 출현", inline=False)
        embed.add_field(name="이명", value="에런 이즈라엘", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="B", inline=False)
        embed.add_field(name="열정", value="9", inline=False)
        embed.add_field(name="지능", value="10", inline=False)
        embed.add_field(name="협조성", value="1", inline=False)
        embed.add_field(name="행동력", value="10", inline=False)
        embed.add_field(name="외모", value="8", inline=False)
        embed.add_field(name="성격", value="3", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
       
    if message.content == f'{PREFIX}레안':
        embed = discord.Embed(name="레안", description="레안", color=0x971374)
        embed.add_field(name="성별", value="여자", inline=False)
        embed.add_field(name="나이", value="약 24세", inline=False)
        embed.add_field(name="키", value="168cm", inline=False)
        embed.add_field(name="몸무게", value="62kg", inline=False)
        embed.add_field(name="혈액형", value="O", inline=False)
        embed.add_field(name="생일", value="5월 29일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="우메가에 모찌(매화빵)", inline=False)
        embed.add_field(name="싫어하는 음식", value="매운음식", inline=False)
        embed.add_field(name="출생지", value="능력자도시 5구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="검도", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="분홍머리에 포니테일인 능력자학교의 교감이다\n소루 이상의 츤데레이다\n'매화'를 좋아하는걸 넘어 사랑한다\n술을 못마신다 마시면 취해버려 광란의 현장이 된다", inline=False)
        embed.add_field(name="이명", value="치와와", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="D+", inline=False)
        embed.add_field(name="열정", value="3", inline=False)
        embed.add_field(name="지능", value="6", inline=False)
        embed.add_field(name="협조성", value="7", inline=False)
        embed.add_field(name="행동력", value="2", inline=False)
        embed.add_field(name="외모", value="6", inline=False)
        embed.add_field(name="성격", value="2", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}사쿠라':
        embed = discord.Embed(name="사쿠라", description="사쿠라", color=0xffa8f9)
        embed.add_field(name="성별", value="여자", inline=False)
        embed.add_field(name="나이", value="약 24세", inline=False)
        embed.add_field(name="키", value="167cm", inline=False)
        embed.add_field(name="몸무게", value="59kg", inline=False)
        embed.add_field(name="혈액형", value="A", inline=False)
        embed.add_field(name="생일", value="7월 7일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="벚꽃떡", inline=False)
        embed.add_field(name="싫어하는 음식", value="에스프레소", inline=False)
        embed.add_field(name="출생지", value="능력자도시 9구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="맛집탐방", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 母 夫 女", inline=False)
        embed.add_field(name="특징", value="벚꽃색의 머리카락과 눈.. 심지어 이름마저도 벚꽃이라는 의미를 가지고 있다\n벚꽃 머리띠를 하고 다닌다\n'거유'이다(컵 사이즈 D)\n남편과 아이가 있다\n아줌마라는 소리를 듣는것을 싫어한다\n술을 잘마신다", inline=False)
        embed.add_field(name="이명", value="없음", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="A", inline=False)
        embed.add_field(name="열정", value="8", inline=False)
        embed.add_field(name="지능", value="9", inline=False)
        embed.add_field(name="협조성", value="9", inline=False)
        embed.add_field(name="행동력", value="7", inline=False)
        embed.add_field(name="외모", value="8", inline=False)
        embed.add_field(name="성격", value="9", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}델타':
        embed = discord.Embed(name="델타", description="델타", color=0x036334)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 27세", inline=False)
        embed.add_field(name="키", value="185cm", inline=False)
        embed.add_field(name="몸무게", value="72kg", inline=False)
        embed.add_field(name="혈액형", value="O", inline=False)
        embed.add_field(name="생일", value="11월 30일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="햄버거", inline=False)
        embed.add_field(name="싫어하는 음식", value="피망", inline=False)
        embed.add_field(name="출생지", value="능력자도시 12구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="영화보기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 母 妻", inline=False)
        embed.add_field(name="특징", value="능력자학교의 교감 중 최강의 교감이다\n가족관계에서는 부인(처)로 표현되었지만 약혼녀이다\n짙은 초록색의 눈과 머리를 가지고 있다\n눈치가 상당히 빠른 편이다 작중 레안과 미나토의 싸움을 중재시키기도 한다", inline=False)
        embed.add_field(name="이명", value="초신성", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C", inline=False)
        embed.add_field(name="열정", value="5", inline=False)
        embed.add_field(name="지능", value="7", inline=False)
        embed.add_field(name="협조성", value="6", inline=False)
        embed.add_field(name="행동력", value="3", inline=False)
        embed.add_field(name="외모", value="7", inline=False)
        embed.add_field(name="성격", value="5", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)

    if message.content == f'{PREFIX}널':
        embed = discord.Embed(name="널", description="널", color=0x000000)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 16세", inline=False)
        embed.add_field(name="키", value="182cm", inline=False)
        embed.add_field(name="몸무게", value="71kg", inline=False)
        embed.add_field(name="혈액형", value="A", inline=False)
        embed.add_field(name="생일", value="3월 5일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="레몬", inline=False)
        embed.add_field(name="싫어하는 음식", value="파프리카", inline=False)
        embed.add_field(name="출생지", value="능력자도시 4구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="사격", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 母", inline=False)
        embed.add_field(name="특징", value="검은색 머리를 가진 학생으로 키가 크다\n팔에 팔찌를 위장한 보구를 끼고있다\nfps게임을 잘한다", inline=False)
        embed.add_field(name="이명", value="C반의 버스기사", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="D+", inline=False)
        embed.add_field(name="열정", value="6", inline=False)
        embed.add_field(name="지능", value="5", inline=False)
        embed.add_field(name="협조성", value="5", inline=False)
        embed.add_field(name="행동력", value="4", inline=False)
        embed.add_field(name="외모", value="4", inline=False)
        embed.add_field(name="성격", value="3", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}터드':
        embed = discord.Embed(name="터드", description="터드", color=0xff0000)
        embed.add_field(name="성별", value="남자", inline=False)
        embed.add_field(name="나이", value="약 21세", inline=False)
        embed.add_field(name="키", value="185cm", inline=False)
        embed.add_field(name="몸무게", value="81kg", inline=False)
        embed.add_field(name="혈액형", value="A", inline=False)
        embed.add_field(name="생일", value="5월 15일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="홍차", inline=False)
        embed.add_field(name="싫어하는 음식", value="가지", inline=False)
        embed.add_field(name="출생지", value="능력자도시 11구역", inline=False)
        embed.add_field(name="소속", value="능력자학교 직속 마도구", inline=False)
        embed.add_field(name="취미", value="마도구 손질", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="父 母", inline=False)
        embed.add_field(name="특징", value="능력자학교의 졸업생이다\n항상 목에 붉은 목도리를 매고 다닌다\n생각보다 근육이 많다", inline=False)
        embed.add_field(name="이명", value="나이트 오브 아너", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="B+", inline=False)
        embed.add_field(name="열정", value="8", inline=False)
        embed.add_field(name="지능", value="6", inline=False)
        embed.add_field(name="협조성", value="9", inline=False)
        embed.add_field(name="행동력", value="7", inline=False)
        embed.add_field(name="외모", value="8", inline=False)
        embed.add_field(name="성격", value="9", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content == f'{PREFIX}디베나':
        embed = discord.Embed(name="디베나", description="디베나", color=0x30a36d)
        embed.add_field(name="성별", value="여자", inline=False)
        embed.add_field(name="나이", value="약 25세", inline=False)
        embed.add_field(name="키", value="167cm", inline=False)
        embed.add_field(name="몸무게", value="51kg", inline=False)
        embed.add_field(name="혈액형", value="AB", inline=False)
        embed.add_field(name="생일", value="8월 3일", inline=False)
        embed.add_field(name="종족", value="능력자", inline=False)
        embed.add_field(name="좋아하는 음식", value="빵", inline=False)
        embed.add_field(name="싫어하는 음식", value="건포도", inline=False)
        embed.add_field(name="출생지", value="능력자도시 9구역", inline=False)
        embed.add_field(name="소속", value="능력자학교", inline=False)
        embed.add_field(name="취미", value="일기쓰기", inline=False)
        embed.add_field(name="국적", value="능력자도시", inline=False)
        embed.add_field(name="가족관계", value="?", inline=False)
        embed.add_field(name="특징", value="몸이 아담하다 평범한 남자라면 한 팔로 끌어안을수 있을 정도\n의사 가운을 입고 있는데 전에 입원했던 병원에서 의도치 않게 가져왔다고 한다\n묶은 머리때문에 머리가 짧아 보이지만 머리가 매우 길다고 한다", inline=False)
        embed.add_field(name="이명", value="학생부장", inline=False)
        embed.add_field(name="능력치", value="", inline=False)
        embed.add_field(name="평가", value="C+", inline=False)
        embed.add_field(name="열정", value="6", inline=False)
        embed.add_field(name="지능", value="8", inline=False)
        embed.add_field(name="협조성", value="5", inline=False)
        embed.add_field(name="행동력", value="7", inline=False)
        embed.add_field(name="외모", value="9", inline=False)
        embed.add_field(name="성격", value="3", inline=False)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        
    if message.content.startswith(f'{PREFIX}정샌찬'):
        await message.channel.send('https://cdn.discordapp.com/attachments/969220566567489566/1078932702255923260/Sanmas.gif')
        
@client.event
async def on_reaction_add():
    if reaction.emoji == "❌":
        await reaction.channel.message.delete()
        
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
