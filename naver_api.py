import os
import sys
import urllib.request
import pandas as pd
import json
import re

client_id = "D0lj0dwSs9pw8T4tHNo2"
client_secret = "bog5VuUDnc"

query = urllib.parse.quote(input('검색 질의: '))
idx = 0
display = 100
start = 1
end = 1000

web_df = pd.DataFrame(columns=('Title', 'link', 'Description'))

for start_index in range(start, end, display):

    url = "https://openapi.naver.com/v1/search/book?query=" + query \
        + "&display=" + str(display) \
        + "&start=" + str(start_index) 

    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_dict = json.loads(response_body.decode('utf-8'))
        items = response_dict['items']
        for item_index in range(0, len(items)):
            remove_tag = re.compile('<.*?>')
            title = re.sub(remove_tag, '', items[item_index]['title'])
            link = items[item_index]['link']
            description = re.sub(remove_tag, '', items[item_index]['description'])
            web_df.loc[idx] = [title, link, description]
            idx += 1
    else:
        print("Error Code:" + rescode)

