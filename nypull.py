#!/usr/bin/env python
'''
nypull.py
@author: varunjai, dilipred
'''

import requests
import json
from pprint import pprint
import sys
import time

#api_key = 'ea222a49a7ca488e89629a34992cb293'
api_key = '8b18491cab36479486581b2c19309a5e'
query = sys.argv[1]
out_file = sys.argv[2]
web_urls = []

# iterate 10 pages
for i in range(10):
    
    # call NYT article api
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=' + api_key + '&q='+ query + '&page=' + str(i)
    resp = requests.get(url)
    data = json.loads(resp.content)

    # each page in turn contains 10 article urls
    for key in data['response']['docs']:
         url = key['web_url']
         
         if(url is not None):
             web_urls.append(key['web_url'])
             print(key['web_url'])

    # sleep for 5s b/w each request
    time.sleep(5)


# write to file
file = open(out_file, 'w')
for web_url in web_urls:
   file.write("%s\n" % web_url)
file.close()
         
      


