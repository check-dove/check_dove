import time
import csv
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from time import strftime
# from os import linesep
"""
  通过”百度热词“来获取当前的实时热点，然后将其作为关键词，
  在今日头条中搜索，最后保存搜索到的内容
"""
website = ["https://www.baidu.com", "https://www.toutiao.com"]

dr = webdriver.Chrome()
dr.implicitly_wait(20)
# dr.get(website)

keywords = []
texts = []


class collectsomething(object):
    def __init__(self):
        # 百度热词提取
        dr.get(website[0])
        time.sleep(1)
        for i in range(3):
            texts = dr.find_element(By.XPATH, '//*[@id="hotsearch-content-wrapper"]/li[1+{}]/a/span[2]'.format(i))
            keywords.append(texts.text)

    def getinfo(self):
        dr.find_element(By.XPATH, '//*[@class="s-result-list"]').text

    def op2nd(self):
        dr.get(website[1])
        time.sleep(1)
        searchwin = dr.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div[1]/input')
        for i in range(len(keywords)):
            # 在进行搜索前，保证窗口为最初打开(get)的页面（即头条首页）
            dr.switch_to.window(dr.window_handles[0])
            searchwin.send_keys(keywords[i])
            dr.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div[1]/button').click()
            # 这里clear方法没起作用，发送删除来进行替代
            searchwin.send_keys('\b' * len(keywords[i]))
            # dr当前窗口，切换至最新的（即弹窗出的新的窗口）
            dr.switch_to.window(dr.window_handles[-1])
            text = dr.find_element(By.XPATH, '//*[@class="s-result-list"]').text
            texts.append(text)
            time.sleep(1)
            # 检查窗口是否是目标窗口，是的话，进行截图保存数据
            # if WebDriverWait(dr, 30, 0.5).until(EC.title_contains(u"头条搜索")):
            #     dr.save_screenshot('{}.png'.format(strftime('%y%m%d%H-%M-%S')))

    def filehandler(self, item):
        # with open('../a.txt', 'a+') as fi:
        #     fi.write(item)
        with open('../selenium_exer/datafile.csv', 'a+', newline='') as fi:
            writer = csv.writer(fi)
            try:
                writer.writerow(item)
            except:
                print("error")
        fi.close()


jinki = collectsomething()
jinki.op2nd()
jinki.filehandler(texts)
dr.quit()
