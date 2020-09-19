# -*- coding: utf-8 -*-
'''
Created on 18.07.2020

@author: Sergey
'''

import csv;
import time;
#to make name with date
import datetime;


#clean file:
def clean_file():
    now = datetime.datetime.now();
    with open('result/all-{}.csv'.format((str(now.year) + '-' + str(now.month) + '-' + str(now.day))), 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';');


def write_title_csv(ans):
    now = datetime.datetime.now();
    with open('result/all-{}.csv'.format((str(now.year) + '-' + str(now.month) + '-' + str(now.day))), 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';');

        #make list of category:
        
        
        list_of_all_categoties = ['Размещение на сайте','Название','Цена минус 5%','oldPrice','Цена','discauntPrice', 'Фотографии','Описание'];
        params = ['Артикул', 'Цвет', 'Мощность (Ватт)', 'Напряжение (Вольт)', 'Цветовая температура (К)', 
     'Срок службы (Час)', 'Размеры мм (длина * толщина)', 'Модель','Цоколь'];
        for x in params:
            list_of_all_categoties.append(x);
        writer.writerow(list_of_all_categoties);
    
    
def write_dict_in_csv(ans):
    now = datetime.datetime.now();
    with open('result/all-{}.csv'.format((str(now.year) + '-' + str(now.month) + '-' + str(now.day))), 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';');
        list_of_all_data = [ans['main_category'],ans['title'],ans['prise_minus_5'],ans['oldPrice'],ans['realPrice'],ans['discauntPrice'], ans['photo'],ans['alltext']];
        #print(list_of_all_data);
        for x in ans['listParamsInfo']:
            list_of_all_data.append(x);
            
        writer.writerow(list_of_all_data);



def readCsv(csvName):
    with open(csvName, 'r', newline="", encoding='utf-8') as file:
        list = [];
        reader = csv.reader(file, delimiter=';');
        for row in reader:
            list.append(row);
        #print('ÐŸÐ¾Ð»ÑƒÑ‡Ð¸Ð»Ð¸ Ð»Ð¸Ñ�Ñ‚:',list);
    return(list);


