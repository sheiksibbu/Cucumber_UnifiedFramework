import logging
import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# class OrangeHRMSteps:


# @given('the user navigates to the OrangeHRM login page')
# def navigate_to_login_page(context):
#     logo = context.driver.find_element(By.XPATH, "//div[@class='login_logo']")
#     assert logo.is_displayed(), "OrangeHRM logo not displayed."


@given('the user navigates to the OrangeHRM login page')
def navigate_to_login_page(context):
    try:

        logo = context.driver.find_element(By.XPATH, "//div[@class='login_logo']")
        assert logo.is_displayed(), "OrangeHRM logo not displayed."
        logging.info("OrangeHRM logo is displayed successfully.")

    except AssertionError as e:
        logging.error(f"Assertion error: {str(e)}")
        context.failure_reason = f"Assertion error: {str(e)}"
        raise
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        context.failure_reason = str(e).split("\n")[0]
        raise


@when('the user enters valid credentails')
def enter_valid_credentials(context):
    try:
        context.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        context.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    except Exception as e:
        context.failure_reason = str(e).split("\n")[0]
        raise


@when('clicks the Login button')
def click_login_button(context):
    try:
        context.driver.find_element(By.ID, "login-button").click()
    except Exception as e:
        # Capture the failure and raise a custom exception if needed
        # context.failure_reason = str(e)
        context.failure_reason = str(e).split("\n")[0]
        raise


@then('the user should be redirected to the home page')
def verify_home_page_redirection(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("inventory")
    )
    assert "inventory" in context.driver.current_url, "Redirection failed!"


@then('the page title should be OrangeHRM')
def verify_page_title(context):
    assert context.driver.title == "Swag Labs", "Page title mismatch."


@then('the dashboard should display OrangeHRM Logo')
def verify_dashboard_logo(context):
    logo = context.driver.find_element(By.XPATH, "//div[@class='app_logo']")
    assert logo.is_displayed(), "OrangeHRM logo not displayed."


@when('clicks the Login buttton')
def click_login_button(context):
    try:
        context.driver.find_element(By.ID, "login-butto").click()
    except Exception as e:
        # Capture the failure and raise a custom exception if needed
        # context.failure_reason = str(e)
        context.failure_reason = str(e).split("\n")[0]
        raise
