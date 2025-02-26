from selenium.webdriver.common.by import By
import re
login_top_btn = (By.ID, 's-top-loginbtn')

# login by password
pw_switch = (By.ID, 'TANGRAM__PSP_11__changePwdCodeItem')
pw_account_input = (By.ID, 'TANGRAM__PSP_11__userName')
pw_password_input = (By.ID, 'TANGRAM__PSP_11__password')
pw_agree = (By.ID, 'TANGRAM__PSP_11__isAgree')
pw_submit_btn = (By.ID, 'TANGRAM__PSP_11__submit')
pw_error = (By.ID, 'TANGRAM__PSP_11__error')

# login by phone number
phone_switch = (By.XPATH, '//*[@id="TANGRAM__PSP_11__changeSmsCodeItem"]')
phone_number_input = (By.ID, 'TANGRAM__PSP_11__smsPhone')
phone_vc_input = (By.ID, 'TANGRAM__PSP_11__smsVerifyCode')
phone_agree = (By.ID, 'TANGRAM__PSP_11__smsIsAgree')
phone_submit_btn = (By.ID, 'TANGRAM__PSP_11__smsSubmit')
phone_error = (By.ID, 'TANGRAM__PSP_11__smsError')

# close Login
pw_close_pop = (By.ID, 'TANGRAM__PSP_4__closeBtn')




