from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


class Data :
    
    def __init__(self,url):
        self.url = url 
        self.data = self.get_data()
        

    def get_data(self) :

        options = ChromeOptions() 
        options.add_argument("headless")
        options.add_argument('--log-level=1')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options=options)
        driver.get(self.url)
        sleep(2)

        while True :
            Load_More = driver.find_elements(By.CSS_SELECTOR ,  'button[data-disable-with="Loading more…"]' )
            if len(Load_More) > 0 :
                Load_More[0].click()
                sleep(1)
            else :
                break

        Topics = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR ,'p.f3.lh-condensed.mb-0.mt-1.Link--primary')]
        Descriptions = [ elem.text for elem in driver.find_elements(By.CSS_SELECTOR ,'p.f5.color-fg-muted.mb-0.mt-1')]
        Topics_url = [elem.get_attribute('href') for elem in  driver.find_elements(By.CSS_SELECTOR ,'a.no-underline.flex-grow-0')]
        del Topics[0]
        del Topics[1]
        del Topics[2]
        del Descriptions[0]
        del Descriptions[1]
        del Descriptions[2]

        data = {'Topics' : Topics , 'Descriptions' :Descriptions , 'Topics_url' : Topics_url}

        return data