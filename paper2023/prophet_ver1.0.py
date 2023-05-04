# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 12:56:05 2023

@author: Spark
"""

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import os

path = './Paper2023/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.xlsx')]

df = pd.DataFrame()
for i in file_list_py:
    data = pd.read_excel(path + i, parse_dates=['Date'])
    df = pd.concat([df,data])
    
df = df.reset_index(drop = True)

jamsil=df[df['st_name']=='잠실역']
jamsil_1=jamsil[['Date', 'total']]

gangnam=df[df['st_name']=='강남역']
ex_ter=df[df['st_name']=='고속터미널역']
seoul_st=df[df['st_name']=='서울역역']
hongdae=df[df['st_name']=='홍대입구역']
suneung=df[df['st_name']=='선릉역']
sinlim=df[df['st_name']=='신림역']
gasan=df[df['st_name']=='가산디지털단지역']
sadang=df[df['st_name']=='사당역']
guro_dig=df[df['st_name']=='구로디지털단지역']