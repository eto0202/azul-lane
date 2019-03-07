import os
import subprocess
from discord.ext import commands
import discord
import requests
import time
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import urllib.parse
from datetime import datetime
import json
import bs4
import re
import unicodedata

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('ログインしました')



@client.command()
async def kansen(self, ctx):
    mess = urllib.parse.quote(ctx, encoding='euc-jp')
    res = requests.get("http://azurlane.wikiru.jp/index.php?" + mess)
    time.sleep(1)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    search_data = soup.find('div', id='body')
    find_th = search_data.find("th").getText()
    find_data = search_data.find_all(["td"])
    del find_data[80:]
    list_jp = []
    for data_jp in find_data[0:]:
        list_jp.append(data_jp.getText())
    list_in = [s for s in list_jp if '補正' in s]
    list_in2 = [s for s in list_jp if '設備' in s]
    del list_jp[list_jp.index(list_in[0]):]
    index_del = int(list_jp.index(list_in2[0])) + 8
    del list_jp[37:index_del]
    list_jp.append(unicodedata.normalize('NFKC', list_jp[-1]))
    del list_jp[-2]
    embed = discord.Embed(title= list_jp[1],
        description= '**図鑑番号**：'+ find_th +'\n'+
        '**レアリティ**：'+ list_jp[2] +'\n'+
        '**艦種**：'+ list_jp[3] +'\n'+
        '**陣営**：'+ list_jp[4] +'\n'+
        '**建造時間**：'+ list_jp[5] +'\n'+
        '**CV**： '+ list_jp[6] +'\n'+
        '**イラスト**：'+ list_jp[7] +'\n\n',
        colour=0x546e7a
        )

    filed_1 ='**耐久**：'+ list_jp[8] +'\n'+ \
             '**火力**：'+ list_jp[9] +'\n'+ \
             '**雷装**：'+ list_jp[10] +'\n'+ \
             '**回避**：'+ list_jp[11] +'\n'+ \
             '**対空**：'+ list_jp[12] +'\n'+ \
             '**航空**：'+ list_jp[13] +'\n'+ \
             '**速力**：'+ list_jp[14] +'\n\n'

    filed_2 =list_jp[16]

    filed_3 =list_jp[17] +'\n\n'

    filed_4 ='**耐久**：'+ list_jp[18] +'/'+ list_jp[19] +'\n'+ \
             '**装甲**：'+ list_jp[20] +'\n'+ \
             '**装填**：'+ list_jp[21] +'/'+ list_jp[22] +'\n'+ \
             '**火力**：'+ list_jp[23] +'/'+ list_jp[24] +'\n'+ \
             '**雷装**：'+ list_jp[25] +'/'+ list_jp[26] +'\n'+ \
             '**回避**：'+ list_jp[27] +'/'+ list_jp[28] +'\n'+ \
             '**対空**：'+ list_jp[29] +'/'+ list_jp[30] +'\n'+ \
             '**航空**：'+ list_jp[31] +'/'+ list_jp[32] +'\n'+ \
             '**消費**：'+ list_jp[33] +'/'+ list_jp[34] +'\n'+ \
             '**対潜**：'+ list_jp[35] +'/'+ list_jp[36] +'\n\n'

    filed_5 ='http://azurlane.wikiru.jp/index.php?' + mess

    tt = []
    tt = [filed_1, filed_2, filed_3, filed_4, filed_5]

    if len(list_jp) == 40:
        filed_6 ='**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n'
        tt.append(filed_6)

    elif len(list_jp) == 43:
        filed_6 ='**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n\n'+ \
                 '**『'+ list_jp[41] +'』**'+'\n'+ list_jp[42] +'\n'
        tt.append(filed_6)

    elif len(list_jp) == 46:
        filed_6 ='**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n\n'+ \
                 '**『'+ list_jp[41] +'』**'+'\n'+ list_jp[42] +'\n\n'+ \
                 '**『'+ list_jp[44] +'』**'+'\n'+ list_jp[45] +'\n'
        tt.append(filed_6)

    elif len(list_jp) == 49:
        filed_6 ='**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n\n'+ \
                 '**『'+ list_jp[41] +'』**'+'\n'+ list_jp[42] +'\n\n'+ \
                 '**『'+ list_jp[44] +'』**'+'\n'+ list_jp[45] +'\n\n'+ \
                 '**『'+ list_jp[47] +'』**'+'\n'+ list_jp[48] +'\n'
        tt.append(filed_6)

    elif len(list_jp) == 52:
        filed_6 ='**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n\n'+ \
                 '**『'+ list_jp[41] +'』**'+'\n'+ list_jp[42] +'\n\n'+ \
                 '**『'+ list_jp[44] +'』**'+'\n'+ list_jp[45] +'\n\n'+ \
                 '**『'+ list_jp[47] +'』**'+'\n'+ list_jp[48] +'\n\n'+ \
                 '**『'+ list_jp[50] +'』**'+'\n'+ list_jp[51] +'\n'
        tt.append(filed_6)

    table = str.maketrans({'%':''})
    result = mess.translate(table)
    embed.set_image(url= "http://azurlane.wikiru.jp/attach2/" + result + '_' + result +'2E6A7067.jpg')
    embed.set_thumbnail(url="http://azurlane.wikiru.jp/attach2/" + result + '_' + result +'2E676966.gif')

    embed.add_field(name= '**・ステータス**', value= tt[0], inline= False)
    embed.add_field(name= '**・自己紹介**', value= tt[1], inline= False)
    embed.add_field(name= '**・入手方法**', value= tt[2], inline= False)
    embed.add_field(name= '**・ステータス(1Lv/100Lv)**', value= tt[3], inline= False)
    embed.add_field(name= '**・スキル**', value= tt[5], inline= False)
    embed.add_field(name= '**・URL**', value= tt[4], inline= False)

    await self.send(embed=embed)


