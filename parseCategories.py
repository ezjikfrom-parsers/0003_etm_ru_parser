# -*- coding: utf-8 -*-
'''
Created on 13.08.2020

@author: Sergey
'''
from bs4 import BeautifulSoup;
import requests;
#from builtins import None

#func to take SOUP (html of page for bs4) to parse data
def take_soup(url):
    page = requests.get(url);
    soup = BeautifulSoup(page.text, "html.parser");
    return soup;


def take_categories_all(soup):
    lis = soup.find('div', class_='shadow-nav');
    
    list_of_categories = [];
    
    #names_cat = lis.find_all('li');
    
    link_cat = lis.find_all('a')
    #print(link_cat)
    for x in link_cat:
        try:
            #name_category = x.a.text;
            link_category = 'https://www.etm.ru'+x['href'];
            list_of_categories.append(link_category);
        except:
            continue;
    return list_of_categories;


if __name__ == '__main__':
    url = 'https://www.etm.ru/catalog/';
    #we take all categories and link
    soup = take_soup(url);
    list_of_categories = take_categories(soup);
    for i in list_of_categories:
        print(i);
    