from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import timedelta, date
from itertools import repeat
from random import randint
from statistics import mean
import datetime, calendar, sys
from pyvirtualdisplay import Display
import time

def Daterange(start_date, end_date):
   for n in range(int ((end_date - start_date).days)):
       yield start_date + timedelta(n)

def Average(lst): 
    return sum(lst) / len(lst) 

def Scrapping(start_date, end_date, traveler, room_reference):
   ##------------------------ changes in this part only --------------------------------- ##
   numb = 0
   link = 'https://fr.airbnb.ca/rooms/{3}?check_in={0}&adults={2}&check_out={1}'.format(start_date, end_date, traveler, room_reference)
   #~ print(link)
   driver.get(link)
   res = driver.execute_script("return document.documentElement.outerHTML")
   soup = BeautifulSoup(res, 'lxml')
   price = soup.find('span', {'class': '_doc79r'})
   if price == None:
     while price == None and numb < 3 :
      driver.get(link)
      res = driver.execute_script("return document.documentElement.outerHTML")
      soup = BeautifulSoup(res, 'lxml')
      price = soup.find('span', {'class': '_doc79r'})
      numb += 1
      time.sleep(1)
      # print("%s, %s"% (price, numb))
     if price != None:
      price = price.text.replace('\n', '')
      return price
   else :
     price = price.text.replace('\n', '')
     return price
   
   
   # return price


if __name__ == "__main__":
    display = Display(visible=0, size=(800, 600))
    display.start()
    driverLocation = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(driverLocation)
    traveler = sys.argv[1] #2
    room_reference = sys.argv[2] #16389574
    
    datetime.datetime.now().strftime("%Y-%m-%d")
    year = int(datetime.datetime.now().strftime("%Y"))
    month = int(datetime.datetime.now().strftime("%m"))
    day = int(datetime.datetime.now().strftime("%d"))

    start_date_all = date(year, month, day)
    end_date_all = date(year+1, month, day)
    list_months = [[] for i in repeat(None, 12)]
    result = []
    print ("begin ...")
    for single_date in Daterange(start_date_all, end_date_all):
       
       month_name = calendar.month_name[single_date.month]
      
       start_date = single_date
       end_date = start_date + timedelta(1)
       print(start_date, end_date)
       day_price_str = Scrapping(start_date, end_date, traveler, room_reference)
       print ("price is %s" % day_price_str)
       if day_price_str != None:
        day_price = int(day_price_str[1:])
       else:
        day_price = None
       # print(day_price)
       with open('daily_output.txt', 'a') as f:
        f.write("%s, %s\n" % (single_date, day_price))
       

       
       # used for test 
       # day_price = randint(10, 90)


    #    list_months[single_date.month-1].append(day_price)

    # [result.append(Average(x)) for x in list_months]

    driver.quit()
    display.stop()
    # with open('output.txt', 'a') as f:
    #    f.write("%s,%s,%s\n" % (room_reference, traveler, result))
