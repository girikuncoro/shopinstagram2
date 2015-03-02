""" File 'get_user.py' 
    assgn   : assignment 2/16
    tools   : -
    desc    : getting user data from data_raw.txt
    question: What countries use Instagram as online store?
"""
# IMPORT
import json
from instagram.client import InstagramAPI
from urllib import urlopen

# Getting argument from user's command line input
if __name__ == "__main__":
    import sys
    file_input = sys.argv[1]
    file_output = sys.argv[2]

# CONSTANT
# Register and get client_id here http://instagram.com/developer/
client_id = "2386e30798cf4e87a573d62b701813d2"
base_url = "https://api.instagram.com/v1"
endpoints = "users"
uid_list = []
user_list = []

# Get user data
# Rewrite to user_data.txt
f_raw = open(file_input, 'r')
f_cleaned = open(file_output, 'w')
for line in f_raw.readlines():
    user_array = line.split('|')
    user_id = user_array[3]
    user_name = user_array[2]
    if user_id not in (uid_list):
        # getting user data from Instagram
        url = "{0}/{1}/{2}/?client_id={3}".format(base_url, endpoints, user_id, client_id)
        json_data = urlopen(url).read()
        response = json.loads(json_data)

        # parsing followers and number of posts
        if 'data' in response:
            user_followers = str(response['data']['counts']['followed_by'])
            user_posts = str(response['data']['counts']['media'])

        # adding user to the list
        uid_list.append(user_id)
        user_list.append([user_id, user_name, user_followers, user_posts])
        print "Added " + user_id

# Write to user_data.txt start from largest followers
# user_list = sorted(user_list, key=lambda lst: int(lst[2]), reverse=True)

# Write to user_data.txt start from the most posts
user_list = sorted(user_list, key=lambda lst: int(lst[3]), reverse=True)
for user in user_list:
    user_id = user[0]
    user_name = user[1]
    user_followers = user[2]
    user_posts = user[3]
    f_cleaned.write(user_id + '|' + user_name + '|' + user_followers + '|' + user_posts + '\n')
    
f_cleaned.close()
f_raw.close()
print "Successfully added " + str(len(user_list)) + " users to list"