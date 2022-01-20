from selenium import webdriver

slider = "https://www.maoyan.com/board/4"
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")

dr.quit()
