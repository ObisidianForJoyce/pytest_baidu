def test_example_title(edge_browser):
    edge_browser.get("https://www.baidu.com")
    assert "百度" in edge_browser.title