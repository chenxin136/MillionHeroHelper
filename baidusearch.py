#coding=utf-8

import urllib
from urllib import parse
from bs4 import BeautifulSoup
import sys
import re

# reload(sys)
# sys.setdefaultencoding('utf-8')

# with open('data.txt','wa') as f:
#     key_word = []
#     with open('key_word.txt','r') as kf:
#         for line in kf:
		
class BaiduSearch(object):
	"""docstring for BaiduSearch"""
	def __init__(self, url):
		super(BaiduSearch, self).__init__()
		self.url = url
		

	def getResult(self):

		line = self.url
		# line = unicode(line, 'GBK').encode('utf-8')
		# request = urllib.request.Request('http://www.baidu.com/s?wd='+parse.quote(line.strip().decode(sys.stdin.encoding).encode('gbk')))
		line = parse.quote(line.encode('gbk'))

		request = urllib.request.Request('http://www.baidu.com/s?wd='+line)
		response = urllib.request.urlopen(request)

		soup = BeautifulSoup(response.read(), "lxml")
		# print(soup.a.string)

		# data = [re.sub(u'<[\d\D]*?>',' ',str(item)) for item in soup.select('div.result h3.t > a')]  
		# data = [re.sub(u'<[\d\D]*?>',' ',str(item)) for item in soup.select('div.c-span18')]
		data = [re.sub(u'<[\d\D]*?>',' ',str(item)) for item in soup.select('div.c-abstract')]


		result = ''
		for item in data:
		    # f.writelines(''.join(item.strip().split())+'\n')
		    result += ''.join(item.strip().split())
		    # print(''.join(item.strip().split()))
		
		return result
		# print(result)

# d = BaiduSearch('北京火车站')
# print(d.getResult())