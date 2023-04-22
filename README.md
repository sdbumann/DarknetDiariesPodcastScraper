# Darknet Diaries Podcast Scraper
This is a Python script that scrapes all the episodes of the [Darknet Diaries](https://darknetdiaries.com/) podcast and downloads the MP3 files.

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Functionality](#functionality)
* [Functions](#functions)
* [Note](#note)
* [License](#license)
* [Contact](#contact)

<!-- REQUIREMENTS -->
## Requirements
* Python 3.x
* Selenium
* Beautiful Soup 4
* ChromeDriver

<!-- INSTALLATION -->
## Installation
1. Clone this repository to your local machine using **'git clone https://github.com/sdbumann/DarknetDiariesPodcastScraper'**.
2. Navigate into the directory: **'cd Darknet Diaries Podcast Scraper'**.
3. Install the required packages by running **'pip install -r requirements.txt'**
(or alternatively 'python setup.py' -> Note that for this the 'conda' package manger might be needed).

<!-- USAGE -->
## Usage
1. Navigate to the directory where you cloned this repository in your terminal.
2. Run the script: **'python scraper.py [ARGUMENT]'**.
3. Listen and enjoy podcast.

The script takes an optional argument:

latest: Downloads only the latest missing episode.
* **'all'**: Downloads all episodes.
* **'range min_episode max_episode'**: Downloads episodes within the specified range.
* **'missing'**: Downloads only the missing episodes.
* **'help'**: Displays usage instructions.
If no argument is specified, the script displays the usage instructions.

The script will begin downloading the MP3 files to a folder called **'downloads'** in the current working directory. If the folder does not exist, the script will create one.
Note that it is also possible to change the folder and path.

<!-- FUNCTIONALITY -->
## Functionality
This script uses the **Selenium** and **Beautiful** Soup packages to scrape the Darknet Diaries website. These packages will be installed automatically when you run **'pip install -r requirements.txt'**.

<!-- FUNCTIONS -->
## Functions
The following functions are defined in the script:

**'scraper(base_url, downloads_folder, episode_numbers)'**'
Scrapes the episodes with the specified episode numbers from the specified base URL and downloads them to the specified downloads folder.

* **'base_url (str)'**: The base URL of the Darknet Diaries podcast.
* **'downloads_folder (str)'**: The path of the downloads folder.
* **'episode_numbers (list)'**: A list of episode numbers to scrape.

**'get_latest_episode(base_url)'**'
Gets the latest episode number from the specified base URL.

* **'base_url (str)'**: The base URL of the Darknet Diaries podcast.

**'get_episode_numbers(downloads_folder)'**'
Gets a list of episode numbers that have already been downloaded from the specified downloads folder.

* **'downloads_folder (str)'**: The path of the downloads folder.

**'get_next_episode_number(downloads_folder)'**'
Gets the next episode number to download from the specified downloads folder.

* **'downloads_folder (str)'**': The path of the downloads folder.

**'get_list_of_all_latest_missing_episodes(downloads_folder, max_eps_num)'**'
Gets a list of the latest missing episodes from the specified downloads folder and the maximum episode number.

* **'downloads_folder (str)'**: The path of the downloads folder.
* **'max_eps_num (int)'**: The maximum episode number.

**'get_list_of_all_missing_episodes(downloads_folder, all_episodes)'**'
Gets a list of all missing episodes from the specified downloads folder and a list of all available episodes.

* **'downloads_folder (str)'**: The path of the downloads folder.
* **'all_episodes (list)'**: A list of all available episodes.

<!-- NOTE -->
## Note
If you find any bugs or issues with this script, please feel free to open an issue or submit a pull request.

<!-- LICENSE -->
## License
This project is licensed under the MIT License.

<!-- CONTACT -->
## Contact
[SDBumann](https://github.com/sdbumann)

<br>
Project Link: https://github.com/sdbumann/DarknetDiariesPodcastScraper
