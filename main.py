from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

RENTING_SITE_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL ="https://forms.gle/sBkF5Sd5sZE7pQP59"

class DataEntery :

    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach",True)

        self.driver =webdriver.Chrome(options=self.chrome_option)
        self.driver.get(url=FORM_URL)

        self.wait = WebDriverWait(self.driver,5)


    def fill_the_data(self,rent_list,link,adder_of_prop) :

        #Filling address to google form
        address_input = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        address_input.click()
        address_input.clear()
        time.sleep(1)
        address_input.send_keys(adder_of_prop)

        #Filling property link to google form
        property_link = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        property_link.click()
        property_link.clear()
        property_link.send_keys(link)
        
        #Filling rent of property to google form
        property_rent = self.wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        property_rent.click()
        property_rent.clear()
        property_rent.send_keys(rent_list)

        #Submit the form 
        submit_button = self.driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()

        #Press the resubmit link to resubmit the form
        resubmit = self.wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
        resubmit.click()

responce = requests.get(url=RENTING_SITE_URL)
web_page = responce.text
soup = BeautifulSoup(web_page,"html.parser")

all_listed_prop = soup.find_all(name="li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

address_list=[]
link_of_prop =[]
prop_rent = []

# Scraped the data from the web page store in the list
for property in all_listed_prop :

    cost = property.find(name="span").text
    link = property.find(name="a").get("href")
    address = property.find(name="address").text

    prop_rent.append(cost.split("+")[0].split("/")[0])
    address_list.append(address)
    link_of_prop.append(link)

clean_address_list = [" ".join(item.split()) for item in address_list]

#Fill the form and submit it 
data_entery =DataEntery()
for i in range(len(prop_rent)) :
    try:
        data_entery.fill_the_data(prop_rent[i],link_of_prop[i],clean_address_list[i])
    except Exception as e :
        print(f"An Error occured during filling the form.Error :{e}")
        