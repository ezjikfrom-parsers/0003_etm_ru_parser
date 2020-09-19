# -*- coding: utf-8 -*-
'''
Created on 13.08.2020

@author: Sergey
'''

from bs4 import BeautifulSoup;
import requests;
import time
#for test in that file
import geckoDriver
from selenium import webdriver
from selenium.webdriver import Firefox;
from selenium.webdriver.firefox.options import Options;




#func to take SOUP (html of page for bs4) to parse data
def take_soup(url):
    page = requests.get(url);
    print(page.status_code);
    soup = BeautifulSoup(page.text, "html.parser");
    return soup;

#func to take all links of products on page
def take_links_from_page(soup):
    lis = soup.find_all('div', class_='catalog-col-middle');
    #print(lis);
    #create variable to save list of links
    list_of_products = [];
    #print(lis);
    for divs in lis:
        link = divs.find('a', class_='nameofgood')['href'];
        #print(link);
        list_of_products.append('https://www.etm.ru'+link);
    #print(list_of_products);


    return list_of_products;

#we take all pages
def pagination(url_first):
    pass
    
    
def take_data_of_product(soup):
    #1. take title of product:
    page = soup.find('section', class_='content-right card');
    title = soup.find('h1');
    try:
        title = title.text;
    except AttributeError:
        #print("Mistake in one. Don't worry we just find empty product. We will go to next");
        return '';
    
    #2. take prise:
    #print(soup.find('span', class_='title-price-card'))
    price_internet = soup.find('span', class_='price');
    ans = price_internet.find('meta', {"itemprop":"lowPrice"})
    print(ans)
    prise_in_store = soup.find('span',class_ = 'num-price ').text;
    min_price = soup.find('span' , class_ = 'num-price.min-rub').text;

    
    #3. take photo:
    photo = soup.find('div', class_='owl-item active');
    photo = photo.img['src'];
    
    #4. take params:
    params = soup.find('div', class_='card-info hidden-768');
    params = params.find_all('div', class_='line-info');
    
    
    #take only data from tags
    listParamsNames = [];
    listParamsInfo = [];

    for data in params:
        first_and_sec_param = data.find_all('span');
        listParamsNames.append(first_and_sec_param[0].text)
        listParamsInfo.append(first_and_sec_param[1].text)
    
    dict_params = dict(zip(listParamsNames, listParamsInfo));
    
    
    
    params = ['Код товара', 'Артикул', 'Производитель', 'Страна', 'Наименование', 
     'Упаковки', 'Сертификат', 'Тип изделия','Длина, мм','Ширина, мм','Цвет','Материал изделия'];
    listParamsInfo = []
    #write list of params:
    for param in params:
        if param in dict_params:
            #print(dict_params);
            listParamsInfo.append(dict_params[param]);
        else:
            listParamsInfo.append('');
    #find new params:
    for param in dict_params:
        if param not in params:
            print('\nwe have not param',param);
            print(param)
    
    #5. take description:
    descr = soup.find('div', class_='card-description');
    descrAll = descr.find('p').text;
    
    #6. take category (from breadcrumbs):
    category = soup.find('div', class_='breadcrumbs');
    all_categories = category.find_all('span').text + category.find_all('a').text;
    #print('Главная категория товара:', main_category);
    
    '''#Каталог/С[ветильники/Светодиодные светильники
    one = ['Встраиваемые точечные светильники','Накладные светильники','Светодиодные панели и комплектующие к ним','Гирлянды',
           'Светодиодные даунлайты','Светодиодные линейные светильники'];
    #Каталог/Источники света/Лампы светодиодные
    two = ['Лампы для встраиваемых и накладных светильников','Накладные светильники','Лампы для встраиваемых и накладных светильников',
           'Лампы-свечи','Лампы-шарики, шары и груши','Рефлекторы "на винте"','Лампы 300-360° и кукурузы','Маленькие лампы для холодильника и шв. машинки',
           'Линейные лампы Т8','Лампы для хрустальных люстр','Золотистые лампы'
           'Лампы серии Ecola Premium','Цветные лампы','Мощные LED лампы','Лампы для диммера'];
    #Каталог/Источники света/Лампы накаливания
    three = ['Нитевидные лампы (Filament)'];
    #Каталог/Источники света/Лампы энергосберегающие
    four = ['Традиционные энергосберегающие (КЛЛ) лампы']
    #Каталог/Светильники/Прожекторы
    fife = ['Светодиодные даунлайты'];
    #Каталог/Источники света/Лента светодиодная
    six = ['Светодиодная лента и всё для светодиодной ленты'];

    if main_category in one:
        main_category = 'Каталог/Светильники/Светодиодные светильники';
    elif main_category in two:
        main_category = 'Каталог/Источники света/Лампы светодиодные';
    elif main_category in three:
        main_category = 'Каталог/Источники света/Лампы накаливания';
    elif main_category in four:
        main_category = 'Каталог/Источники света/Лампы энергосберегающие';
    elif main_category in four:
        main_category = 'Каталог/Светильники/Прожекторы';
    elif main_category in four:
        main_category = 'Каталог/Источники света/Лента светодиодная';'''
    
    '''#print('Главная категория товара:', main_category);
    all = '';
    for i in descrAll:
        all = all + i.text;'''
    
    #print('Параметры:',listParamsInfo);
    return {'main_category':main_category,'title':title,'prise_minus_5':prise_minus_5, 'oldPrice':oldPrice,'realPrice':realPrice,'discauntPrice':discauntPrice, 'photo':photo,'listParamsNames':listParamsNames,'listParamsInfo':listParamsInfo,'alltext':descrAll};

if __name__ == '__main__':
    
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless');
    browser = Firefox(executable_path=r'geckodriver.exe',options=options);
    
    url = 'https://www.etm.ru/cat/nn/1827706/';
    html = geckoDriver.openPageNotSeeIt(url,browser);
    soup = BeautifulSoup(html, 'lxml')
    #take_links_from_page(soup);
    
    ans = take_data_of_product(soup)
    print(ans);
