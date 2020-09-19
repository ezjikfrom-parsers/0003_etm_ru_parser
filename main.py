# -*- coding: utf-8 -*-
'''
Created on 19.08.2020

@author: Sergey
'''

import products_parse;
import parseCategories;
import write_csv;
import geckoDriver;
#play alert
import winsound
#take data from html
from bs4 import BeautifulSoup;
import pickle;
import random;
#many process together:
#import threading;
import time;
from selenium import webdriver;
from selenium.webdriver import Firefox;
from selenium.webdriver.firefox.options import Options;
from selenium.webdriver.common.proxy import Proxy, ProxyType


options = webdriver.FirefoxOptions()
options.add_argument('-headless');
#browser = Firefox(executable_path=r'geckodriver.exe');#,options=options);
browser2 = Firefox(executable_path=r'geckodriver.exe',options=options);
url = 'https://www.etm.ru/catalog/';
browser2.get(url);
browser2.get(url);

def find_all_categoties_link(url,browser):
    #we take HTML data with gekcoDriver:
    html = geckoDriver.openPage(url,browser);
    soup = BeautifulSoup(html, 'lxml');
    links = parseCategories.take_categories_all(soup);
    
    
    #save in file:
    with open('categories.pickle', 'wb') as f:
        pickle.dump(links, f);        

def find_all_products(url):
    glob_list_of_products = [];
    count_page = 1;
    while True:
        html = geckoDriver.openPage(url+'?goodsOnPage=25&searchValue=&val=&pars=mnf&cst=0&dst=&sidx=rel&sord=desc&page={}&spec=0'.format(count_page),browser);
        soup = BeautifulSoup(html, 'lxml');
        products_on_page = products_parse.take_links_from_page(soup);
        if products_on_page[0] in glob_list_of_products:
            print('OOOOps! We stop in Product on page:',products_on_page[0]);
            print('Glob list:',glob_list_of_products)
            break;
        glob_list_of_products = glob_list_of_products + products_on_page;
        count_page += 1;
    return glob_list_of_products;
    
def go_all_number_products(range1,range2,x):
    count = 1;
    list_of_all_products = [];
    for i in range(range1,range2):
        for attempt in range(1,20):
            try:
                url = 'https://ipro.etm.ru/cat/descsc.html?nn={}&t=ipro'.format(i);
                #print(url);
                soup = products_parse.take_soup(url);
                #print(soup)
                #print(soup.find('h1',class_='desc-h1'));
                if soup.find('h1',class_='desc-h1') != None:
                    list_of_all_products.append(url);
                    print('Number in url:',i);
                    print('Взяли товар', x, '-', count);
                    count += 1;
            except:
                #print(url);
                time.sleep(attempt);
                continue;
            break;
    with open('products{}.pickle'.format(x), 'wb') as f:
        pickle.dump(list_of_all_products, f);

    print('---------------All!--------------------',range1,range2)

def take_list_products_on_page(url,browser2):
    page = geckoDriver.openPageNotSeeIt(url+add,browser2);
    soup = BeautifulSoup(page, "html.parser");
    list_of_products = products_parse.take_links_from_page(soup); 
    
    return list_of_products;

#take proxy
def change_proxy(proxy,port):
    profile = webdriver.FirefoxProfile();
    profile.set_preference("network.proxy.type", 1);
    profile.set_preference("network.proxy.http", proxy);
    profile.set_preference("network.proxy.http_port", port);
    profile.set_preference("network.proxy.ssl", proxy);
    profile.set_preference("network.proxy.ssl_port", port);

    return profile;

if __name__ == '__main__':
    print("Let's begin!");
    #take categories and save them in categories.pickle:
    #url = 'https://www.etm.ru/catalog/';
    #find_all_categoties_link(url);
    
    #load from categories.pickle
    
    with open('categories.pickle', 'rb') as f:
        links_categories = pickle.load(f);

    with open('products_links_list.pickle', 'rb') as f:
         all_list_of_products = pickle.load(f);     

    #parse products:
    #all_list_of_products = []
    count = 0;
    for category in links_categories:
        #pass what we wrote
        count += 1;
        if count < 79:
            continue;
        url = category;
        for num_page in range(1,5):
            add = '?goodsOnPage=25&page={}'.format(num_page)
            time_sleep = 1;
            while True:
                list_of_products = take_list_products_on_page(url+add,browser2);
                if list_of_products != []:
                    #print('Nice');
                    time_sleep = 2;
                    break;
                else:
                    #print(browser2.page_source);
                    '''#reload browser
                    #browser2.close();
                    #browser2.quit();
                    
                    #list_proxy = ['91.217.42.2','178.62.223.104','91.217.42.4','85.12.221.147','46.101.113.185','94.230.35.108',
                                  '88.198.50.103','191.96.42.80','52.56.220.212','70.83.106.82','165.227.35.11'];
                    #list_port = ['8080','80','8080','80','80','80','3128','8080','80','55801','80']; 
                    #num = random.randrange(0, len(list_proxy), 1)
                    
                    #proxy = list_proxy[num];
                    #port = list_port[num];
                    
                    #try usual pref:
                    #if time_sleep == 3 or time_sleep == 5:
                        #browser2.quit();
                        #browser2 = Firefox(executable_path=r'geckodriver.exe')#,options=options);
                    #else:
                        #print(proxy,port);                   
                        #profile = change_proxy(proxy,port)                        
                        #browser2 = Firefox(executable_path=r'geckodriver.exe',options=options,firefox_profile=profile);
                    #reload page to take city:
                    url = 'https://www.etm.ru/catalog/';
                    browser2.get(url);
                    time.sleep(time_sleep);
                    browser2.get(url);'''
                    if time_sleep > 40:
                        break;
                    print('pause in',url+add); 
                    
                    browser2.get(url+add);
                    
                    time.sleep(time_sleep);
                    time_sleep += 0.25;
                
            all_list_of_products = list_of_products + all_list_of_products
        print('Всего товаров записали: ',len(all_list_of_products));
        print('Записали категорию:\n', category);
    
        #save in file:
        with open('products_links_list.pickle', 'wb') as f:
            pickle.dump(all_list_of_products, f); 
        print('Wrote',count,'link in list');
        
    
    '''
    #go_all_number_products(range1,range2);
    range1 = 1;
    range2 = 20001;
    
    for i in range(1,2):
        my_thread = threading.Thread(target=go_all_number_products, args=(range1,range2,i));
        my_thread.start();
        range1 += 20000;
        range2 += 20000;
    '''
    
    '''
    #we take HTML data with gekcoDriver:
    url = 'https://www.etm.ru/catalog/';
    html = geckoDriver.openPage(url);
    
    #and then we take soup for bs4
    soup = BeautifulSoup(html, 'lxml')
    #print(soup);
    #take links of categories
    list_of_categories = parseCategories.take_categories(soup);
    
    print('All categoies:')
    print(list_of_categories);
    #--------------------------------take links on orders in categoty:-----------------
    for link in list_of_categories:
        all_products_on_page = find_all_products(link);
        print('Products on page:',len(all_products_on_page));
        print('page:', link);
        print(all_products_on_page, '\n');
    
    print('---------------------All!----------------------');
    #play alert:
    winsound.Beep(500, 500);
    winsound.Beep(500, 500);
    '''
    
    
