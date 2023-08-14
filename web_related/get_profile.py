import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_profile(__username, webpage):
    chrome = Options()
    # chrome.add_argument("--headless")
    chrome.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome)
    driver.get(f"https://www.twitter.com/{__username}")

    time.sleep(5)

    display_name = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]").text

    username = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/span").text
    try:
        about = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span").text
    except:
        about = "N/A"
    try:
        location = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span").text
    except:
        location = "N/A"

    account_date = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/span[2]/span").text

    account_date = account_date.split(" ")
    account_date = account_date[1] + account_date[2]
    account_date = datetime.datetime.strptime(account_date, "%m%Y")
    return {'display_name': display_name, 'username': username, 'about': about, 'location': location,
            'creation_date': account_date}


print(get_profile("elonmusk", "baller"))
