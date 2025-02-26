from selenium.webdriver.common.by import By


# 设置
setting_menu = (By.XPATH, '//*[@id="s-usersetting-top"]')
advanced_search_menu = (By.XPATH, '//*[text()="高级搜索"]') # 高级搜索设置
close_advanced = (By.XPATH,'//*[@id="wrapper"]/div[6]/span/i')
privacy_setting_menu = (By.XPATH, '//*[text()="隐私设置"]') # 隐私设置

# 个人中心入口
account_menu = (By.XPATH, '//*[@id="s-top-username"]')
personal_info = (By.XPATH, '//*[@id="s-user-name-menu"]/a[1]') # 个人中心
account_setting = (By.XPATH, '//*[@id="s-user-name-menu"]/a[2]') # 账号设置
