import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common.log_handle import logger

driver = webdriver.Chrome()

try:
    # Open browser and navigate to Login page.
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    driver.implicitly_wait(5)

    # click Login button
    WebDriverWait(driver, timeout=5, poll_frequency=0.5).until(EC.visibility_of_element_located((By.ID,'s-top-loginbtn')))
    driver.find_element(By.ID, 's-top-loginbtn').click()
    # input required fields, click Login button.
    WebDriverWait(driver, timeout=5, poll_frequency=1).until(
        EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_11__userName')))
    driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('22222111')
    driver.find_element(By.ID,'TANGRAM__PSP_11__password').send_keys('222222')
    driver.find_element(By.ID,'TANGRAM__PSP_11__isAgree').click()
    driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]').click()
    sleep(4)
    error_message = driver.find_element(By.ID,'TANGRAM__PSP_11__error').text
except Exception as e:
    logging.error('Error occurred for login action" {}'.format(e))

assert '账号或密码错误，请重新输入或者找回密码' in error_message