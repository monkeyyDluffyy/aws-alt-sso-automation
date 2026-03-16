from playwright.sync_api import sync_playwright
from utils.logger import get_logger

logger = get_logger()

def create_external_app(console_url, username, password, app_name):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(console_url)

        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)

        page.click('button[type="submit"]')

        page.wait_for_load_state("networkidle")

        logger.info("Logged into AWS console")

        page.goto("https://console.aws.amazon.com/singlesignon/applications")

        page.click("text=Add application")

        page.click("text=External AWS Account")

        page.fill('input[name="name"]', app_name)

        page.click("button:has-text('Create')")

        logger.info("External AWS Application Created")

        browser.close()
