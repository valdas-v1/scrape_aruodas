import pytest
from scrape_aruodas.scraper import Scraper
import pandas as pd
from bs4 import BeautifulSoup

a = Scraper()


def test_get_response():
    response = a.get_response("https://m.en.aruodas.lt/")
    assert response.ok


def test_get_soup():
    soup = a.get_soup(a.get_response("https://m.en.aruodas.lt/"))
    assert isinstance(soup, BeautifulSoup)
