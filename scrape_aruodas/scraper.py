from bs4 import BeautifulSoup
import requests
import pandas as pd

pd.options.mode.chained_assignment = None
import pickle
import re
import time


class Scraper:
    """A Scraper designed to scrape Aruodas.lt apartment listing data
    More info at: https://github.com/valdas-v1/scrape_aruodas
    """

    def __init__(self):
        # Placeholder DataFrame to hold scraped data
        self.df = pd.DataFrame()

    def get_soup(self, url: str) -> BeautifulSoup:
        """Returns BeautifulSoup object of the URL

        Args:
            url (str): The URL of the page

        Returns:
            BeautifulSoup (object): BeautifulSoup object of the URL
        """

        time.sleep(1.26)

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5",
        }
        response = requests.get(url, headers=headers)

        # Checks the response, if not OK, prints the error code
        if not response.ok:
            print(f"Server response: {response.status_code}")
        else:
            return BeautifulSoup(response.text, "html.parser")

    def extract_info(self, soup: BeautifulSoup):
        """Takes BeautifulSoup object and extracts aparment data. Appends the extracted data to the main DataFrame

        Args:
            soup (BeautifulSoup): Beautiful soup object of the aparment listing
        """

        try:
            # Aparment data is listed in a dl
            info = soup.find_all("dl")

            # Placeholder DataFrame to hold aparment data. Matches data tags with data
            flat_info = pd.DataFrame()
            cleaned_key = []
            for i in info[0].find_all("dt"):
                cleaned_key.append(i.text.strip())

            cleaned_value = []
            for i in info[0].find_all("dd"):
                cleaned_value.append(i.text.strip())

            flat_info["key"] = cleaned_key
            flat_info["value"] = cleaned_value

            clean_df = flat_info.pivot_table(
                values="value", columns="key", aggfunc="first"
            )

            # Setting a filter for the desired data
            required_data = [
                "Area",
                "Build year",
                "Building type",
                "Equipment",
                "Floor",
                "Heating system",
                "No. of floors",
                "Number of rooms",
            ]

            clean_df = clean_df.filter(required_data)

            # Cleaning up data with regex
            clean_df["Area"] = clean_df["Area"].str.findall(r"(\d+)")
            clean_df["Area"] = ".".join(clean_df["Area"].iloc[0])

            clean_df["Build year"] = clean_df["Build year"].str.findall(r"(\d+)")

            # Cheking if aparment has been renovated, if not, setting the renovation date to 0
            clean_df["Renovation year"] = 0
            if len(clean_df["Build year"].iloc[0]) == 2:
                clean_df["Renovation year"].iloc[0] = clean_df["Build year"].iloc[0][1]
                clean_df["Build year"].iloc[0] = clean_df["Build year"].iloc[0][0]
            else:
                clean_df["Build year"].iloc[0] = clean_df["Build year"].iloc[0][0]

            # Extracting the price
            price = soup.find("span", class_="main-price")
            price = re.findall("\d+", price.text)
            clean_df["price"] = "".join(price)

            # Extracting and parsing the address
            address = soup.find("h1")
            address = address.text.split(",")

            clean_df["city"] = address[0].strip()
            clean_df["region"] = address[1].strip()

            if len(address) > 2:
                clean_df["street"] = address[2].strip()
            else:
                clean_df["street"] = clean_df["region"]
                clean_df["region"] = 'None'

            self.df = self.df.append(clean_df, ignore_index=True)
        except:
            print("Could not extract data, check url")

    def scrape_aruodas(self, pages: int) -> pd.DataFrame:
        """Iterates through search results, scraping every listing in the page

        Args:
            pages (int): How many search pages to scrape (there are 25 listings on each page)

        Returns:
            DataFrame (object): DataFrame of the scraped data
        """
        for page in range(pages):
            print(f"Scraping page {page+1}/{pages}")
            search = self.get_soup(f"https://m.en.aruodas.lt/butai/puslapis/{page}/")
            search = search.find_all("a", class_="object-image-link")

            for link in search:
                print(f'Currently scraping: https://m.en.aruodas.lt{link["href"]}')
                flat = self.get_soup(f'https://m.en.aruodas.lt{link["href"]}')

                self.extract_info(flat)

        return self.df

    def save(self, name: str):
        """Saves collected data from scraping to csv with the specified name

        Args:
            name (str): Name of the csv
        """

        self.df.to_csv(f"{name}.csv", index=False)
