# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:48:23 2017

@author: My
"""

from getpixiv import *
import datetime
import os,os.path

def sendpixiv(msg):
    today = datetime.date.today().strftime("%Y-%m-%d")
    if(os.path.exists(today)):
        print("exists")
    else:
        os.mkdir(today)
    
    p = log_in(yourusername,yourpassword)
    pic_IDs = get_pic_IDs(p)
    for ID in pic_IDs[1:10]:
        pic_path = save_pics(today,ID,p)
        if os.path.exists(pic_path):
#            msg.user.send("https://www.pixiv.net/member_illust.php?mode=medium&illust_id="+ID)
            msg.user.send('@img@%s' % pic_path)
    
    
    