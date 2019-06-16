from selenium import webdriver
from selenium.webdriver import ActionChains


def test_mousehoverdemo():
    driver=webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.implicitly_wait(30)
    a1=ActionChains(driver)
    category_ele = driver.find_element_by_xpath("//span[text()='Category']")
    a1.move_to_element(category_ele).perform()


