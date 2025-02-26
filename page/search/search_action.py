from base.basePage import BasePage
import page.search.search_loc as sp

class SearchPage(BasePage):

    def input_search_content(self,text):
        """
        input the text for searching
        :param text:
        :return:
        """
        self.clean_context(sp.search_textbox)
        self.send_keys(sp.search_textbox,text, 'send_value')

    def click_search(self):
        self.click_action(sp.search_btn,'click_search')