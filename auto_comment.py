from selenium import webdriver
import time
import pickle
import random

# https://www.douyin.com/user/MS4wLjABAAAAbon_VQY_4dB7dzuBf8Roykgr9umNW5vXhj5hEBDFzbE?enter_method=video_title&author_id=100407188539&group_id=6977211498972056835&log_pb=%7B%22impr_id%22%3A%22021628698872157fdbddc0100fff0030a1030e700000091b342ad%22%7D&enter_from=video_detail
with open("抖音cookies文件.pickle", 'rb') as file:
    cookiesList = pickle.load(file)

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.douyin.com/')
#input("请输入任意键继续...")
for cookie in cookiesList:
    browser.add_cookie(cookie)

browser.get('https://live.douyin.com/630471648476')   #直播链接地址
# https://live.douyin.com/2732898268
# https://live.douyin.com/512037658897
time.sleep(1)

from selenium.webdriver.common.by import By
muteSwitches = browser.find_elements(By.XPATH,'//*[@id="_douyin_live_scroll_container_"][@data-state="mute"]')
for muteSwitche in muteSwitches:
    print("___---" * 10)
    muteSwitche.click()

remarks = [
    '太好看了！！！',
    '在哪里可以购买？！！！',
    '为主播商品打call！！！',
    '主播好美！！！',
    '太好看了！！！',
    '很帅！！！',
    '666太美了！！！',
]
time.sleep(10)
while True:
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    browser.find_element(By.XPATH,'//*[@id="_douyin_live_scroll_container_"]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/textarea').click()
    #print(random.choice(remarks))

    browser.find_element(By.XPATH,'//*[@id="_douyin_live_scroll_container_"]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/textarea').send_keys(random.choice(remarks))
    
    #browser.find_element(By.CSS_SELECTOR,'.webcast-chatroom___textarea').send_keys(6)
    
    time.sleep(2)
    #textElement.clear()
    #textElement.send_keys(random.choice(remarks))  # 输入新字符串
    from selenium.webdriver.common.by import By
    sendElement = browser.find_element(By.XPATH,'//*[@id="_douyin_live_scroll_container_"]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/button').click()
    time.sleep(5)
    #sendElement.click()

# input("请输入任意键继续...")
browser.quit()