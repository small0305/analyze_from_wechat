# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:23:51 2017

@author: My
"""
import jieba
from jieba import analyse
from os import path
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import re


def get_keywords_from_text(text, n=200):
    '''
    Given the text and number of keywords we need, returns the frequences list.
    The frequences is like:
            [('喵',0.1),('兔子',0.05),...]
    '''
    key_words = jieba.analyse.extract_tags(text, topK=n, withWeight=True, allowPOS=())
#        'nb', 'n', 'nr', 'ns', 'a', 'ad', 'an', 'nt', 'nz', 'v', 'd'))
    frequences = []
    for word, fre in key_words:
        frequences.append((word, fre))
    return frequences

def draw_pic_with_frequences(frequences, pic_path, maxfontsize=800, fontpath='MSYH.TTC'):
    '''
    Given frequences list and mask image path, plot the image of word cloud.
    '''
    d = path.dirname(__file__)
    mask_pic = np.array(Image.open(path.join(d, pic_path)))
    wc = WordCloud(background_color="white", mask=mask_pic,
                   max_font_size=maxfontsize, random_state=21, font_path=fontpath)
    wc.fit_words(frequences)
    image_colors = ImageColorGenerator(mask_pic)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.savefig('cloud.jpg',bbox_inches='tight',pad_inches=0,dpi = 300)

def text_analyze(msg_now,msgs):
    user_now = msg_now['User']
    nickname = user_now['NickName']
        
    user_now = msg_now['ToUserName']
    text = ''
    for msg in msgs:
        if msg['User']['NickName']==nickname:
            t_now = msg['Text']
            t_now = re.sub('\d','',t_now)
            t_now = re.sub('cloud','',t_now)
            if 'http' not in t_now and len(t_now)<300:
                text+=t_now+' '

            
    print(text)
    pic_path = 'test.jpg'
    freq = dict(get_keywords_from_text(text))
    freq['cloud'] = 0
    draw_pic_with_frequences(freq, pic_path)


