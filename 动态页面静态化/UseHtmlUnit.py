from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Remote
import time

dc = {'browseName':'htmlUnit'}

#driver = Remote(command_executor='',desired_capabilities=dc)

browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)
browser.get("https://sit.ibdp2p.com/invest/creditInfo.action?creditId=19815") # Load page

time.sleep(5)
print(browser.page_source)