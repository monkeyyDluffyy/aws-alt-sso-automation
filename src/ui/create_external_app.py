from playwright.sync_api import sync_playwright


def create_external_app(username, password, app_name):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://eu-west-2.sso.signin.aws/platform/d-9c674bea45/login?workflowStateHandle=5e07a8b0-4d00-4423-a063-cdf16a452804")

        page.fill("input[name='username']", username)
        page.fill("input[name='password']", password)

        page.click("button[type='submit']")

        page.wait_for_load_state("networkidle")

        page.click("text=Applications")
        page.click("text=Add application")

        page.click("text=External AWS Account")

        page.fill("input[name='appName']", app_name)

        page.click("button:has-text('Create application')")

        page.wait_for_selector("text=Application created")

        browser.close()
