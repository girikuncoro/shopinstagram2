""" File 'crawl_stores.py' 
    assgn   : assignment 3/2
    tools   : -
    desc    : crawling posts from instagram stores
    question: What kind of products are sold in Instagram?
"""
# IMPORT
import json
from instagram.client import InstagramAPI
from urllib import urlopen

# CONSTANT
# Register and get client_id here http://instagram.com/developer/
# Get stores data from json file
client_id = "ff8b092c952a43b18e6fc41e33da8150"
base_url = "https://api.instagram.com/v1"
endpoints = "users"

json_data = open('analyses/bali_stores_sample.json')
stores = json.load(json_data)
json_data.close()

# Write Instagram response to data_raw.txt
f = open('bali_stores_data.json', 'w')
def write_to_txt(data):
    if 'text' in data['caption']:
        f.write('"time":' + data['created_time'] + ',')
        f.write('"likes":' + str(data['likes']['count']) + ',')
        f.write('"comments":' + str(data['comments']['count']) + '}')

# Fetch next posts batch
def get_next_page(content):
    if 'pagination' in content:
        if 'next_url' in content['pagination']:
            return content['pagination']['next_url']
        else:
            return ''
    else:
        return ''

# MAIN
# Crawl posts from each page
count_caption = 0
count_uid = 0
for store in stores:
    count_uid += 1
    uid = store['uid']
    url = "{0}/{1}/{2}/media/recent/?client_id={3}".format(base_url, endpoints, uid, client_id)

    f.write('{"' + uid + '":[{')
    while url != '':
        next_data = urlopen(url).read()
        response = json.loads(next_data)
        if 'data' in response:
            for i in range(0, len(response['data'])):
                if response['data'][i]['caption'] is not None:
                    write_to_txt(response['data'][i])
                    count_caption += 1
                    if i < len(response['data']) - 1:
                        f.write(',{')
        print 'crawled {0} captions from store #{1}'.format(count_caption, count_uid)
        url = get_next_page(response)
        if url != '':
            f.write(',{')
        else:
            f.write(']')

    if count_uid < 50:
        f.write(',')

f.write('}')           
f.close()
print "Successfully crawled {0}".format(count_caption)