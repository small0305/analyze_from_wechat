# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:27:23 2017

@author: My
"""

def reply(text):
    if '啪' in text:
        return text.count('啪')*'[捂脸]'
    if '喵' in text:
        return text.count('喵')*'喵'
        
        