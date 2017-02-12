#-*- coding: UTF-8 -*- 
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

import io
import re
import jieba
from jieba import analyse
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from os import path

filename = #relative path of html file
pic_path = #relative path of mask image


def get_text_from_html(filename):
	'''
	Given a html file, returns the chat content from it.
	The part of chat content is like this:
		<pre style="white-space:pre-wrap;*white-space:pre;*word-wrap:break-word;">欢迎！</pre>
	'''
	f = io.open(filename,'r',encoding='utf-8')
	content = f.read()
	f.close()

	chats = re.findall('<pre style=\"white-space\:pre\-wrap\;\*white-space\:pre\;\*word\-wrap\:break\-word\;\">(.*?)</pre>', content)
	chats = [chat for chat in chats if '[' not in chat and 'png' not in chat]
	text = '\n'.join(chats)
	text = re.sub(u'\W+', '', text, flags=re.U)
	return text

def get_keywords_from_text(text,n=200):
	'''
	Given the text and number of keywords we need, returns the frequences list.
	The frequences is like:
		[('喵',0.1),('兔子',0.05),...]
	'''
	key_words = jieba.analyse.extract_tags(text, topK=n, withWeight=True, allowPOS=('nb','n','nr', 'ns','a','ad','an','nt','nz','v','d'))
	frequences =[]
	for word,fre in key_words:
		frequences.append((word,fre))
	return frequences


def output(frequences,filename):
	'''
	Given the frequences list and previous filename, print the frequences in filename.summary.
	'''
	text = ""
	for word,fre in frequences:
		text += word + " " + str(fre) +"\n"
	outf = open(filename + '.summary', 'w')
	outf.write(text)
	outf.close()

def input_from_file(filename):
	'''
	Given the previous filename, get frequences from the file.
	'''
	f = io.open(filename + '.summary','r',encoding='utf-8')
	content = f.readlines()
	f.close()
	frequences =[]
	for line in content:
		word,fre = line.split()
		frequences.append((word,float(fre)))
	return frequences


def draw_pic_with_frequences(frequences,pic_path,fontpath = 'MSYH.TTC'):
	'''
	Given frequences list and mask image path, plot the image of word cloud.
	'''
	d = path.dirname(__file__)
	mask_pic = np.array(Image.open(path.join(d, pic_path)))
	wc = WordCloud(background_color="white", mask=mask_pic,max_font_size=40, random_state=11,font_path=fontpath)
	wc.fit_words(frequences)
	image_colors = ImageColorGenerator(mask_pic)
	plt.axis("off")
	plt.imshow(wc.recolor(color_func=image_colors))
	plt.show()

text = get_text_from_html(filename)
frequences = get_keywords_from_text(text)

## Incase the frequences need to be revised:
# output(frequences, filename)
# frequences = input_from_file(filename)

draw_pic_with_frequences(frequences, pic_path)
