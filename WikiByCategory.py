#!/usr/bin/python3
# -*- coding: utf-8 -*-

from wikiapi import WikiApi
import requests, pprint

# This is suitable for extracting content that is organized by categories and sub-categories
# This code requires the wiki-api python library created by Richard O'Dwyer of UK
# https://github.com/richardasaurus/wiki-api
# Note that the Wikipedia categories and sub-categories are not in a tree structure. There are circular references.

wiki = WikiApi()
wiki = WikiApi({ 'locale' : 'ta'}) # to specify your locale, 'en' is default

# Get the page text of the article with the given title
def getArticleParagraphs(title):
    articleFull = wiki.get_article(title)
    fullText = articleFull.content

    chapter = ""
    paragraphs = fullText.split('\n\n')
    # print(paragraphs)
    # We want only whole paragraphs that end in a ".", "!", "?" or '"' not fragments
    for paragraph in paragraphs:
        if len(paragraph) > 30:
            end = paragraph[-1]
            if end == '.' or end == '!' or end == '?' or end == '"':
                chapter = chapter + "\n\n" + paragraph
    return chapter

articleTitles = []
f = open('/your/folder/wikipedia_content.txt', 'wt', encoding='utf-8')
def getTitlesForCategory(title):
    # url = 'https://ta.wikipedia.org/w/api.php?action=query&list=categorymembers&cmnamespace=14&cmlimit=500&format=json&cmtitle=Category:வரலாறு'
    # http://ta.wikipedia.org/w/api.php?action=query                # Base Url
    # &format=json                                                  # want data in JSON, default is XML
    # &cmlimit=500                                                  # முதல் 500 துணைப் பகுப்புகள் / கட்டுரைகள்
    # &cmnamespace=14                                               # 14 -  துணைப் பகுப்புகள்; 0 - கட்டுரைகள்
    # &list=categorymembers
    # &cmtitle=Category:வரலாறு                                       #  பகுப்பு = வரலாறு
    baseUrl = 'https://ta.wikipedia.org/w/api.php?action=query&list=categorymembers&cmlimit=500&format=json'
    # For extracting the Wikisource content
    # In the wikiapi.py file change the following two lines
    # api_uri = 'wikisource.org/w/api.php'
    # article_uri = 'wikisource.org/wiki/'
    # And change the baseUrl here as follows
    # baseUrl = 'https://ta.wikisource.org/w/api.php?action=query&list=categorymembers&cmlimit=500&format=json'
    namespaceUrl = '&cmnamespace='
    categoryUrl = '&cmtitle=Category:'
    articleNamespace = '0'
    categoryNamespace = '14'
    url = baseUrl + namespaceUrl + articleNamespace + categoryUrl + title
    # print(url)
    data = requests.get(url)
    result = data.json()
    pprint.pprint(result)

    # Get all the article titles and write to the list
    for item in result["query"]["categorymembers"]:
        print(str(len(articleTitles)) + ": " +  item['title'])
        # Skip duplicate titles that are already in the list
        if item['title'] not in articleTitles:
            articleTitles.append(item['title'])
            f.write(getArticleParagraphs(item['title']))
        else:
            break
        # Safety check to avoid an infinite loop
        if len(articleTitles) > 15000:
            return
    # Get all the sub-categories
    url = baseUrl + namespaceUrl + categoryNamespace + categoryUrl + title
    # print(url)
    data = requests.get(url)
    result = data.json()
    # For each sub-category
    for item in result["query"]["categorymembers"]:
        print("Item title: " + item['title'])
        # When we get the title of categories, we have to strip out the first 8 characters to get the title
        cat = item['title'][8:]
        getTitlesForCategory(cat)

getTitlesForCategory('வரலாறு')
print(len(articleTitles))