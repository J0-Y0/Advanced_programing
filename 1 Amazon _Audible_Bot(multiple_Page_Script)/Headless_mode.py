from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# path of the chrome driver
path = "C:\\Users\\Am jos\\Downloads\\Compressed\\chromedriver"

# Headless mode
options = Options()  # Initialize an instance of the Options class
options.headless = True  # True -> Headless mode activated
options.add_argument('window-size=1920x1080')  # Set a big window size, so all the data will be displayed

web = "https://www.audible.com/search"
driver = webdriver.Chrome(path, options=options)  # add the "options" argument to make sure the changes are applied
driver.get(web)
# driver.maximize_window()

container = driver.find_element_by_class_name('adbl-impression-container ')
products = container.find_elements_by_xpath('./li')

book_title = []
book_author = []
book_length = []

for product in products:
    # In headless mode we won't see the bot scraping the website, so print any element to check the progress
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)
driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})

df_books.to_csv('List_Of_Books headless_mode.csv', index=False)
print('____________________task completed!!__________________')