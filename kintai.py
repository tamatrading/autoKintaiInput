
import selenium.webdriver.chrome.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import common as Co

# 指定時間待機
import time

from selenium.webdriver.common.by import By


def inputKintai(driver:selenium.webdriver.chrome.webdriver.WebDriver, in_data):

    #勤怠ボタン
    time.sleep(1)
    driver.find_element(by=By.ID, value="draggable_RowElement_メニュー_2").click()

    #＋ボタン
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME, value="circle-button-fab").click()

    #フォーム入力


    return 0