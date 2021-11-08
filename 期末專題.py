# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 05:29:05 2021

@author: a526a
"""

from urllib.request import urlopen
x=urlopen(url="https://news.ltn.com.tw/rss/politics.xml")
s=x.read()
##print(s.decode("utf8"))
f=open(file="Ltn_politics.xml",mode="w",encoding="utf8")
f.write(s.decode("utf8"))
f.close()
from xml.etree import ElementTree
f=open(file="Ltn_politics.xml",mode="r",encoding="utf8")
tree=ElementTree.parse(f)
root=tree.getroot()

import jieba
jieba.load_userdict('./green.txt')
x=0
for item in root.iter('item'):
    values=[]
    for child in item:
        if child.text is None:values.append('')
        else:values.append(child.text.strip())
    title,description,link,pubDate=values
    seg_list=jieba.lcut(description)
    if '公投' in seg_list:
        x=x+1
    ##print('\t'.join([pubDate,link,title,description]))

print('公投:',x)




