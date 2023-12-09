
import selenium.webdriver.chrome.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import common as Co

# 指定時間待機
import time

from selenium.webdriver.common.by import By

#-----------------------------
#SBI証券の口座でIPOのBB申込を行なう
#-----------------------------
def inputLogin(driver:selenium.webdriver.chrome.webdriver.WebDriver, in_data):
    # サイトを開く
    driver.get("https://www.appsheet.com/start/394c45f4-6d7e-467c-9455-9a235822d36e#control=%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC&page=deck")

    #locator = (By.NAME, "ACT_login")
    #WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator))

    driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Box')]").click()

    #ログイン
    try:
        driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Boxへのアクセスを許可するにはログインしてください')]")
    except:
        return -1

    driver.find_element(by=By.ID, value="login").send_keys(in_data["g_login"])
    driver.find_element(by=By.ID, value="password").send_keys(in_data["g_pass"])
    driver.find_element(by=By.CLASS_NAME, value="login_submit_div").click()

    locator = (By.NAME, "consent_accept")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator))
    time.sleep(2)
    driver.find_element(by=By.NAME, value="consent_accept").click()

    time.sleep(5)
    locator = (By.CLASS_NAME, "input-block-level")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))
    driver.find_element(by=By.CLASS_NAME, value="input-block-level").send_keys(in_data["g_pass"])

    driver.find_element(by=By.CLASS_NAME, value="FormView__footer-saveButton").click()


    return 0
