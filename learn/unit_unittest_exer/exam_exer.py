import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import csv
"""
    将猫眼爬取TOP100榜单 适配为unittest用例
"""


class examle_exer(unittest.TestCase):
    def setUp(self) -> None:
        self.website = "https://www.maoyan.com/"
        self.dr = webdriver.Chrome()
        self.dr.get(self.website)

        self.amount = 100  # max = 100
        self.uptimes = []
        self.introduces = []
        self.scores = []
        self.actors = []
        self.titles = []
        self.delimiter = '=' * 60
        self.page_cur = 0

        while True:
            try:
                WebDriverWait(self.dr, 4, 0.5).until(ec.title_contains("猫眼电影"))
            except:
                self.dr.get(self.website)
            else:
                self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div[1]/span[1]/a').click()
                self.dr.switch_to.window(self.dr.window_handles[-1])
                break
        sleep(1)

    def tearDown(self) -> None:
        # 写入文件
        with open('title.csv', 'w+', newline='', encoding='gb18030') as f:
            writor = csv.writer(f)
            # 初始化标题
            writor.writerow(('电影名', '演员', '评分', '上映时间'))
            # 传入数据
            for eachitem in zip(self.titles, self.actors, self.scores, self.uptimes):
                writor.writerow(eachitem)
        print(self.delimiter)
        print('收集工作完成：感谢等待，下次再会。')
        # 关闭文件、窗口，结束采集
        f.close()
        self.dr.quit()

    def test_selenium_exer(self):
        while True:
            # 获取每页电影数
            length = self.dr.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
            # 确定需爬取的页数
            page_need = self.amount // len(length)
            if self.amount % len(length):
                page_need += 1
            if self.page_cur == 0:
                print('waring: 共需对{}页内容进行爬取'.format(page_need))
                print(self.delimiter)

            # 查看当前所在页
            pagenumb = self.dr.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/ul/li')
            for eachpage in pagenumb:
                if eachpage.get_attribute('class') == "active":
                    self.page_cur = int(eachpage.text)
                    print("目前正在第{}页，准备努力获取东西".format(self.page_cur))

            # 获取每页电影信息
            for i in range(1, len(length) + 1):
                print("-------正在加油获取第{}条内容".format(i))
                # 获取标题
                title = '//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[1]/p[1]/a'.format(i)
                title = self.dr.find_element_by_xpath(title).get_attribute('title')
                self.titles.append(title)
                # 获取演员
                actor = '//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[1]/p[2]'.format(i)
                actor = self.dr.find_element_by_xpath(actor).text
                self.actors.append(actor)
                # 获取上映时间
                uptime = '//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[1]/p[3]'.format(i)
                uptime = self.dr.find_element_by_xpath(uptime).text
                self.uptimes.append(uptime)
                # 获取评分
                score = '//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[2]/p/i'.format(i)
                score = self.dr.find_elements_by_xpath(score)
                score = score[0].text + score[1].text
                self.scores.append('评分：' + score)

            # 进入下一页:下一页按钮一般是页签行的最后一个元素（
            # 为了更强的健壮性，最后一个不是下一页的话，也可以结束采集）
            nextpage_xpath = '//*[@id="app"]/div/div/div[2]/ul/li[{}]'.format(len(pagenumb))
            nextpage = self.dr.find_element_by_xpath(nextpage_xpath)
            if nextpage.text == "下一页":
                nextpage.click()
            elif nextpage.text != "下一页":
                if self.page_cur == page_need:
                    print('已到最后一页')
                    break

            # 退出判定：当前页为需要的页数

            sleep(1)
