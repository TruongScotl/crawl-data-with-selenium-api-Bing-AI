import time
from selenium.webdriver.common.by import By
import numpy as np
from random import randint




# this code below only work with new bing search, unfortunately it not always work
def crawl_taxcode_bing(additional_keysearch, lst, driver)->list:
    taxcode_ls = []
    for i in lst:
        driver.get('https://www.bing.com/');
        search_box = driver.find_element("name", "q")
        time.sleep(5)


        search_box.send_keys(additional_keysearch + i)
        search_box.submit()
        time.sleep(5)

        value = driver.find_element(By.CLASS_NAME,'b_focusTextLarge').text
        taxcode_ls.append(value)
    return taxcode_ls

def crawl_tax_phone(additional_keysearch, lst, driver)->list:
    taxcode_ls = []
    phone_ls = []
    for i in lst:
        driver.get('https://www.google.com/');
        search_box = driver.find_element("name", "q")
        time.sleep(randint(5,10))


        search_box.send_keys(additional_keysearch + i)
        search_box.submit()
        time.sleep(randint(5,10))

        #take first result of search google
        driver.find_element(By.CLASS_NAME, "iUh30").click()
        #time.sleep(randint(5,10))
        driver.implicitly_wait(randint(5,10))
        try:
            taxcode = driver.find_element(By.XPATH, '//*[@id="main"]/section[1]/div/table[1]/tbody/tr[3]/td[2]/span').text
            taxcode_ls.append(taxcode)
        except:
            taxcode_ls.append(np.nan)
        try:
            phone = driver.find_element(By.XPATH, '//*[@id="main"]/section[1]/div/table[1]/tbody/tr[6]/td[2]/span').text
            phone_ls.append(phone)
        except:
            phone_ls.append(np.nan)
        
    return taxcode_ls, phone_ls