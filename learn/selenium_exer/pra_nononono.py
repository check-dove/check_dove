from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

website = "https://www.csdn.net"
dr = webdriver.Chrome()
dr.implicitly_wait(20)
dr.get(website)

location = (By.XPATH, '//*[@id="floor-nav_557"]/div/div/div/ul/li[1]/a')

try:
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(location))
finally:
    a = dr.find_element_by_xpath('//*[@id="floor-nav_557"]/div/div/div/ul/li[1]/a')
    print(a.get_attribute('href'))
    a.click()

sleep(5)
dr.quit()



