import requests
from bs4 import BeautifulSoup
import csv


def write_csv(data):
    with open("yandex_news.csv", "a") as f:
        writer = csv.writer(f, lineterminator='\r')
        writer.writerow((data["topic"], data["url"], data["source"]))


def get_html(url):
    r = requests.get(url)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("div", class_="mg-grid__col")
    for el in elements:
        try:
            topic = el.find("a").text.strip()
        except ValueError:
            topic = ""
        try:
            url = el.find("h2").find("a").get("href")
        except ValueError:
            url = ""
        try:
            source = el.find("span", class_="mg-card-source__source").find("a").text.strip()
        except ValueError:
            source = ""
        data = {"topic": topic, "url": url, "source": source}
        write_csv(data)


def main():
    url = "https://yandex.ru/news"
    get_page_data(get_html(url))


if __name__ == "__main__":
    main()

print("_______________________________________________________________________")
