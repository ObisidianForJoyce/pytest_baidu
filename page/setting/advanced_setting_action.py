from selenium.webdriver.common.by import By

from base.basePage import BasePage
import page.setting.advanced_setting_loc as asl
class AdvancedSettingPage(BasePage):

    #更新‘包含全部关键字’，并点击搜索
    def set_keyword_search(self, keyword):
        self.wait(asl.key_word_1, 'key_word_1')
        self.send_keys(asl.key_word_1, keyword,'update_keyword')
        self.wait(asl.advanced_btn, 'advanced_btn')
        self.click_action(asl.advanced_btn,'advanced_btn')