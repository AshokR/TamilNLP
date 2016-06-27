#!/usr/bin/python3
# -*- coding: utf-8 -*-

from wikiapi import WikiApi
import requests, pprint

# This is suitable for extracting content that is organized by pages under a title
# This code requires the wiki-api python library created by Richard O'Dwyer of UK
# https://github.com/richardasaurus/wiki-api

wiki = WikiApi()
wiki = WikiApi({ 'locale' : 'ta'}) # to specify your locale, 'en' is default

# Get the page text of the article with the given title
def getArticleParagraphs(title):
    print(title)
    articleFull = wiki.get_article(title)
    fullText = articleFull.content

    article = ""
    paragraphs = fullText.split('\n\n')
    # print(paragraphs)
    # We want only whole paragraphs that end in a ".", "!", "?" or '"' not fragments
    for paragraph in paragraphs:
        if len(paragraph) > 30:
            end = paragraph[-1]
            if end == '.' or end == '!' or end == '?' or end == '"':
                article = article + "\n\n" + paragraph
    return article

f = open('/your/folder/wikisource_content.txt', 'wt', encoding='utf-8')
def getPagesForTitle(title):
    # In the wikiapi.py file change the following two lines
    # api_uri = 'wikisource.org/w/api.php'
    # article_uri = 'wikisource.org/wiki/'
    baseUrl = 'https://ta.wikisource.org/w/api.php?action=query&list=allpages&aplimit=500&format=json'
    titleUrl = '&apprefix='
    url = baseUrl + titleUrl + title
    print(url)
    data = requests.get(url)
    result = data.json()
    pprint.pprint(result)
    for item in result['query']['allpages']:
        # print(item['title'])
        f.write(getArticleParagraphs(item['title']))

getPagesForTitle('பொன்னியின் செல்வன்')



