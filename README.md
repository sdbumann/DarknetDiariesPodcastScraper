# Darknet Diaries Podcast Scraper
This is a Python script that scrapes all the episodes of the [Darknet Diaries](https://darknetdiaries.com/) podcast and downloads the MP3 files.

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usuage)
* [Functionality](#functionality)
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
2. Install the required packages by running **'pip install -r requirements.txt'**.

<!-- USAGE -->
## Usage
1. Navigate to the directory where you cloned this repository in your terminal.
2. Run the script by executing **'python scraper.py'**.

The script will begin downloading the MP3 files for each episode to a folder called **'downloads'** in the current working directory. If the folder does not exist, the script will create one.

<!-- FUNCTIONALITY -->
## Functionality
This script uses the **Selenium** and **Beautiful** Soup packages to scrape the Darknet Diaries website. These packages will be installed automatically when you run **'pip install -r requirements.txt'**. The script also uses the **'urllib.request.urlretrieve'** function to download the MP3 files.

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
