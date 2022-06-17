from selenium import webdriver
import time
import os


path = "C:\\Users\\Am jos\\Downloads\\Compressed\\chromedriver"

web = "https://twitter.com/"
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# fined login button using xpath and click it
login = driver.find_element_by_xpath('//a[@href="/login"]')
login.click()
time.sleep(2)

# finding  a  login form that contains the username and password
login_box = driver.find_element_by_xpath('//form[@action="/sessions"]')

# locating username and password inputs
username = login_box.find_element_by_xpath('.//input[@name="session[username_or_email]"]')
password = login_box.find_element_by_xpath('.//input[@name="session[password]"]')

############################################################################
        # i have filled twitter's login form with my account
        # which is already set on my environmental variable
        # NOTE ->replace it with yours to log in to your twitter account
############################################################################

username.send_keys(os.environ.get("yosfemyayu@gmail.com"))
password.send_keys(os.environ.get("myTwittPasskey"))

# find login button and then clicking on it
login_button = driver.find_element_by_xpath('//div[@role="button"]')
login_button.click()
