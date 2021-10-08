#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:10:15 2021

@author: adityan_manick
"""

import pandas as pd
from datetime import datetime
import sqlalchemy
from calendar import monthrange

name='root' 
password=''
database_name='ETL'

engine=sqlalchemy.create_engine('mysql+pymysql://'+name+':'+password+'@localhost:3306/'+database_name)

holi_df = pd.read_sql('select * from holiday',engine)
type_df = pd.read_sql('select * from shift_types',engine)

mon_yr = input('Enter the month and year (mon_year) :')
mon_yr = mon_yr.split('_')
month = datetime.strptime(mon_yr[0],'%b').month

dates = []
for d in range(1,monthrange(int(mon_yr[1]),month)[1]+1):
    temp_date = datetime.strptime(mon_yr[1]+'-'+str(month)+'-'+str(d), '%Y-%m-%d').date()
    dates.append(temp_date)


for i in dates:
    if i in holi_df['date'].values:
        pass
    else:
        if i.strftime('%A') == 'Sunday':
            pass
        elif i.strftime('%A') == 'Saturday':
            sat_df = pd.DataFrame({'shift_id' : 0,'date':i,'start_time':type_df.iloc[0][1],'end_time':type_df.iloc[0][2]},
                                  columns = ['shift_id','date','start_time','end_time'], index =[0])
            sat_df.to_sql(name = 'shifts', con = engine, if_exists = 'append', index = False)
        else:
            mor_df = pd.DataFrame({'shift_id' : 0,'date':i,'start_time':type_df.iloc[0][1],'end_time':type_df.iloc[0][2]}, 
                                  columns = ['shift_id','date','start_time','end_time'], index =[0])
            mor_df.to_sql(name = 'shifts', con = engine, if_exists = 'append', index = False)
            eve_df = pd.DataFrame({'shift_id' : 0,'date':i,'start_time':type_df.iloc[1][1],'end_time':type_df.iloc[1][2]}, 
                                  columns = ['shift_id','date','start_time','end_time'], index =[0])
            eve_df.to_sql(name = 'shifts', con = engine, if_exists = 'append', index = False)
