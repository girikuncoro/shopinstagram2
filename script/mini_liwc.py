""" File 'mini_liwc.py' 
    assgn   : assignment 2/16
    tools   : -
    desc    : analyzing product categories
    question: What kind of products are sold in Instagram?
"""
# IMPORT
import nltk
from collections import defaultdict
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

# Getting argument from user's command line input
if __name__ == "__main__":
    import sys
    corpus = sys.argv[1]

# LIWC
# Defining dictionaries
clothing_shop = {"dress":1, "baju":1, "jeans":1, "kebaya":1, "celana":1, "bra":1, "cardigan":1, 
                "sweater":1, "cotton":1, "hijab":1, "rok":1, "skirt":1, "miniskirt":1, "longskirt":1,
                "vest":1, "hotpants":1, "tshirt":1, "hijabers":1, "jersey":1, "tenun":1, "kaos":1}
accessory_shop = {"eyewear":1, "kacamata":1, "sunglasses":1, "glasses":1, "kalung":1, "anting":1, "necklace":1,
                  "hairclip":1}
footwear_shop = {"sepatu":1, "boots":1, "boot":1, "shoes":1, "footwear":1, "nike":1, "sneakers":1, "wedges":1, "sandal":1}
bag_shop = {"bag":1, "tas":1}
gift_shop = {"kado":1, "popupcard":1, "popup":1, "card":1, "hadiah":1, "gift":1, "coklat":1, "chocolate":1}
home_shop = {"lampu":1, "sprei":1, "bed":1, "lampumurah":1}
health_shop = {"herbal":1, "keputihan":1, "langsing":1, "kesehatan":1, "pemutih":1, "penyakit":1, "healthy":1,
               "gairah":1, "alami":1, "sabun":1, "alergi":1, "reproduksi":1, "vagina":1}
beauty_shop = {"makeup":1, "lipstick":1, "lips":1, "eyeliner":1, "kosmetik":1, "wajah":1,
               "flek":1, "jerawat":1, "shampoo":1, "skin":1}

liwc = {}
liwc["clothing"] = clothing_shop
liwc["accessory"] = accessory_shop
liwc["footwear"] = footwear_shop
liwc["bag"] = bag_shop
liwc["gift"] = gift_shop
liwc["home"] = home_shop
liwc["health"] = health_shop
liwc["beauty"] = beauty_shop
liwc["others"] = {}

# Analyzing product categories from data_cleaned.txt
cat_counts = defaultdict(int)
text = ''
count_line = 0
cat_found = 0

f_cleaned = open(corpus, 'r')
for line in f_cleaned.readlines():
    data_array = line.split('|')
    tokens = nltk.word_tokenize(data_array[6])
    text += data_array[6] # Merging corpus
    count_line += 1 # Count number of products sold

    for cat in liwc:
    	for t in tokens:
			if t in liwc[cat]:
				cat_counts[cat] += 1
				cat_found += 1
				break
cat_counts["others"] = count_line - cat_found
all_tokens = nltk.word_tokenize(text)
f_cleaned.close()

# Finding 20 most common words used for selling products
product = nltk.FreqDist(t for t in all_tokens)
print "======================="
print "Most common words"
print "======================="
pprint (product.most_common()[:20])

# Printing product categories
print "======================="
print "Product categories"
print "======================="
for key in cat_counts:
    if key is not 2:
        print key,":",cat_counts[key]
print "======================="
print "total :", count_line


# Visualization
# matplotlib is used to plot the data
x_pos = cat_counts.keys()
y_pos = np.arange(len(x_pos))
counts = cat_counts.values()

plt.barh(y_pos, counts, align='center', alpha=0.4)
plt.yticks(y_pos, x_pos)
plt.xlabel('Number of products')
plt.title('Products sold in #onlineshopjogja Instagram')
plt.show()


