from selenium import webdriver
import time
import pickle
browser = webdriver.Chrome('./chromedriver')
# 设置最大等待时长为 10秒
browser.implicitly_wait(10)
browser.get('https://www.douyin.com/')
time.sleep(1)
print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())
input("登入抖音账号后,请输入任意键继续...")

time.sleep(1)
with open("抖音cookies文件.pickle",'wb') as file:
    pickle.dump(browser.get_cookies(),file)
print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())

input("请输入任意键继续...")
browser.delete_all_cookies()
time.sleep(1)
print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())