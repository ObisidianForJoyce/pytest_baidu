import logging

from base.basePage import BasePage
import page.personal.personal_info_loc as pil

class PersonalInfoPage(BasePage):

    def clean_all_history(self):
        self.wait(pil.clean_all, 'clean_history')
        self.click_action(pil.clean_all,'clean_all')
        self.wait(pil.confirm_clean, 'confirm_clean')
        self.click_action(pil.confirm_clean,'confirm_clean')

    def get_text_of_username(self):
        self.wait(pil.username,'username')
        name = self.get_text(pil.username)
        logging.info('name......', name)
        return name