def test_css_selector(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("input[name='username']","student")
    page.fill("input[name='password']","Password123")
    page.click("#submit")
    assert "logged in" in page.text_content("h1").lower()

def test_xpath_selector(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("//input[@name='username']","student")
    page.fill("//input[@name='password']","Password123")
    page.click("//button[@id='submit']")
    assert "logged in" in page.text_content("h1").lower()

def test_text_selector(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("input[name='username']", "student")
    page.fill("input[name='password']", "Password123")
    page.click("text=Submit")
    assert "logged in" in page.text_content("h1").lower()

def test_role_selector(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("textbox", name="Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    assert page.text_content("h1") == "Logged In Successfully"

def test_data_attribute(page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.wait_for_selector("[placeholder='What needs to be done?']")
    page.locator("[placeholder='What needs to be done?']").fill("Learn Playwright")
