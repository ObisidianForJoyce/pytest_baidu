import logging
import re

import allure
import pytest

from page.search.search_action import SearchPage


@allure.epic('Automation Test - Baidu')
@allure.feature("Baidu - Search")
@allure.link('http://www.baidu.com')
class BD_Test_Search(object):
    @pytest.mark.skip()
    def test_search(self,browser):
        search_page = SearchPage(browser)
        search_page.input_search_content('selenium')
        search_page.click_search()
        result = re.search(r'selenium',search_page.get_source)
        logging.info(result)
        logging.info("测试输出文本！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
        assert result