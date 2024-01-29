# Aruodas.lt Real Estate Listing Scraper

## Overview
The Aruodas.lt Scraper was a robust tool designed for efficiently extracting apartment listing data from Aruodas.lt. Initially tailored for data analysts and real estate professionals seeking comprehensive market insights, this scraper served as an efficient tool for data extraction.

### Important Update
Since the development of this project, Aruodas.lt has significantly enhanced its anti-scraping measures. They have implemented advanced security features like Cloudflare protection and mandatory JavaScript execution. As a result, this version of the scraper is no longer functional. However, the HTML extraction and parsing logic remain largely unchanged, making this project a valuable example of how web scraping was previously accomplished.

For historical data and insights into Aruodas.lt's listings, visit my [Lithuanian Real Estate Listings Repository](https://github.com/valdas-v1/lithuanian-real-estate-listings).

### Features
- **Apartment Listings**: Extracted key details such as price, build year, and number of rooms.
- **Bot Detection Evasion**: Previously utilized techniques to avoid detection by website security.
- **Data Management**: Seamlessly integrated with Pandas DataFrame for efficient data handling.

### Technologies
Built on a foundation of open-source technologies, the Aruodas.lt Scraper leveraged:
- [Python](https://www.python.org/): Core programming language.
- [Pandas](https://pandas.pydata.org/): Data analysis and manipulation tool.
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/): For efficient HTML parsing.
- [Pickle](https://docs.python.org/3/library/pickle.html): Python object serialization.

## Getting Started

### Prerequisites
- Python 3

### Installation Options

#### As a Python Module:
1. **Setup Virtual Environment**:
    ```sh
    python -m venv venv
    ```
2. **Activate Virtual Environment**:
    ```sh
    venv\Scripts\activate.bat
    ```
3. **Install with pip**:
    ```sh
    pip install git+https://github.com/valdas-v1/scrape_aruodas
    ```

#### As a Standalone Script:
1. **Clone Repository**:
    ```sh
    git clone https://github.com/valdas-v1/scrape_aruodas
    ```
2. **Navigate to Directory**:
    ```sh
    cd scrape_aruodas
    ```
3. **Setup Virtual Environment**:
    ```sh
    python -m venv venv
    ```
4. **Activate Virtual Environment**:
    ```sh
    venv\Scripts\activate.bat
    ```
5. **Install Requirements**:
    ```sh
    pip install -r requirements.txt
    ```

## Contact for Current Data
If you are interested in current listing data, I have been able to circumvent Aruodas.lt's security measures and continue to scrape their website. Feel free to contact me on [LinkedIn](https://www.linkedin.com/in/valdas-paulavicius/). We can discuss potential collaborations or solutions.

## License
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](LICENSE).