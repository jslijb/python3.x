# coding = utf-8
from selenium import webdriver
import time

#设置Google浏览器下载的默认路径
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": "\\\\192.168.1.25\\e\\backuprds"}
chromeOptions.add_experimental_option("prefs", prefs)

dr = webdriver.Chrome(chrome_options=chromeOptions)
#dr = webdriver.Chrome()
dr.get("https://signin.aliyun.com/ibd/login.htm")
dr.find_element_by_id("user_principal_name").clear()
dr.find_element_by_id("user_principal_name").send_keys("ibd_devops@ibd")
time.sleep(3)
dr.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/div[2]/span").click()
time.sleep(3)
dr.find_element_by_id("password_ims").clear()
dr.find_element_by_id("password_ims").send_keys("9NGnGzSnYiZivLqjgs2mKF#f")
dr.find_element_by_xpath("/html/body/div[2]/div/form/div[4]/div[2]/div/input").click()
time.sleep(3)
dr.get("https://rdsnew.console.aliyun.com/#/detail/rdsip2omoeszh86mbfgcb/backupRestore/list?region=cn-shenzhen")
time.sleep(1)
dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[3]/div/div["
                         "2]/div/div/div[2]/table/tbody/tr[1]/td[8]/div/a[1]").click()
time.sleep(2)
dr.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/a").click()
