import time
import numpy as np


def crawl_fanpage(additional_keysearch, lst, driver)->list:
    """
    input: additional key search + name company, example: fanpage facebook + name company
            list of company
    output: list of link fanpage company
    """
    ls_page = []
    for i in lst:
        driver.get('https://www.google.com/');
        search_box = driver.find_element("name", "q")
        time.sleep(5)


        search_box.send_keys(additional_keysearch+i)
        search_box.submit()
        time.sleep(5)
        try:
            value = driver.find_element("xpath",'//*[@id="rso"]/div[1]/div/div/div[1]/div/a').get_attribute('href')
            ls_page.append(value)
        except Exception:
            try:
                value = driver.find_element("xpath",'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a').get_attribute('href')
                ls_page.append(value)
            except:
                ls_page.append(np.nan)
        
    return ls_page


def crawl_linkedin(additinal_keysearch, lst, driver)->list:
    ls_link = []
    for i in lst:
        driver.get('https://www.google.com/');
        search_box = driver.find_element("name", "q")
        time.sleep(5)


        search_box.send_keys(additinal_keysearch +i)
        search_box.submit()
        time.sleep(5)
        try:
            value = driver.find_element("xpath",'//*[@id="rso"]/div[1]/div/div/div[1]/div/a').get_attribute('href')
            if "linkedin" in value:
                ls_link.append(value)
            else:
                ls_link.append(np.nan)
        except Exception:
            try:
                value = driver.find_element("xpath",'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a').get_attribute('href')
                if "linkedin" in value:
                    ls_link.append(value)
                else:
                    ls_link.append(np.nan)
            except:
                ls_link.append(np.nan)
    return ls_link
