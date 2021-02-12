import pytest
from scrape_aruodas.scraper import Scraper
import pandas as pd
from bs4 import BeautifulSoup

scraper = Scraper()
aruodas_url = "https://m.en.aruodas.lt/"
example_apartment_url = "https://m.en.aruodas.lt/butai-vilniuje-naujamiestyje-gerosios-vilties-g-siulome-irengta-dvieju-kambariu-buta-su-1-2964577/"


def test_get_response():
    response = scraper.get_response(aruodas_url)
    assert response


def test_get_soup():
    soup = scraper.get_soup(scraper.get_response(aruodas_url))
    assert isinstance(soup, BeautifulSoup)


def test_extract_apartment_data():
    soup = scraper.get_soup(scraper.get_response(example_apartment_url))
    df = scraper.extract_apartment_data(soup)
    assert not df.empty


def test_filter_apartment_data():
    soup = scraper.get_soup(scraper.get_response(example_apartment_url))
    df = scraper.extract_apartment_data(soup)

    filtered_df = scraper.filter_apartment_data(df)

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

    assert (filtered_df.columns == required_data).all()


def test_clean_apartment_data():
    soup = scraper.get_soup(scraper.get_response(example_apartment_url))
    df = scraper.extract_apartment_data(soup)
    filtered_df = scraper.filter_apartment_data(df)

    clean_df = scraper.clean_apartment_data(df)

    assert clean_df["Area"].iloc[0] == "47"
    assert clean_df["Build year"].iloc[0] == ["2020"]


def check_if_renovated():
    soup = scraper.get_soup(scraper.get_response(example_apartment_url))
    df = scraper.extract_apartment_data(soup)
    filtered_df = scraper.filter_apartment_data(df)
    clean_df = scraper.clean_apartment_data(df)

    clean_df = scraper.check_if_renovated(clean_df)

    assert clean_df["Renovation year"].iloc[0] == "0"


def test_extract_price():
    soup = scraper.get_soup(scraper.get_response(example_apartment_url))
    price = scraper.extract_price(soup)

    assert price == "129400"


def test_extract_address():
    soup = scraper.get_soup(scraper.get_response(example_apartment_url))
    address = scraper.extract_address(soup)

    assert address == ['Vilnius', ' Naujamiestis', ' Gerosios Vilties g.']


def test_extract_info():
    soup = scraper.get_soup(scraper.get_response(example_apartment_url))
    scraper.extract_info(soup)

    assert len(scraper.df.columns) == 13
    

def test_scrape_aruodas():
    scraper.scrape_aruodas(1)

    assert scraper.df.shape == (26,13)