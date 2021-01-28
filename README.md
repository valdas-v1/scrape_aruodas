# Aruodas.lt Scraper
A Scraper designed to scrape Aruodas.lt apartment listing data

Aruodas.lt Scraper currently supports:
  - Scraping of apartment listings: price, build year, number of rooms...
  - Bot detection avoidance
  - Storing collected data in a Pandas DataFrame
### Upcomming Features!

  - Scraping house listings

### Tech
Aruodas.lt Scraper uses a number of open source projects to work properly:

* [Python](https://www.python.org/) - The programming language for of this project
* [Pandas](https://pandas.pydata.org/) - A fast, powerful, flexible and easy to use open source data analysis and manipulation tool
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) - Screen-scraping library
* [Pickle](https://docs.python.org/3/library/pickle.html) - Python object serialization

## Installation
* Aruodas.lt Scraper requires Python 3 to run

#### Installation as a python module:
1) Create a virtual environment
    ```sh
    $ python -m venv venv
    ```
2) Activate the virtual environment
    ```sh
    $ venv\Scripts\activate.bat
    ```
3) Install the Aruodas.lt Scraper with pip
    ```sh
    $ pip install git+https://github.com/valdas-v1/scrape_aruodas
    ```
## Usage
1) Import the package
    ```python
    from scrape_aruodas import Scraper
    ```
2) Create an instance of the Scraper
    ```python
    a = Scraper()
    ```
3) Scraping a single search page of 25 listings
    ```python
    a.scrape_aruodas(1)
    ```
4) Saving collected data in a csv
    ```python
    a.save('data')
    ```

License
----

[MIT](LICENSE)