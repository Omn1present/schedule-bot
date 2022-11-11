# coding=windows-1251

import datetime
import pandas as pd
def find_schedule():
    df1 = pd.read_html(r'E:\schedule\PZPI.html', encoding='windows-1251')
    df=df1[1]


    start=datetime.date(2022,8,29)
    day = datetime.date.today() 

    target = day.strftime('%d.%m.%Y')
    area = df[((day-start).days)//7+2]
    print(area,target)
    schedule={1:'7:45-9:20', 2:'9:30-11:05', 3:'11:15-12:50', 4:'13:10-14:45'}

    for i in range(len(area)):
        if area[i]==target:
            for j in range(i+1,i+5):
                schedule[area[j]] = schedule.pop(j-1)
    
    return '\n'.join(map(str,schedule.items())) 

