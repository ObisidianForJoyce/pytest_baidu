from selenium.webdriver.common.by import By

from base.basePage import BasePage
import page.setting.basic_page_loc as bpl
class BasicPage(BasePage):

    #访问设置菜单
    def access_setting_view(self):
        self.wait(bpl.setting_menu, 'setting_menu_wait')
        self.click_action(bpl.setting_menu, 'setting_menu')

    #访问高级设置菜单
    def access_advanced_setting(self):
        self.wait(bpl.advanced_search_menu, 'advanced_search_menu_wait')
        self.click_action(bpl.advanced_search_menu,'search_setting_menu')

    # 关闭高级设置菜单
    def close_advanced_setting(self):
        self.wait(bpl.close_advanced,'close_advanced_wait')
        self.click_action(bpl.close_advanced,'close_advanced_click')
     #访问隐私设置菜单
    def access_privacy_setting_menu(self):
        self.wait(bpl.privacy_setting_menu,'privacy_setting_menu_wait')
        self.click_action(bpl.privacy_setting_menu,'privacy_setting_menu')
    # 访问account 下拉列表
    def access_account_view(self):
        self.wait(bpl.account_menu, 'account_menu')
        self.click_action(bpl.account_menu, 'account_menu')

    # 访问个人中心
    def access_personal_info(self):
        self.wait(bpl.personal_info, 'personal_info')
        self.click_action(bpl.personal_info, 'personal_info')

    # 访问账号设置页面
    def access_account_setting(self):
        self.wait(bpl.account_setting,'account_setting')
        self.click_action(bpl.account_setting, 'account_setting')