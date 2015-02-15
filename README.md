## About
The goal of this project is to find out which countries use Instagram as online stores the most. We will also collect Instagram posts that correspond to onlineshop tags for further analyses on what kinds of products are sold by the online shop members.

## Requirement
This project uses Instagram API and NLTK library for Natural Language Processing. In the script, I already assigned client id as permission to use Instagram API, you don't have to generate by yourself. Install Python and NLTK if you haven't.

1. Python 2.7 (https://www.python.org/downloads/), do not use Python 3 as not supported by NLTK library
2. NLTK (http://www.nltk.org/install.html)

## How To

1. To learn how many posts in Instagram related to online stores, run "country_shopper.py", it will print out total number of posts, related tags and most active countries.
2. To learn what kind of products are sold in Instagram (onlineshopbali tag), run "crawl.py", it will generate "data_raw.txt" with more than 20,000 posts. I chose Bali due to frequent use of english words.
3. To clean the data, run "cleaner.py", it will remove unnecessary stuffs like smiley, hashtags, unrelated links, etc and generate "data_cleaned.txt"
4. Data analyses is postponed due to limited amount of time. I will update this project again after learning some analyses techniques.

## Author

Hello, I'm Giri! This project is written by me as part of my assignment in INFO6010 - Computational Method in Information Science. DanCo (http://www.cs.cornell.edu/~danco/) teaches this, he is a great professor! Checkout my web (http://kuncoro.co) to know more about me.
