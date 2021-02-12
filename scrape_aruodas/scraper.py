from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle
import re
import time

# Disable Pandas error code
pd.options.mode.chained_assignment = None


class Scraper:
    """A Scraper designed to scrape Aruodas.lt apartment listing data
    More info at: https://github.com/valdas-v1/scrape_aruodas
    """

    def __init__(self):
        # Placeholder DataFrame to hold scraped data
        self.df = pd.DataFrame()

        # Hedear for making requests
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5",
        }

    def __sleep(self) -> None:
        """Sleeps for 1.26 seconds to avoid getting flagged as a bot and get a captcha"""
        time.sleep(1.26)

    def get_response(self, url: str) -> requests.Response:
        """Returns get response from url

        Args:
            url (str): url to request

        Returns:
            requests.Response: Get response
        """
        self.__sleep()
        return requests.get(url, headers=self.headers)

    def get_soup(self, response: requests.Response) -> BeautifulSoup:
        """Returns BeautifulSoup object of the response if response is OK

        Args:
            response: (requests.Response): Get response

        Returns:
            BeautifulSoup (object): BeautifulSoup object of the URL
        """

        # Checks the response, if OK, prints the error code
        if response.ok:
            return BeautifulSoup(response.text, "html.parser")
        else:
            print(f"Server response: {response.status_code}")

    def extract_apartment_data(self, soup: BeautifulSoup) -> pd.DataFrame():
        """Extracts data about an apartment from listing soup

        Args:
            BeautifulSoup (object): BeautifulSoup object of the listing

        Returns:
            df (pd.DataFrame): Aparment data DataFrame
        """

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

        df = flat_info.pivot_table(values="value", columns="key", aggfunc="first")

        return df

    def filter_apartment_data(self, df: pd.DataFrame) -> pd.DataFrame():
        """Filters required listing data from scraped data about an apartment

        Args:
            df (pd.DataFrame): DataFrame to be filtered

        Returns:
            pd.DataFrame: Filtered DataFrame
        """

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

        return df.filter(required_data)

    def clean_apartment_data(self, clean_df: pd.DataFrame) -> pd.DataFrame():
        """Cleans apartment data with regex

        Args:
            df (pd.DataFrame): DataFrame to be cleaned

        Returns:
            pd.DataFrame: Cleaned DataFrame
        """

        clean_df["Area"] = clean_df["Area"].str.findall(r"(\d+)")
        clean_df["Area"] = ".".join(clean_df["Area"].iloc[0])

        clean_df["Build year"] = clean_df["Build year"].str.findall(r"(\d+)")

        return clean_df

    def check_if_renovated(self, clean_df: pd.DataFrame) -> pd.DataFrame():
        """Cheking if aparment has been renovated, if not, setting the renovation date to 0

        Args:
            clean_df (pd.DataFrame): Apartment data to be checked

        Returns:
            pd.DataFrame: Clean DataFrame with column for renovation
        """

        clean_df["Renovation year"] = 0
        if len(clean_df["Build year"].iloc[0]) == 2:
            clean_df["Renovation year"].iloc[0] = clean_df["Build year"].iloc[0][1]
            clean_df["Build year"].iloc[0] = clean_df["Build year"].iloc[0][0]
        else:
            clean_df["Build year"].iloc[0] = clean_df["Build year"].iloc[0][0]

        return clean_df

    def extract_price(self, soup: BeautifulSoup) -> str:
        """Extract the price of the apartment

        Args:
            soup (BeautifulSoup): Beautiful soup object of the aparment listing

        Returns:
            price (str): Price of the apartment
        """

        price = soup.find("span", class_="main-price")
        price = re.findall("\d+", price.text)
        price = "".join(price)

        return price

    def extract_address(self, soup: BeautifulSoup) -> str:
        """Extract the address of the apartment

        Args:
            soup (BeautifulSoup): Beautiful soup object of the aparment listing

        Returns:
            address (str): Address of the apartment
        """

        address = soup.find("h1")
        address = address.text.split(",")

        return address

    def extract_info(self, soup: BeautifulSoup) -> None:
        """Takes BeautifulSoup object and extracts aparment data. Appends the extracted data to the main DataFrame

        Args:
            soup (BeautifulSoup): Beautiful soup object of the aparment listing
        """

        try:
            df = self.extract_apartment_data(soup)

            filtered_df = self.filter_apartment_data(df)

            clean_df = self.clean_apartment_data(filtered_df)

            clean_df = self.check_if_renovated(clean_df)

            clean_df["price"] = self.extract_price(soup)

            address = self.extract_address(soup)
            clean_df["city"] = address[0].strip()
            clean_df["region"] = address[1].strip()

            if len(address) > 2:
                clean_df["street"] = address[2].strip()
            else:
                clean_df["street"] = clean_df["region"]
                clean_df["region"] = "None"

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
            search = self.get_soup(
                self.get_response(f"https://m.en.aruodas.lt/butai/puslapis/{page}/")
            )
            search = search.find_all("a", class_="object-image-link")

            for link in search:
                print(f'Currently scraping: https://m.en.aruodas.lt{link["href"]}')
                flat = self.get_soup(
                    self.get_response(f'https://m.en.aruodas.lt{link["href"]}')
                )

                self.extract_info(flat)

        return self.df

    def save_csv(self, name: str) -> None:
        """Saves collected data from scraping to csv with the specified name

        Args:
            name (str): Name of the csv
        """

        self.df.to_csv(f"{name}.csv", index=False)
