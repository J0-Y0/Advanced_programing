from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

web = "https://twitter.com/ethiopia?q=ethiopia&src=typed_query"
path = "C:\\Users\\Am jos\\Downloads\\Compressed\\chromedriver"
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()


def get_tweet(element):
    try:
        user = element.find_element_by_xpath(
            ".//span[contains(text(), '@')]").text
        text = element.find_element_by_xpath(".//div[@lang]").text
        tweets_data = [user, text]
    except:
        tweets_data = ['user', 'text']
    return tweets_data


# Initializing storage
user_data = []
text_data = []

# Getting all the tweet cards/boxes listed in a single page
tweets = WebDriverWait(driver, 80).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))

# iterate through all related tweets
for tweet in tweets:
    tweet_list = get_tweet(tweet)  # calling the function get_tweet to scrape data of the tweets list
    user_data.append(tweet_list[0])  # appending the first element of tweet_list (user)
    text_data.append(" ".join(tweet_list[1].split()))  # appending the second element of tweet_list (text)

driver.quit()

# Storing the data into a DataFrame and exporting to a csv file
df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
df_tweets.to_csv('Tweets about ethiopia.csv', index=False)
print(df_tweets)
