import json
from instagram.client import InstagramAPI
from urllib import urlopen
from pprint import pprint

client_id = "c58899640d8943ccab8d1cacfaced36a"
base_url = "https://api.instagram.com/v1"
endpoints = "users"

# Getting argument from user's command line input
if __name__ == "__main__":
    import sys
    file_input = sys.argv[1]
    file_output = sys.argv[2]

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
count_caption,count_stores = 0,1
contents = ''
content = ''

json_data = open(file_input)
stores = json.load(json_data)
json_data.close()

for store in stores:
    uid = store['uid']
    url = "{0}/{1}/{2}/media/recent/?client_id={3}".format(base_url, endpoints, uid, client_id)
    while url != '':
        next_data = urlopen(url).read()
        response = json.loads(next_data)
        for i in range(0, len(response['data'])):
            if 'data' in response:
                data = response['data'][i]
                content += ',{' + '"times":"{0}","likes":{1},"comments":{2}'.format(data['created_time'], data['likes']['count'], data['comments']['count']) + '}'
                count_caption += 1
        url = get_next_page(response)
        print 'crawled {0} posts from {1} stores'.format(count_caption, count_stores)
        if url == '':
            contents += '"{0}":[{1}]'.format(uid, content[1:])
    count_stores += 1
    contents += ','

f = open(file_output, 'w')
f.write('{' + contents[:-1] + '}')
f.close()