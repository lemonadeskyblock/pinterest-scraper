# pinterest-scraper
A Python-based Pinterest scraper that fetches image URLs from Pinterest boards and downloads the images to your local machine. This project uses Selenium for web scraping and SQLite for storing URLs of the images.

## Features

- Scrapes image URLs from Pinterest boards.
- Downloads images to a specified folder.
- Stores image URLs in an SQLite database to avoid downloading duplicates.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/lemonadeskyblock/pinterest-scraper.git
    cd pinterest-scraper
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Install the package:

    ```sh
    pip install .
    ```

## Usage

1. Run the script using the command:

    ```sh
    scrape_board
    ```
Answer:
   - Link of the Pinterest board whose images you wish to extract: 
   - Folder path for the images, if the folder does not exist it will be creates:
   - The images would be named 'imagename_i.img', choose 'imagename': 
