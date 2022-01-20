from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


dr = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME.copy())
website = "https://www.csdn.net"
dr.get(website)
time.sleep(1)
dr.quit()
