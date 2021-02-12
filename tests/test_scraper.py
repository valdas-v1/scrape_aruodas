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
