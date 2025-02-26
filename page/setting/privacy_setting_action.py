from base.basePage import BasePage
import page.setting.privacy_setting_loc as psl

class PrivacySetting(BasePage):

    def click_clean_history(self):
        self.wait(psl.clean_history, 'clean_history')
        self.click_action(psl.clean_history,'clean_history')
