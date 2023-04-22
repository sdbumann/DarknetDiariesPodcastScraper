import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request

def scraper(base_url, downloads_folder, episode_to_download):
    """
    This function scrapes all the podcast episodes of the podcast Darknet Diaries from the website given by base_url.
    It downloads each episode's MP4 file and saves it in a folder specified by downloads_folder in the current working directory.
    
    Args:
    base_url: A string representing the base URL of the Darknet Diaries website.
    downloads_folder: A string representing the path to the 'downloads' folder.
    episode_to_download: A list of episode numbers to download

    Returns:
    -
    """

    # set up the webdriver
    driver = webdriver.Chrome()

    # loop through each episode and scrape the download link
    for episode in episode_to_download:
        print(f"Scraping episode {episode}...")
        # construct the URL for the current episode
        url = base_url + str(episode)

        # navigate to the URL and wait for the page to load
        driver.get(url)
        time.sleep(5)

        # switch to the iframe containing the episode page
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe')) 

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

def get_episode_numbers(downloads_folder):
    """
    This function reads the names of all the files in the 'downloads' folder and returns a list of all episodes that exist. 
    If there are no files in the folder, it returns [].

    Args:
    downloads_folder: A string representing the path to the 'downloads' folder.

    Returns:
    A sorted list of episode numbers that exist in the 'downloads' folder
    """

    episode_numbers = []
    for filename in os.listdir(downloads_folder):
        if filename.endswith(".mp3") and filename.startswith("Darknet Diaries S01E"):
            episode_numbers.append(int(filename[len('Darknet Diaries S01E'):-len('.mp4')]))

    if not episode_numbers:
        return []

    episode_numbers.sort()
    return episode_numbers

def get_next_episode_number(downloads_folder):
    """
    This function reads the names of all the files in the 'downloads' folder and returns the next highest episode
    number that does not already exist in the folder. If there are no files in the folder, it returns 1.

    Args:
    downloads_folder: A string representing the path to the 'downloads' folder.

    Returns:
    An integer representing the next highest episode number that does not already exist in the 'downloads' folder.
    """

    episode_numbers = get_episode_numbers(downloads_folder)
    if not episode_numbers:
        return 1
    
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

def get_list_of_all_latest_missing_episodes(downloads_folder, max_eps_num):
    """
    This function retrieves the episode numbers of all the missing episodes between the last downloaded episode and the latest available episode. 
    It first determines the last downloaded episode by checking the files in the "downloads" folder, 
    then it determines the latest available episode by scraping the podcast website. 
    Finally, it returns a list of all the missing episodes between these two numbers.

    Args:
    downloads_folder: A string representing the path to the 'downloads' folder.
    max_eps_num: An integer representing the latest episode number available on the podcast website.

    Returns:
    episode_to_download: A list of all the missing episodes between the last downloaded episode and the latest available episode.
    """

    # get the minimum episode number to scrape by looking at the already downloaded episodes
    min_eps_num = get_next_episode_number(downloads_folder)
    print("Last downloaded episode: " + str(min_eps_num - 1).zfill(3) if str(min_eps_num - 1).zfill(3)!= '000' else "No episodes downloaded yet")
    print("Next episode to download: " + str(min_eps_num).zfill(3))

    # specify the range of episode numbers you want to scrape
    if min_eps_num == max_eps_num:
        episode_to_download = [min_eps_num]
    elif min_eps_num < max_eps_num:
        episode_to_download = list(range(min_eps_num, max_eps_num))
    else:
        episode_to_download = []

    print("Episodes to download: " + str(episode_to_download))

    return episode_to_download

def get_list_of_all_missing_episodes(downloads_folder, all_episodes):
    """
    This function takes in two arguments: downloads_folder, which is the path to the folder containing already downloaded episodes, 
    and all_episodes, which is a list of all available episode numbers. The function uses the get_episode_numbers function to 
    retrieve the episode numbers of already downloaded episodes. It then generates a list of all missing episode numbers by 
    comparing the list of all available episodes with the list of downloaded episodes. The missing episodes are returned as a list.

    Args:
    downloads_folder: A string representing the path to the 'downloads' folder.
    all_episodes: A list of all available episode numbers.

    Returns:
    episode_to_download: A list of all missing episodes.
    """

    episode_numbers = get_episode_numbers(downloads_folder)
    episode_to_download = [x for x in all_episodes if x not in episode_numbers]

    return episode_to_download

if __name__ == '__main__':
    # specify the base URL
    base_url = 'https://darknetdiaries.com/episode/'
    downloads_folder = 'downloads'

    # create the downloads directory if it doesn't exist
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)

    # get latest episode number
    max_eps_num = get_latest_episode(base_url)
    print("Latest available episode: " + str(max_eps_num).zfill(3))

    # list of all episodes
    all_episodes = list(range(1,max_eps_num))

    # check if the user has passed an argument to only download the latest missing episodes
    episode_to_download=[]
    if len(sys.argv) > 1 and sys.argv[1] == 'latest':
        print("Getting list of latest missing episodes...")
        episode_to_download = get_list_of_all_latest_missing_episodes(downloads_folder, max_eps_num)
    elif len(sys.argv) > 1 and sys.argv[1] == 'all':
        print("Getting list of all episodes...")
        episode_to_download = all_episodes
    elif len(sys.argv) > 1 and sys.argv[1] == 'missing':
        print("Getting list of missing episodes...")
        episode_to_download = get_list_of_all_missing_episodes(downloads_folder, all_episodes)
    elif len(sys.argv) > 3 and sys.argv[1] == 'range':
        print("Getting list of episodes in range...")
        # check if the range is valid
        if int(sys.argv[2]) > int(sys.argv[3]) or int(sys.argv[2]) < 1 or int(sys.argv[3]) < 1 or int(sys.argv[3]) > max_eps_num:
            print("Invalid range. Exiting...")
            sys.exit()
        else:
            episode_to_download = list(range(int(sys.argv[2]),int(sys.argv[3])))
    elif len(sys.argv) > 1 and sys.argv[1] == 'help':
        print('Please specify an argument: "latest", "all", "range min_episode max_episode", "missing"')
        print('Example: python3 darknet_diaries.py latest')
        print('Example: python3 darknet_diaries.py all')
        print('Example: python3 darknet_diaries.py range 1 10')
        print('Example: python3 darknet_diaries.py missing')
        print('Exiting...')
    else:
        print('Please specify an argument: "latest", "all", "range min_episode max_episode", "missing"')
        print('Example: python3 darknet_diaries.py latest')
        print('Example: python3 darknet_diaries.py all')
        print('Example: python3 darknet_diaries.py range 1 10')
        print('Example: python3 darknet_diaries.py missing')
        print('Exiting...')

    # scrape the episodes
    if not episode_to_download:
        print('Nothing to scrape.')
    else:
        print(f'Scraping episodes {episode_to_download}...')
        scraper(base_url, downloads_folder, episode_to_download)
