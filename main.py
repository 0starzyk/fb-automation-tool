from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from getpass import getpass
import time


def setup_webdriver(driver_path: str, options: list, url: str):
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


if __name__ == "__main__":
    email = input("Email: ")
    password = getpass("Password: ")

    driver = setup_webdriver("chromedriver.exe", ["--disable-notifications"], "https://www.facebook.com/")
    login(driver, email, password)

    WebDriverWait(driver, timeout=100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/"
                                                                                "div[5]/div/div[1]/div[2]/span/div")))
    message_button = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[2]/span/div")
    message_button.click()

    WebDriverWait(driver, timeout=100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/input")))
    user_search = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/"
                  "div[2]/div[1]/div/div[1]/input"
    )
    user_search.send_keys("Bugs Bunny")

    WebDriverWait(driver, timeout=100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/"
                                         "div[1]/div[1]/div/div/div/div/div/div[2]/div/"
                                         "div[1]/div/div[2]/div[2]/div/div[1]/ul/li[1]/ul/li[1]/div/a/div/div[1]")))
    user = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/"
                                         "div[1]/div[1]/div/div/div/div/div/div[2]/div/"
                                         "div[1]/div/div[2]/div[2]/div/div[1]/ul/li[1]/ul/li[1]/div/a/div/div[1]")
    user.click()

    WebDriverWait(driver, timeout=100).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/"
                                               "div[1]/div/div/div/div/div/div[2]/div/div[2]/div[2]/"
                                               "div/div/div/div[4]/div[2]/div/div/div[1]")))
    text_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/"
                                               "div[1]/div/div/div/div/div/div[2]/div/div[2]/div[2]/"
                                               "div/div/div/div[4]/div[2]/div/div/div[1]")
    text_input.send_keys("What's up doc?")

    WebDriverWait(driver, timeout=100).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/"
                                                "div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/span[2]/div")))
    send_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/"
                                                "div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/span[2]/div")
    send_button.click()

    driver.quit()
