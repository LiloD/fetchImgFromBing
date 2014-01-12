#! /usr/bin/env python
'''Personal Interest,using Python to fetch the background Image from bing
It is just so interesting
by Zhizhuo Ding '''

import urllib2
import urllib
import re
import os

#The url below will response a json object which contains the img url
#http://www.bing.com/HPImageArchive.aspx?
#format=js&idx=1&n=1&nc=1389477541224&pid=hp&FORM=HYLH&video=1

#mkdir named bing_img to store the images fetched from bing
if not os.path.exists("bing_img"):
	os.mkdir("bing_img")

bing_url = r"www.bing.com"

#to match the imge url from the Json Object
reg = r'"url":"(.+?)"'
regObj = re.compile(reg)


for i in range(0,10):
	#get the url
	url = r"http://www.bing.com/HPImageArchive.aspx?format=js&idx="+str(i)+"&n=1&nc=0&pid=hp&FORM=HYLH&video=1"
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	fetch_img_url = bing_url + regObj.search(data).group(1)

	print fetch_img_url
	name = fetch_img_url.split('/')[4]
	fetch_img_url = "http://"+fetch_img_url
	savepath = "bing_img/"+name
	#save the image
	urllib.urlretrieve(fetch_img_url,savepath)


