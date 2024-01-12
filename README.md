# Aruodas.lt Real Estate Listing Scraper

## Overview
The Aruodas.lt Scraper is a robust tool designed for efficiently extracting apartment listing data from Aruodas.lt. This scraper is tailored to meet the needs of data analysts and real estate professionals seeking comprehensive market insights.

### Features
- **Apartment Listings**: Extracts key details such as price, build year, and number of rooms.
- **Bot Detection Evasion**: Utilizes advanced techniques to avoid detection by website security.
- **Data Management**: Seamlessly integrates with Pandas DataFrame for efficient data handling.
- **Upcoming**: Extension to house listing scraping.

### Technologies
Built on a foundation of open-source technologies, the Aruodas.lt Scraper leverages:
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
2. **Setup Virtual Environment**:
    ```sh
    python -m venv venv
    ```
3. **Activate Virtual Environment**:
    ```sh
    venv\Scripts\activate.bat
    ```
4. **Install Requirements**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **Import the Scraper**:
    ```python
    from scrape_aruodas import Scraper
    ```
2. **Initialize Scraper**:
    ```python
    scraper = Scraper()
    ```
3. **Scrape Listings** (e.g., a single search page of 25 listings):
    ```python
    scraper.scrape_aruodas(1)
    ```
4. **Save Data to CSV**:
    ```python
    scraper.save_csv('data.csv')
    ```

## License
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](LICENSE).
