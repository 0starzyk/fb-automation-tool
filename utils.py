from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec


def setup_webdriver(driver_path: str, options: list[str], url: str):
    service = Service(executable_path=driver_path)
    chrome_options = webdriver.ChromeOptions()
    for option in options:
        chrome_options.add_argument(option)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    return driver


def login(driver, email: str, password: str):
    cookies_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[1]")
    cookies_button.click()
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(email)
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(password)
    submit_button = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    submit_button.click()


def click_on_element(driver, element_xpath: str):
    WebDriverWait(driver, timeout=100).until(ec.element_to_be_clickable((By.XPATH, element_xpath)))
    driver.find_element(By.XPATH, element_xpath).click()


def send_keys_to_element(driver, element_xpath: str, content: str):
    WebDriverWait(driver, timeout=100).until(ec.element_to_be_clickable((By.XPATH, element_xpath)))
    driver.find_element(By.XPATH, element_xpath).send_keys(content)
