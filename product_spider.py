import scrapy
from selenium import webdriver
import json
import re
import time


class ProductSpider(scrapy.Spider):
    name = "product_spider"
    add_to_list=[]
    def start_requests(self):
        with open(r'input_1.json', 'r', encoding='utf-8') as f:
                input = json.load(f)
        for row in input:
            company_name=row['Company']
            location_name=row['Location']
            title_name=row['Title']
            ori_company_name=company_name.lstrip()
            ori_company_name=ori_company_name.replace(" ","+")
            ori_company_name=ori_company_name.replace("&", "")
            title_name=title_name.replace(" ","+")
            title_name=title_name.replace("&", "")
            location_name=location_name.replace(" ","+")
            location_name=location_name.replace("&", "")
            google_url="https://www.google.co.in/search?q="+ori_company_name+"+in+"+location_name+"&ibp=htl;jobs";
            yield scrapy.Request(url=google_url, callback=self.parse)
         
    def __init__(self):
        self.driver =  webdriver.Chrome('D://chromedriver.exe')

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.maximize_window()
        elems=self.driver.find_elements_by_xpath("//div[contains(@class,'nsol9b hxSlV') or contains(@class, 'k8RiQ nsol9b hxSlV')]")
        i=0
        links=''
        list=[]
        listOfApplys=[]
        list_of_list=[]
        for ele in elems:
            list.append(ele.text)
            if(i==2):
                i=0
                list_of_list.append(list)
                list=[]
            else:
                i=i+1

        apply_links=self.driver.find_elements_by_xpath("//a[@class='D7VqAe LwS2ce']")
        for link in apply_links:
            tag_=link.text
            if(tag_!=''):
                listOfApplys.append(tag_)

        
        with open('out.json', 'w') as outfile:
            json.dump(listOfApplys, outfile)


        