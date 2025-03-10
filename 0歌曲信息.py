import requests,openpyxl,time

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='song_info'
sheet['A1']='曲目'
sheet['B1']='专辑'
sheet['C1']='时长'
sheet['D1']='链接'
song_info_list=[]

songnumber=int(input('请输入要爬取的页数（每页最多60首）'))
writer=str(input('请输入要爬取的歌手'))

for i in range(1,songnumber+1):

    url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'


    headers={
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
        }

    

    params={
    '﻿ct':'24',
    'qqmusic_ver':'1298',
    'new_json':'1',
    'remoteplace':'txt.yqq.top',
    'searchid':'66796594183405799',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(i),
    'n':'99',
    'w':writer,
    '_':'1631883628777',
    'cv':'4747474',
    'ct':'24',
    'format':'json',
    'inCharset':'utf-8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0',
    'uin':'0',
    'g_tk_new_20200303':'5381',
    'g_tk':'5381',
    'hostUin':'0',
    'loginUin':'0'
    }

    res=requests.get(url,headers=headers,params=params)


    dict_info=res.json()

    print(type(dict_info))
    

    info_list=dict_info['data']['song']['list']


    for item in info_list:
        name=item['name']
        album=item['album']['name']
        seconds=item['interval']
        time_formal=str(int(seconds/60))+'分'+str(seconds%60)+'秒'
        url='https://y.qq.com/n/ryqq/songDetail/'+item['mid']
        row=[name,album,time_formal,url]
        song_info_list.append(row)

for r in song_info_list:
        sheet.append(r)


time=time.asctime(time.localtime(time.time()))
sheet.append([time])
wb.save('%s.xlsx'%(writer))


    
