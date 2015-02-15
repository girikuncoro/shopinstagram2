## About
The goal of this project is to find out what kind of products are sold in Instagram and who are the big players using Instagram as online store. Products are categorized using self-defined LIWC. We analyze the data collected from "#onlineshopbali" and "#onlineshopjogja" tags.

## Requirement
This project uses Instagram API, NLTK library for Natural Language Processing, Numpy for fundamental computation in Python and matplotlib to plot a simple visualization. In the script, we already assigned client ID as permission to use Instagram API, you don't have to generate by yourself. Install Python, NLTK, Numpy and matplotlib if you haven't.

1. Python 2.7 (https://www.python.org/downloads/), do not use Python 3 as not supported by NLTK library
2. NLTK (http://www.nltk.org/install.html)
3. Numpy (http://www.scipy.org/install.html), it is usually included during Python installation
4. matplotlib (http://matplotlib.org/users/installing.html)

## How To
1. To collect posts in Instagram with specific tags, run "crawl.py" followed by query tags you want to search. It will collect posts written to file. Find below example for crawling data using #onlineshopbali tags that is written to "data_raw.txt".
```
# python crawl.py onlineshopbali data_raw.txt
```
2. To find out list of unique username from particular raw data file, run "get_user.py". It will generate text file with the list.
```
# python get_user.py data_raw.txt user_data.txt
```
3. To clean the data, run "cleaner.py", it will remove unnecessary stuffs like smiley, hashtags, unrelated links, stopwords, etc and generate output file. Specify the input and output filename on the command line as below example.
```
# python cleaner.py data_raw.txt data_cleaned.txt
```
4. To find what kind of products are posted, run "mini_liwc.py" follows by text file that will be analyzed. This will print out most common words, product categories and visualization. Products that are not defined in our LIWC will be categorized as "others".
```
# python mini_liwc.py data_cleaned.txt
```
## Author
>>>>>>> 29528078c0222e65b4c2b3b0eb4ff4a37e6c69a6
Hello, I'm Giri! This project is written by me as part of my assignment in INFO6010 - Computational Method in Information Science. DanCo (http://www.cs.cornell.edu/~danco/) teaches this, he is a great professor! Checkout my web (http://kuncoro.co) to know more about me.
