#!/usr/bin/env python
'''
nypull_article.py
@author: varunjai, dilipred
'''

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
import time
import sys
from bs4 import BeautifulSoup

in_file = sys.argv[1] 

# initiate session
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


cnt = 1
for url in open(in_file):
    output = None
    try:
       # hit url
       resp = session.get(url)
       soup = BeautifulSoup(resp.content, 'html.parser')
      
       # search for <p> tag with attributes itemprop=articleBody
       #articles = soup.findAll("p", {"itemprop" : "articleBody"})
       articles = soup.findAll("p")

       # get text from each article and append to file
       text = ''
       for article in articles:
           # concatenate
           text += article.get_text() + ' '

       # format    
       text = text.replace('\n', ' ')
       text = text.replace('\t', ' ')

       # write to file        
       output = open('article' + str(cnt) + '.txt', 'w')
       output.write(text)
       output.close()

       # increment cnt 
       cnt += 1

    except:
       # suppress exceptions related to connection refused
       print("Connection refused by the server..")

       # close file
       if(output is not None):
             output.close()
    
    # sleep for 5s post each request
    time.sleep(10)

# close
session.close()
