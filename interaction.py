from selenium import webdriver

CHROMEDRIVER_PATH = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

while True:
    cookies = driver.find_element_by_id("cookie")
    cookies.click()
    money = driver.find_element_by_id("money")
    cursor = driver.find_element_by_id("buyCursor")
    if money == "100":
        cursor.click()