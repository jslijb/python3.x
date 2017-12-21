from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()
dr.get("https://www.rapidsold.com/login.php")
dr.find_element_by_id("username").click()
dr.find_element_by_id("username").send_keys("ljb188")
dr.find_element_by_id("password").click()
dr.find_element_by_id("password").clear()
dr.find_element_by_id("password").send_keys("Ljb19860402")