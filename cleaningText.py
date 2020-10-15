# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:14:21 2020

@author: icska
"""
#importing libraries
from bs4 import BeautifulSoup
import nltk
import pandas as pd
import requests
import re
import string

#function to verify a valid url in loop
def is_valid(url):
    if url:
        if url.startswith('/wiki/'):
            if not re.compile('/\w+:').search(url):
                return True
            
            
            
    return False

#random url to scrape
random_url = 'https://en.wikipedia.org/wiki/TypeScript'

#send request 
request_one = requests.get(random_url)

#print request url
print('url:', request_one.url)

#parser for text in the random url
soup = BeautifulSoup(request_one.text, 'html.parser')

#extracts title in <h1> tag
title_one = soup.find('h1', {'class': 'firstHeading'})

#printing random url and title
print('starting website:', request_one.url)
print('titled:', title_one.text)

#empty list for hrefs
valid_urls = []

#looping to find all hrefs in random_url
for link in soup.find_all('a'):
    url = link.get('href', '')
    if url not in valid_urls and is_valid(url):
        valid_urls.append(url)
        
#prints all links in random_url
print('\n'.join(valid_urls))

#find all <p> tags in url and store as string
p_tags = str(soup.find_all('p'))

#convert p_tags object to list of words
words = p_tags.split()

#punctuation characters to remove from text
print(string.punctuation)

#translation table object
translation_table = str.maketrans('', '', string.punctuation)

#strip each word with translation_table
stripped = [w.translate(translation_table) for w in words]

#print first 50
print(stripped[:50])

#using nltk to clean and tokenize text
#initialize a new url
another_url = 'https://en.wikipedia.org/wiki/Computational_linguistics'

#send another request 
request_two = requests.get(another_url)

#print another request url
print('url_two:', request_two.url)

#parser for text in the another url
soup = BeautifulSoup(request_two.text, 'html.parser')

#extracts title in <h1> tag
title_two = soup.find('h1', {'class': 'firstHeading'})

#printing another url and title
print('another website:', request_two.url)
print('titled:', title_two.text)

#empty list for hrefs
more_urls = []

#looping to find all hrefs in another_url
for link in soup.find_all('a'):
    url = link.get('href', '')
    if url not in more_urls and is_valid(url):
        more_urls.append(url)
        
#prints all links in another_url
print('\n'.join(more_urls))

#find all <p> tags in url and store as string
p_tags_two = str(soup.find_all('p'))

#removing stop words with nltk
nltk.download('stopwords')
stop_words = stopwords.words('english')

#importing tokenizer
from nltk.tokenize import word_tokenize

#tokenizing p_tags_two
tokens = word_tokenize(p_tags_two)

#convert to lowercase
tokens = [w.lower() for w in tokens]

#remove punctuation
stripped_two = [w.translate(translation_table) for w in tokens]

#remove blanks and other unneeded tokens
words_two = [word for word in stripped_two if word.isalpha()]

#remove stopwords
words_two = [w for w in words_two if not w in stop_words]

#print first 50
print(words_two[:50])

#pandas series and value_counts() method
words_two = pd.Series(words_two)
unique_two = words_two.value_counts()

#more words to remove
to_remove = ['p', 'b', 'mt', 'eg', 'like', 'put', 'thus',
             'day', 'al', 'et', 'nt', 'g', 'id', 'href', 'sup']
words_two = [w for w in words_two if not w in to_remove]

#rerunning pandas series and value_counts() method
words_two = pd.Series(words_two)
unique_two = words_two.value_counts()