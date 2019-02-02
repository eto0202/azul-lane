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

desc='''このボットは開発途中です！
        「!kansen キャラ名」でキャラ情報参照
        「!nowevent」で現在開催中のイベントを表示 '''

client = commands.Bot(command_prefix='!',description=desc)


@client.event
async def on_ready():
    print('ログインしました')



@client.command()
async def kansen(ctx):
    mess = urllib.parse.quote(ctx, encoding= 'euc-jp')
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
    msg1 = discord.Embed(title= list_jp[1],
        description= '**図鑑番号**：'+ find_th +'\n'+
        '**レアリティ**：'+ list_jp[2] +'\n'+
        '**艦種**：'+ list_jp[3] +'\n'+
        '**陣営**：'+ list_jp[4] +'\n'+
        '**建造時間**：'+ list_jp[5] +'\n'+
        '**CV**： '+ list_jp[6] +'\n'+
        '**イラスト**：'+ list_jp[7] +'\n\n',
        colour=0x546e7a
        )
    msg2 = discord.Embed(description=
        '**耐久**：'+ list_jp[8] +'\n'+
        '**火力**：'+ list_jp[9] +'\n'+
        '**雷装**：'+ list_jp[10] +'\n'+
        '**回避**：'+ list_jp[11] +'\n'+
        '**対空**：'+ list_jp[12] +'\n'+
        '**航空**：'+ list_jp[13] +'\n'+
        '**速力**：'+ list_jp[14] +'\n\n',
        colour=0x546e7a
        )
    msg3 = discord.Embed(description=
        '**【自己紹介】**'+'\n'+ list_jp[16] +'\n\n'+
        '**【入手方法】**'+'\n'+ list_jp[17] +'\n\n',
        colour=0x546e7a
        )
    msg4 = discord.Embed(description=
        '**『ステータス(1Lv/100lv)』**'+'\n'+
        '**耐久**：'+ list_jp[18] +'/'+ list_jp[19] +'\n'+
        '**装甲**：'+ list_jp[20] +'\n'+
        '**装填**：'+ list_jp[21] +'/'+ list_jp[22] +'\n'+
        '**火力**：'+ list_jp[23] +'/'+ list_jp[24] +'\n'+
        '**雷装**：'+ list_jp[25] +'/'+ list_jp[26] +'\n'+
        '**回避**：'+ list_jp[27] +'/'+ list_jp[28] +'\n'+
        '**対空**：'+ list_jp[29] +'/'+ list_jp[30] +'\n'+
        '**航空**：'+ list_jp[31] +'/'+ list_jp[32] +'\n'+
        '**消費**：'+ list_jp[33] +'/'+ list_jp[34] +'\n'+
        '**対潜**：'+ list_jp[35] +'/'+ list_jp[36] +'\n\n',
        colour=0x546e7a
        )
    tt = []
    table = str.maketrans({'%':''})
    result = mess.translate(table)
    p = "http://azurlane.wikiru.jp/attach2/" + result + '_' + result +'2E6A7067.jpg'
    pp = "http://azurlane.wikiru.jp/attach2/" + result + '_' + result +'C1B4BFC82E6A7067.jpg'
    msg1.set_image(url= p)
    msg2.set_image(url=pp)
    tt = [msg1, msg2, msg3, msg4]
    if len(list_jp) == 40:
        msg5 = discord.Embed(description=
        '**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n'+
        'http://azurlane.wikiru.jp/index.php?' + mess,
        colour=0x546e7a
        )
        tt.append(msg5)
    elif len(list_jp) == 43:
        msg6 = discord.Embed(description=
        '**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n\n'+
        '**『'+ list_jp[41] +'』**'+'\n'+ list_jp[42] +'\n'+
        'http://azurlane.wikiru.jp/index.php?' + mess,
        colour=0x546e7a
        )
        tt.append(msg6)
    elif len(list_jp) == 46:
        msg7 = discord.Embed(description=
        '**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n\n'+
        '**『'+ list_jp[41] +'』**'+'\n'+ list_jp[42] +'\n\n'+
        '**『'+ list_jp[44] +'』**'+'\n'+ list_jp[45] +'\n'+
        'http://azurlane.wikiru.jp/index.php?' + mess,
        colour=0x546e7a
        )
        tt.append(msg7)
    elif len(list_jp) == 49:
        msg8 = discord.Embed(description=
        '**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n\n'+
        '**『'+ list_jp[41] +'』**'+'\n'+ list_jp[42] +'\n\n'+
        '**『'+ list_jp[44] +'』**'+'\n'+ list_jp[45] +'\n\n'+
        '**『'+ list_jp[47] +'』**'+'\n'+ list_jp[48] +'\n'+
        'http://azurlane.wikiru.jp/index.php?' + mess,
        colour=0x546e7a
        )
        tt.append(msg8)
    elif len(list_jp) == 52:
        msg9 = discord.Embed(description=
        '**『'+ list_jp[38] +'』**'+'\n'+ list_jp[39] +'\n\n'+
        '**『'+ list_jp[41] +'』**'+'\n'+ list_jp[42] +'\n\n'+
        '**『'+ list_jp[44] +'』**'+'\n'+ list_jp[45] +'\n\n'+
        '**『'+ list_jp[47] +'』**'+'\n'+ list_jp[48] +'\n\n'+
        '**『'+ list_jp[50] +'』**'+'\n'+ list_jp[51] +'\n'+
        'http://azurlane.wikiru.jp/index.php?' + mess,
        colour=0x546e7a
        )
        tt.append(msg9)
    mes = await client.say(embed=tt[0])
    await client.add_reaction(mes, '◀')
    await client.add_reaction(mes, '▶')
    while True:
            target_reaction = await client.wait_for_reaction(message=mes)
            if target_reaction.user != mes.author:
                    if target_reaction.reaction.emoji =='◀':
                            tt.insert(0, tt[-1])
                            del tt[-1]
                            await client.edit_message(mes, embed=tt[0])
                    elif target_reaction.reaction.emoji =='▶':
                            await client.edit_message(mes, embed=tt[0])
                            tt.append(tt[0])
                            del tt[0]
                    else:
                            pass
                    await client.remove_reaction(mes, \
                    target_reaction.reaction.emoji, target_reaction.user)

@client.command()
async def nowevent():
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
        time_data = re.findall(r'[0-9]{4}.*で', split_list2)
        time_list.append(time_data[0])
    print(time_list)
    event_name = []
    for x in split_list:
            x_sub = re.sub(r'\([0-9]{4}.*で\)', '', x)
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
    await client.say(embed= msg)

print(os.environ.get('DISCORD_TOKEN'))
