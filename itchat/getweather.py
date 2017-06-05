# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:50:17 2017

@author: My
"""
import requests

key = 'd12b7f563330403da53a46d517bbb1a4'


def get_weather(city='上海'):
    url = 'https://free-api.heweather.com/v5/weather?city='+city+'&key='+key
    w = requests.get(url).json()['HeWeather5'][0]
    
    
    weather_d = w['daily_forecast'][0]['cond']['txt_d']
    weather_n = w['daily_forecast'][0]['cond']['txt_n']
    max_tmp = w['daily_forecast'][0]['tmp']['max']
    min_tmp = w['daily_forecast'][0]['tmp']['min']
    AQI = w['aqi']['city']['aqi']
    pollution = w['aqi']['city']['qlty']
    
    hum = w['now']['hum']
    tmp = w['now']['tmp']
    fl = w['now']['fl']
    
    s =city+"天气\n"+\
        "白天："+weather_d+" 夜间："+weather_n+"\n"+\
    "温度："+min_tmp+"℃~"+max_tmp+"℃\n"+\
    "空气质量："+pollution+'('+AQI+')\n'+\
    '舒适度指数：'+w['suggestion']['comf']['brf']+'。'+w['suggestion']['comf']['txt']+'\n'+\
    '穿衣指数：'+w['suggestion']['drsg']['brf']+'。'+w['suggestion']['drsg']['txt']+'\n'+\
    '感冒指数：'+w['suggestion']['flu']['brf']+'。'+w['suggestion']['flu']['txt']+'\n'+\
    '运动指数：'+w['suggestion']['sport']['brf']+'。'+w['suggestion']['sport']['txt']+'\n'+\
    '紫外线指数：'+w['suggestion']['uv']['brf']+'。'+w['suggestion']['uv']['txt']+'\n'+\
    '旅游指数：'+w['suggestion']['trav']['brf']+'。'+w['suggestion']['trav']['txt']+'\n'+\
    '当前天气：\n'+\
    '相对湿度：'+hum+'%\n'+\
    '温度：'+tmp+'℃\n'+\
    '体感温度：'+fl+'℃\n'
    
    hours = w['hourly_forecast']
    try:
        if '雨' in hours[0]['cond']['txt']:
            s += '未来1小时可能有雨。'
        else:
            if '雨' in hours[1]['cond']['txt'] or '雨' in hours[2]['cond']['txt']:
                s+='未来3小时可能有雨。'
    except IndexError:
        print('what happened')
    
    return s


