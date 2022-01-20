from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import csv
# import gc
# gc.collect()
# 垃圾收集器
"""
    获取猫眼电影的 TOP 100 榜单
"""
website = "https://www.maoyan.com/"
dr = webdriver.Chrome()
dr.get(website)

amount = 100  # max = 100
uptimes = []
introduces = []
scores = []
actors = []
titles = []
page_cur = 0
delimiter = '=' * 60

# 由于重定向，selenium在第一次连接猫眼的时候都是这样，再连接，就正常了，目前不清楚原因
while True:
    try:
        WebDriverWait(dr, 4, 0.5).until(ec.title_contains("猫眼电影"))
    except:
        dr.get(website)
    else:
        dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div[1]/span[1]/a').click()
        dr.switch_to.window(dr.window_handles[-1])
        break
sleep(1)


while True:
    # 获取每页电影数
    length = dr.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    # 确定需爬取的页数
    page_need = amount // len(length)
    if amount % len(length):
        page_need += 1

    if page_cur == 0:
        print('waring: 共需对{}页内容进行爬取'.format(page_need))
        print(delimiter)

    # 查看当前所在页
    pagenumb = dr.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/ul/li')
    for eachpage in pagenumb:
        if eachpage.get_attribute('class') == "active":
            page_cur = int(eachpage.text)
            print("目前正在第{}页，准备努力获取东西".format(page_cur))

    # 获取每页电影信息
    for i in range(1, len(length) + 1):
        print("-------正在加油获取第{}条内容".format(i))
        # 获取标题
        title = '//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[1]/p[1]/a'.format(i)
        title = dr.find_element_by_xpath(title).get_attribute('title')
        titles.append(title)
        # 获取演员
        actor = '//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[1]/p[2]'.format(i)
        actor = dr.find_element_by_xpath(actor).text
        actors.append(actor)
        # 获取上映时间
        uptime = '//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[1]/p[3]'.format(i)
        uptime = dr.find_element_by_xpath(uptime).text
        uptimes.append(uptime)
        # 获取评分
        score = '//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[2]/p/i'.format(i)
        score = dr.find_elements_by_xpath(score)
        score = score[0].text + score[1].text
        scores.append('评分：' + score)

    # 进入下一页:下一页按钮一般是页签行的最后一个元素（
    # 为了更强的健壮性，最后一个不是下一页的话，也可以结束采集）
    nextpage_xpath = '//*[@id="app"]/div/div/div[2]/ul/li[{}]'.format(len(pagenumb))
    nextpage = dr.find_element_by_xpath(nextpage_xpath)
    if nextpage.text == "下一页":
        nextpage.click()

    # 退出判定：当前页为需要的页数
    if page_cur == page_need:
        break
    sleep(1)

# 写入文件
with open('title.csv', 'w+', newline='', encoding='gb18030') as f:
    writor = csv.writer(f)
    # 初始化标题
    writor.writerow(('电影名', '演员', '评分', '上映时间'))
    # 传入数据
    for i in zip(titles, actors, scores, uptimes):
        writor.writerow(i)

# 结束时清场
print(delimiter)
print('收集工作完成：感谢等待，下次再会。')
f.close()
dr.quit()
