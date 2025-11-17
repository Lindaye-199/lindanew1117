import os.path

from playwright.sync_api import Page ,expect

def test_filter(page: Page):
    page.goto("http://taobao.com")
    assert page.locator('[aria-label="查看更多"]').filter(has_text="工业品").get_by_role("link").all_text_contents()[-1]=="定制"
