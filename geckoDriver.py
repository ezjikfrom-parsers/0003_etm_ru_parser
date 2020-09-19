  # -*- coding: utf-8 -*-
'''
Created on 24.08.2020

@author: Sergey
'''
from selenium import webdriver
from selenium.webdriver import Firefox;
from selenium.webdriver.firefox.options import Options;
#for save data in file
import pickle;
#pause in programm
import time;


def openPage(url,browser):
    #options = webdriver.FirefoxOptions()
    #don't open page:
    #options.add_argument('-headless')
    #browser = Firefox(executable_path=r'geckodriver.exe');#,options=options);
    browser.get(url);
    browser.get(url);
    time.sleep(30);
    print('30')
    time.sleep(20);
    print('50')
    time.sleep(10);
    main_page = browser.page_source;
  
    return main_page;

def openPageNotSeeIt(url,browser):
    #options = webdriver.FirefoxOptions()
    #don't open page:
    #options.add_argument('-headless');
    #browser = Firefox(executable_path=r'geckodriver.exe',options=options);
    browser.get(url);
    browser.get(url);
    main_page = browser.page_source;
  
    return main_page;

def loadCookie(browser):
    with open('data.pickle', 'rb') as f:
        cookies = pickle.load(f);
    for cooki in cookies:
        browser.add_cookie(cooki)
    return browser;



if __name__ == '__main__':
    url = 'https://www.etm.ru/catalog/';
    
    #driver = Firefox(executable_path=r'geckodriver.exe');
    #driver.get(url);
    #main_page = driver.page_source
    #time.sleep(8);
    #pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
    #driver = Firefox(executable_path=r'geckodriver.exe');
    #driver.get(url);
    #cookies = pickle.load(open("cookies.pkl", "rb"))
    #for cookie in cookies:
        #driver.add_cookie(cookie)
    #time.sleep(2);
    #driver.get(url);
    
    