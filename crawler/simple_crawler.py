#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       simple_crawler.py
#       
#       Copyright 2012 Kumar Varun <kumar@Eureka>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       

import urllib

'''
Usage

to crawl a URL url, url should begin with
'http://' or other protocol

uc = URL_Crawler(url)
urls = uc.get_urls()

'''

__all__ = ['Page_Crawler', 'File_Crawler', 'URL_Crawler']

class Page_Crawler(object):
    '''Crawls a html page given in form of string
    '''
    def __init__(self, page):
        self.html = page.replace('\'', '"')
        self.urls = []
    def get_urls(self):
        start_point = self.html.find('<a href=',0)
        while start_point >= 0:
	    eq = self._get_url(start_point)
    	    start_point = self.html.find('<a href=',eq)
        return self.urls

    def _get_url(self, start_point):
        start_quote = self.html.find('"',start_point)
        end_quote = self.html.find('"',start_quote+1)
        self.urls.append(self.html[start_quote+1:end_quote])
        return end_quote


class File_Crawler(object):
	'''Crawls a File and return URLS
	'''
	def __init__(self, f):
		self.f = f
		self.urls = []
		
	def get_urls(self):
		if type(self.f) == file : self.f.seek(0)
		page = self.f.read()
		page_crawler = Page_Crawler(page)
		self.urls = page_crawler.get_urls()
		return self.urls

class URL_Crawler(object):
	'''Crawls a Web Page pointed by the URL
	will if no protocol given we'll handle it as http
	'''
	def __init__(self, url):
		url = url.strip()
		if not '://' in url:
			url = 'http://'+url
		self.url = url
		self.urls = []
		
	def get_urls(self):
		res = urllib.urlopen(self.url)
		file_crawler = File_Crawler(res)
		self.urls = file_crawler.get_urls()
		self.clean_urls()
		return self.urls
	
	def clean_urls(self):
		'''takes care of relative urls, fixing them by appending it
		to base url.		 
		'''
		for i in range(len(self.urls)):
			url = self.urls[i].strip()
			if url.startswith('/') or url.startswith('#'):
				url = self.url+url
			self.urls[i] = url
		#TODO not sure about urls starting with "#" they need not 
		#not to be re-crawled,
		#should i take care of that in other handler 
		#or just remove it from returning list	
			
		
		
		

def main():
	
	return 0

if __name__ == '__main__':
	main()

