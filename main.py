from getpass import getpass

from utils import *


if __name__ == "__main__":
    email = input("Email: ")
    password = getpass("Password: ")

    driver = setup_webdriver("chromedriver.exe", ["--disable-notifications"], "https://www.facebook.com/")
    login(driver, email, password)

    click_on_element(driver, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[2]/span/div")

    send_keys_to_element(driver, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/"
                                 "div/div[1]/div/div[2]/div[1]/div/div[1]/input", "Bugs Bunny")

    click_on_element(driver, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/"
                             "div[1]/div/div[2]/div[2]/div/div[1]/ul/li[1]/ul/li[1]/div/a/div/div[1]")

    send_keys_to_element(driver, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/"
                                 "div/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div/div[1]", "What's up doc?")

    click_on_element(driver, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/"
                             "div[2]/div[2]/div/div/span[2]/div")

    driver.quit()
