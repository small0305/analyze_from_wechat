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
    
    daily_forecast = w['daily_forecast'][0]
    AQI = w['aqi']['city']
    now = w['now']
    suggestion = w['suggestion']

    
    s =city+"天气\n"+\
    "白天："+daily_forecast['cond']['txt_d']+" 夜间："+daily_forecast['cond']['txt_n']+"\n"+\
    "温度："+daily_forecast['tmp']['min']+"℃~"+daily_forecast['tmp']['max']+"℃\n"+\
    "空气质量："+AQI['qlty']+'('+AQI['aqi']+')\n'+\
    '舒适度指数：'+suggestion['comf']['brf']+'。'+suggestion['comf']['txt']+'\n'+\
    '穿衣指数：'+suggestion['drsg']['brf']+'。'+suggestion['drsg']['txt']+'\n'+\
    '感冒指数：'+suggestion['flu']['brf']+'。'+suggestion['flu']['txt']+'\n'+\
    '运动指数：'+suggestion['sport']['brf']+'。'+suggestion['sport']['txt']+'\n'+\
    '紫外线指数：'+suggestion['uv']['brf']+'。'+suggestion['uv']['txt']+'\n'+\
    '旅游指数：'+suggestion['trav']['brf']+'。'+suggestion['trav']['txt']+'\n'+\
    '当前天气：\n'+\
    '相对湿度：'+now['hum']+'%\n'+\
    '温度：'+now['tmp']+'℃\n'+\
    '体感温度：'+now['fl']+'℃\n'
    
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