@client.command()
async def nowevent(ctx):
    res = requests.get("http://azurlane.wikiru.jp/index.php?%A5%A4%A5%D9%A5%F3%A5%C8%B0%EC%CD%F7")
    time.sleep(1)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    search = soup.find('div', id='body')
    ul = search.find_all('ul')
    list_jp = []
    for data_jp in ul[0:]:
        list_jp.append(data_jp.getText())
    split_list = list_jp[0].splitlines()
    time_list = []
    for split_list2 in split_list[0:]:
        time_data = re.findall(r'[0-9]{4}.*テ', split_list2)
        time_list.extend(time_data)
    print(time_list)
    event_name = []
    for x in split_list:
            x_sub = re.sub(r'[0-9]{4}.*テ', '', x)
            x_sub = x_sub[:-2]
            event_name.append(x_sub)
    print(event_name)
    url = search.select('ul a')
    url_list = []
    for url_sourse in url:
        url_list.append(url_sourse.get('href'))
    print(url_list)
    msg_sourse = []
    for a, b, c in zip(event_name[0:], time_list[0:], url_list[0:]):
        format_date = '\n**『{}』**\n・{}\n{}\n'.format(a, b, c)
        msg_sourse.append(format_date)
    main_data = ''.join(map(str, msg_sourse))
    print(main_data)
    msg = discord.Embed(title= '現在開催中のイベント',
        description= main_data,
        colour=0x546e7a
    )
    await ctx.send(embed= msg)

client.remove_command('help')
@client.command()
async def help(ctx):
    embed = discord.Embed(title='アズレン Wiki bot', description='アズレンWikiの情報をまとめたBotです。\nhttp://azurlane.wikiru.jp/\n※現在開発中')
    embed.add_field(name='!kansen キャラ名(正式名称)', value='キャラクター検索ができます。', inline= False)
    embed.add_field(name='!nowevent', value='現在開催中のイベントを参照できます。',inline= False)
    await ctx.send(embed=embed)

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
client.run(DISCORD_TOKEN)