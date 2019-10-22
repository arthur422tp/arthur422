#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random as rd
from numpy.random import sample,choice
from numpy.random import randint
春天=['竹外桃花三兩枝','春風又綠江南岸','紅杏枝頭春意鬧','萬紫千紅總是春','吹面不寒楊柳風','深鎖春光一院愁','碧玉妝成一樹高','二月春風似剪刀','草色遙看近卻無','春色滿園關不住','風前欲勸春光住','誰家新燕啄春泥','千里鶯啼綠映江','春江水暖鴨先知','春江潮水連海平','何處春江無月明','江流宛轉繞芳甸','昨夜閒潭夢落花']
夏天=['謝卻海棠飛盡絮','晴日暖風生麥氣','綠陰幽草勝花時','槐柳陰中野徑斜','綠槐高柳咽新蟬','布穀聲中夏令新','四月清和雨乍晴','夏鶯千囀弄薔薇','點溪荷葉疊青錢','稻花香里說豐年','黃梅時節家家雨','長夏江村事事幽','石榴開遍透簾明','梅子金黃杏子肥']
秋天=['臥看牽牛織女星','洛陽城裡見秋風','秋叢繞舍似陶家','萬里悲秋常作客','銀燭秋光冷畫屏','停車坐愛楓林晚','秋風蕭瑟天氣涼','卻道天涼好個秋','自古逢秋悲寂寥','湖光秋月兩相和','花自飄零水自流','金井梧桐秋葉黃','角聲滿天秋色里','峨眉山月半輪秋','辭根散作九秋蓬','荷葉枯時秋恨成','八月秋高風怒號']
冬天=['月明直見嵩山雪','北風捲地白草折','寒氣先侵玉女扉','可憐冬景似春華','歲雲暮矣多北風','瀟湘洞庭白雪中','天涯霜雪霽寒宵','柳絮章臺街裏飛','日暮詩成天又雪','胡天八月即飛雪','檐流未滴梅花凍','有雪無詩俗了人','輕於柳絮重於霜']
user=input('喜歡什麼季節的詩歌呢?')
if user=='春天':
    n=randint(2,3)
    for i in range(n):
        o=randint(2,3)
        egg=choice(春天,n)
        ppp=' '.join(egg)
        print(ppp)
if user=='夏天':
    n2=randint(2,3)
    for j in range(n2):
        o2=randint(2,3)
        egg2=choice(夏天,n2)
        ppp2=' '.join(egg2)
        print(ppp2)
if user=='秋天':
    n3=randint(2,3)
    for l in range(n3):
        o3=randint(2,3)
        egg3=choice(秋天,n3)
        ppp3=' '.join(egg3)
        print(ppp3)
if user=='冬天':
    n4=randint(2,3)
    for h in range(n4):
        o4=randint(2,3)
        egg4=choice(冬天,n4)
        ppp4=' '.join(egg4)
        print(ppp4)


# In[ ]:




