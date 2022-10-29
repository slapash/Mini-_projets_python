from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def gecko_test(link, query):
    
    # set the driver 
    driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

    # load this article 
    driver.get(link)
    # and chill a bit
    search = driver.find_element(By.ID,'recherche')
    sleep(2)
    search.send_keys(query)
    
    search.send_keys(Keys.RETURN)
    sleep(10)

    # k, cool. let's bounce. 
    driver.quit()


# make runable 
if __name__ == '__main__':
    # here we go
    gecko_test("http://127.0.0.1:5000/handle", "funny")