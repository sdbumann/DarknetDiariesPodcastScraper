import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

def scraper(base_url, min_eps_num, max_eps_num):
    # specify the range of episode numbers you want to scrape
    episode_range = range(min_eps_num, max_eps_num)

    # set up the webdriver
    driver = webdriver.Chrome()

    # loop through each episode and scrape the download link
    for episode in episode_range:
        # construct the URL for the current episode
        url = base_url + str(episode)

        # navigate to the URL and wait for the page to load
        driver.get(url)
        time.sleep(5)

        # switch to the iframe containing the episode page
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe')) 


        # find the download button element by CSS selector
        download_button = driver.find_element(By.CSS_SELECTOR, 'button.download-button')

        # click the download button
        download_button.click()
        time.sleep(2)

        # find the mp3 link element and get its href attribute
        mp3_link = driver.find_element(By.CSS_SELECTOR, 'a.download-link-mp3')
        mp3_url = mp3_link.get_attribute('href')

        # download the mp3 file for the current episode
        file_name = f"Darknet Diaries S01E{str(episode).zfill(3)}.mp3"
        urllib.request.urlretrieve(mp3_url, file_name)
        print(f"Downloaded episode {episode}: {file_name}")

    # close the webdriver
    driver.quit()

    if __name__ == '__main__':
        # specify the base URL
        base_url = 'https://darknetdiaries.com/episode/'

        scraper(base_url, 1, 2)
