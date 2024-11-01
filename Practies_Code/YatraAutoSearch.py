import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Yatra_URL = "https://www.yatra.com/"
Departurefrom = "New"

def TabSwitch():

    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Yatra_URL)
        print(f'Open the URL: {Yatra_URL}')
        time.sleep(3)

        

    except Exception as e:
        print(f'Error occured at open Yatra.com error: ',e)

    try:
        
            # Auto search functionality
            # Departure_from = driver.find_element(By.CSS_SELECTOR, "div[class='MuiBox-root css-1epn4zm'] div:nth-child(1) div:nth-child(1)")
            Departure_from = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='MuiBox-root css-1epn4zm'] div:nth-child(1) div:nth-child(1)")))
            Departure_from.click()

            Input_DeparturePlace = driver.find_element(By.XPATH, "//input[@id='input-with-icon-adornment']")
            Input_DeparturePlace.send_keys(Departurefrom)
            time.sleep(3)

            # ListofCities = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/div[@class='MuiBox-root css-0']//li//div//div//div[1]")))
            ListofCities = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='MuiBox-root css-0']//li//div//div//div[1]")))

            

            # ListofCities = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-0']//li//div//div//div[1]")
            City_Name = [i.text for i in ListofCities]
            print(City_Name)

            city_names = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-0']//li//div//div//div[1]")            
            for i in city_names:
                  
                  if "New Delhi" in i.text:
                        i.click()
                        print(f'clicked on the {i.text}')

            # Airports = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-0']//li//div//div//div[2]")
            # AirportsNames = [i.text for i in Airports]

            # data = []

            # for City, Airport in zip(City_Name, AirportsNames):
            #       sub_data = [City, Airport]
            #       data.append(sub_data)
            # print(data)   

            
                
                        

    except Exception as e:
            print('error occurred at click on Departure from the error is: ', e)    

    # finally:
    #     driver.close()
    #     print('Closed the website')
    time.sleep(10)
    driver.close()


    

TabSwitch()    