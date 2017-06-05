# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:20:34 2017

@author: My
"""

import re   
import requests

def log_in(username,password):
    data = {
        'pixiv_id':username,
        'password':password,
        'post_key':'cf55eead2f99c3449f5568a5123ef75f',
        'source':'pc',
        'ref':'wwwtop_accounts_index',
        'return_to':'https://www.pixiv.net/'
    }
    header = {
              'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    params = {
        'lang':'zh',
        'source':'pc',
        'view_type':'page',
        'ref':'wwwtop_accounts_index'
    }
    login_url = 'https://accounts.pixiv.net/api/login?lang=zh'
    p = requests.Session()
    p.headers = header
    r = p.get(url= 'https://accounts.pixiv.net/login',params = params)
    print("finding post_key")
    post_key = re.findall('name="post_key"\svalue="(.*?)"',r.text,re.S)
    data['post_key'] = post_key[0]
    print("logging in")
    p.post(url = login_url, data=data)
    print("logged in")
    return p



def get_pic_IDs(p):    
    response = p.get(url='https://www.pixiv.net/ranking.php?mode=daily')
    print("getting pic IDs")
    page = response.text    
    pic_IDs = re.findall('<.*?href=".*?illust_id=(.*?)&amp.*?".*?work\s\s_work\s.*?>',page,re.S)
    print("IDs got")
    return(pic_IDs)


def save_pics(dir_path,ID,p):    
    url = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id="+ID
    page_pic = p.get(url).text
    picUrl = re.findall('<img\salt=.*?data-src="(.*?)"\sclass="original-image".*?>',page_pic,re.S)
    header_new = {
                  'Referer':url,
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    p.headers = header_new
    try:
        picture = p.get(picUrl[0])
        open(dir_path+'\\'+ID+'.jpg', 'wb').write(picture.content)
        print(picUrl[0])       
    except IndexError:
        print('multiple')
        
    except ConnectionError:
        print('connectionerror')
    return(dir_path+'\\'+ID+'.jpg')

