from selenium import webdriver  
import pandas as pd
import asyncio
from selenium.webdriver.chrome.options import Options
import pickle
import numpy as np

from crawl_fanpage_linkedin import crawl_fanpage, crawl_linkedin
from crawl_tax_phone import crawl_tax_phone
from crawl_email import crawl_email 
from utils import read_data, extract_email, check_email
from geocoding import geocode



andress_list = read_data('data.csv', 'address')
#get latitude, longtitude
ls_lat = [] #latitude
ls_lng = [] #longtitude
for i in andress_list:
    geo = geocode(i)
    ls_lat.append(geo["lat"])
    ls_lng.append(geo["lng"])
df_lat_lng = pd.DataFrame({'latitude':ls_lat, 'longtitude':ls_lng})
df_lat_lng.to_csv(r'lat_lng.csv', index = False, header=True)

driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
path = 'data.csv'
driver.get("http://www.google.com")
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

    
#get fanpage, linkedin, tax, phone

lst = read_data(path, 'company_name')

fanpage = crawl_fanpage("fanpage facebook ", lst, driver)
linkedin = crawl_linkedin("linkedin + ", lst, driver)
tax, phone = crawl_tax_phone("masothue.com + ", lst, driver)



driver.close()


#get email company
def ls_email(lst):
    ls_email_1 = []
    ls_email_2 = []
    for i in lst:
        value = list(set(extract_email(asyncio.run(crawl_email(i)))))
        print(type(value))
        try:
            ls_email_1.append(str(value[0]))
        except IndexError:
            ls_email_1.append(str(np.nan))
        try:
            ls_email_2.append(str(value[1]))
        except IndexError:
            ls_email_2.append(str(np.nan))
    return ls_email_1, ls_email_2

def check_valid(lst1, ls2):
    is_valid_1 = []
    is_valid_2 = []
    for i in lst1:
        is_valid_1.append(check_email(i))
    for j in ls2:
        is_valid_2.append(check_email(j))
    return is_valid_1, is_valid_2

ls_email_1, ls_email_2 = ls_email(lst)
is_valid_1, is_valid_2 = check_valid(ls_email_1, ls_email_2)


df = pd.DataFrame({'masothue': tax, 'email': ls_email_1, 'is_email_valid': is_valid_1, 'email_2': ls_email_2, 'is_email_2_valid': is_valid_2, 
                  'phone': phone, 'latitude':ls_lat,'longitude':ls_lng, 'fanpage': fanpage,'Linkedin': linkedin})  

df.to_csv (r'after_crawl.csv', index = False, header=True)


