import pytest
from playwright.sync_api import Page

def test_valid_login(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("input[name='username']","student")
    page.fill("input[name='password']","Password123")
    page.screenshot(path="screenshot1.png")
    page.click("#submit")
    assert page.title()=="Logged In Successfully"
    assert page.url()=="https://practicetestautomation.com/logged-in-successfully/"
    assert "Logged In Successfully" in page.text_content("h1")
    page.screenshot(path="screenshot2.png")

def test_invalid_username(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("input[name='username']","invalid_username")
    page.fill("input[name='password']","Password123")
    page.screenshot(path="screenshot3.png")
    page.click("#submit")
    assert "invalid" in page.text_content("#error").lower()
    page.screenshot(path="screenshot4.png")

def test_invalid_password(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("input[name='username']","student")
    page.fill("input[name='password']","invalid_password")
    page.screenshot(path="screenshot5.png")
    page.click("#submit")
    assert "invalid" in page.text_content("#error").lower()
    page.screenshot(path="screenshot6.png")

def test_empty_username(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("input[name='username']","")
    page.fill("input[name='password']","Password123")
    page.screenshot(path="screenshot7.png")
    page.click("#submit")
    assert "invalid" in page.text_content("#error").lower()
    page.screenshot(path="screenshot8.png")

def test_empty_password(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("input[name='username']","student")
    page.fill("input[name='password']","")
    page.screenshot(path="screenshot9.png")
    page.click("#submit")
    assert "invalid" in page.text_content("#error").lower()
    page.screenshot(path="screenshot10.png")
