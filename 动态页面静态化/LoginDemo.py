from selenium import webdriver
import time

#定义登录方法
def login(username, password):
    driver = webdriver.Chrome()
    driver.get('https://sit.ibdp2p.com/access/login.jsp')  #登录页面
    driver.find_element_by_id('phone').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_link_text('登录').click()
    time.sleep(5)

if __name__ == '__main__':
    login('15999534925','1')