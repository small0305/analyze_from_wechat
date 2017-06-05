# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:00:59 2017

@author: My
"""
from savepixiv import *
import itchat
from itchat import *
from itchat.content import *
from getweather import *
from textanalyze import *
import pickle
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
    msgs.append(msg)
#    if(msg.user.NickName=="滕岩松"):
#        msg.user.send("么么哒")
    if msg.text=="P":
        print("PPP")
#        pic_path = '2017-06-01\\63134559.jpg'
#        msg.user.send('@img@%s' % pic_path)
#        itchat.send_img(pic_path, toUserName=msg.FromUserName)
        sendpixiv(msg)
    if '啪' in msg.text:
        #msg.user.send('[捂脸]')
        msg.user.send( msg.text.count('啪')*'[捂脸]')
#    if '棒棒' in msg.text:
#        msg.user.send('儿童节快乐')
    if 'cloud' in msg.text:
        print('drawing')
        print(len(msgs))
        text_analyze(msg,msgs)
        msg.user.send('@img@%s' % 'cloud.jpg')
    if '天气' in msg.text:
        city = msg.text.split('天气')[0]
        
        if city == '':
            s = get_weather()
        else:
            try:
                s = get_weather(city)
                msg.user.send(s)
            except KeyError:
                print('invalid input')

def save_data():
    f = open('msgs','wb')
    pickle.dump(msgs,f)
    f.close()

def load_data():
    f = open('msgs','rb')
    msgs = pickle.load(f)
    f.close()
#        msg.user.send('@img@%s' % 'test.jpg')
#==============================================================================
#     return ('%s: %s' % (msg.type, msg.text))
#==============================================================================

#==============================================================================
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)
#==============================================================================

#==============================================================================
# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')
#==============================================================================

#==============================================================================
# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg.isAt:
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))
#==============================================================================
log_in()
dear_name = get_username("滕岩松")
my_name = get_username("small")
family_name = get_chatroom("family")

itchat.send_msg(msg = 'Test',toUserName=my_name)

itchat.run()

