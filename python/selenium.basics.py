from selenium import webdriver 
import time

driver = webdriver.Chrome()

url =   "https://chatgpt.com/"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("ekran görüntüsü.png")

url = "https://www.youtube.com/"
driver.get(url)

print(driver.title)


time.sleep(2)

driver.back()

time.sleep(2)
driver.close()