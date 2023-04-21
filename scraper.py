import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request

def scraper(base_url, downloads_folder, min_eps_num, max_eps_num):
    """
    This function scrapes all the podcast episodes of the podcast Darknet Diaries from the website given by base_url.
    It downloads each episode's MP4 file and saves it in a folder specified by downloads_folder in the current working directory.
    
    Args:
    base_url: A string representing the base URL of the Darknet Diaries website.
    downloads_folder: A string representing the path to the 'downloads' folder.
    min_eps_num: An integer representing the minimum episode number to scrape.
    max_eps_num: An integer representing the maximum episode number to scrape.

    Returns:
    -
    """

    # specify the range of episode numbers you want to scrape
    if min_eps_num == max_eps_num:
        episode_range = [min_eps_num]
    else:
        episode_range = range(min_eps_num, max_eps_num)
    print(episode_range)

    # set up the webdriver
    driver = webdriver.Chrome()

    # loop through each episode and scrape the download link
    for episode in episode_range:
        print(f"Scraping episode {episode}...")
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
        mp3_filename = f"Darknet Diaries S01E{str(episode).zfill(3)}.mp3"
        mp3_path = os.path.join(downloads_folder, mp3_filename)
        urllib.request.urlretrieve(mp3_url, mp3_path)
        print(f"Downloaded episode {episode}: {mp3_filename}")

    # close the webdriver
    driver.quit()

def get_next_episode_number(downloads_folder):
    """
    This function reads the names of all the files in the 'downloads' folder and returns the next highest episode
    number that does not already exist in the folder. If there are no files in the folder, it returns 1.

    Args:
    downloads_folder: A string representing the path to the 'downloads' folder.

    Returns:
    An integer representing the next highest episode number that does not already exist in the 'downloads' folder.
    """

    episode_numbers = []
    for filename in os.listdir(downloads_folder):
        if filename.endswith(".mp3") and filename.startswith("Darknet Diaries S01E"):
            episode_numbers.append(int(filename[len('Darknet Diaries S01E'):-len('.mp4')]))

    if not episode_numbers:
        return 1

    episode_numbers.sort()
    return episode_numbers[-1] + 1

def get_latest_episode(base_url):
    """
    This function navigates to the Darknet Diaries website and finds the episode number of the latest episode by looking
    at the href of the first "post__title" class element. It then returns an integer representing the episode number. If
    there is an error in accessing the website or finding the latest episode number, the function will return None.

    Args:
    base_url: A string representing the base URL of the Darknet Diaries website.

    Returns:
    An integer representing the episode number of the latest episode on the Darknet Diaries website, or None if there
    was an error in accessing the website or finding the latest episode number.
    """

    html = urllib.request.urlopen(base_url)
    soup = BeautifulSoup(html, 'html.parser')
    post_titles = soup.select('.post__title a')
    latest_episode = 0
    for post_title in post_titles:
        href = post_title['href']
        if '/episode/' in href:
            episode_number = int(href.split('/episode/')[1].strip('/'))
            if episode_number > latest_episode:
                latest_episode = episode_number
    return latest_episode

if __name__ == '__main__':
    # specify the base URL
    base_url = 'https://darknetdiaries.com/episode/'
    downloads_folder = 'downloads'

    # create the downloads directory if it doesn't exist
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)

    # get the minimum episode number to scrape by looking at the already downloaded episodes
    min_eps_num = get_next_episode_number(downloads_folder)
    print("Last downloaded episode: " + str(min_eps_num - 1).zfill(3) if str(min_eps_num - 1).zfill(3)!= '000' else "No episodes downloaded yet")
    print("Next episode to download: " + str(min_eps_num).zfill(3))

    # get latest episode number
    max_eps_num = get_latest_episode(base_url)
    print("Latest available episode: " + str(max_eps_num).zfill(3))

    # scrape the episodes
    if min_eps_num <= max_eps_num:
        print(f'Scraping episodes {str(min_eps_num).zfill(3)} to {str(max_eps_num).zfill(3)}')
        scraper(base_url, downloads_folder, min_eps_num, max_eps_num)
    else:
        print('No new episodes to scrape.')
