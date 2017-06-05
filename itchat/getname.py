# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:00:59 2017

@author: My
"""
from getpixiv import *
import itchat
from itchat import *
from itchat.content import *
from getweather import *
from textanalyze import *
from secret import *
from reply import *

#msgs = []
def log_in():
    itchat.auto_login(hotReload = True)

def get_username(NAME):
    name_dict = itchat.search_friends(name = NAME)
    return name_dict[0]['UserName']

def get_chatroom(NAME):
    name_dict = itchat.search_chatrooms(name = NAME)
    return name_dict[0]['UserName']

@itchat.msg_register(TEXT,isFriendChat=True, isGroupChat=False)
def text_reply(msg):
    reply_text = reply(msg.text)
    if reply_text and msg['ToUserName']!=msg['User']['UserName']:
        msg.user.send(reply_text)
    if msg.text=="P":
        sendpixiv(msg,username,password)
        return
    if 'cloud' in msg.text:
        print('drawing')
        print(len(msgs))
        text_analyze(msg,msgs)
        msg.user.send('@img@%s' % 'cloud.jpg')
        return
    if '天气' in msg.text:
        city = msg.text.split('天气')[0]        
        if city == '':
            s = get_weather('上海')
        else:
            try:
                s = get_weather(city)
                msg.user.send(s)
            except KeyError:
                print('invalid input')
        return
    msgs.append(msg)

log_in()

itchat.send_msg(msg = 'Test')

itchat.run()

