from playwright.sync_api import sync_playwright

def test_basic():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com")
        print(page.title())
        assert "Google" in page.title()
        browser.close()