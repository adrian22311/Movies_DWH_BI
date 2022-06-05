from bs4 import BeautifulSoup
import requests
from urllib.parse import urlsplit
import unittest


def get_url(imdb_id):
    return f"https://www.imdb.com/title/tt{imdb_id}/"


def _get_number_of_votes(url):
    counts_page = requests.get(url)
    view_soup = BeautifulSoup(counts_page.text, features="html.parser")
    div = view_soup.find("div", {"class": "allText"})
    number_text = div.text.split(maxsplit=1)[0].replace(',', '')
    return int(number_text)


def get_info(imdb_url):
    page = requests.get(imdb_url)
    soup = BeautifulSoup(page.text, features="html.parser")

    rating_span = soup.find("span", {"sc-7ab21ed2-1 jGRxWM"})
    rating = float(rating_span.text)

    a_counts = soup.findChild("a", {"aria-label": "View User Ratings"}, href=True)
    split = urlsplit(imdb_url)
    number_of_votes = _get_number_of_votes(split.scheme + "://" + split.netloc + a_counts["href"])

    budget_li = soup.find("li", {"data-testid": "title-boxoffice-budget"})
    budget_txt = budget_li.findChild(class_="ipc-metadata-list-item__list-content-item").text
    budget_txt = budget_txt.split(maxsplit=1)[0].translate({ord(','): None, ord('$'): None})
    budget = int(budget_txt)

    gross_li = soup.find("li", {"data-testid": "title-boxoffice-cumulativeworldwidegross"})
    gross_txt = gross_li.findChild(class_="ipc-metadata-list-item__list-content-item").text
    gross_txt = gross_txt.split(maxsplit=1)[0].translate({ord(','): None, ord('$'): None})
    gross = int(gross_txt)

    return rating, number_of_votes, budget, gross


def get_all_data(imdb_id):
    url = get_url("0114709")
    return get_info(url)


class TestIMDbScrapping(unittest.TestCase):

    def test_number_of_votes(self):
        self.assertTrue(_get_number_of_votes("https://www.imdb.com/title/tt0120363/ratings/?ref_=tt_ov_rt"))

    def test_without_url(self):
        rating, number, budget, gross = get_info("https://www.imdb.com/title/tt0126029/")
        self.assertTrue(rating)
        self.assertTrue(number)
        self.assertTrue(budget)
        self.assertTrue(gross)

    def test_with_url1(self):
        rating, number, budget, gross = get_all_data("114709")
        self.assertTrue(rating)
        self.assertTrue(number)
        self.assertTrue(budget)
        self.assertTrue(gross)

    def test_with_url2(self):
        rating, number, budget, gross = get_all_data("2119532")
        self.assertTrue(rating)
        self.assertTrue(number)
        self.assertTrue(budget)
        self.assertTrue(gross)


if __name__ == '__main__':
    unittest.main()
