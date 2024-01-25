import requests
from bs4 import BeautifulSoup


def main():
    print("Starting scraping...")

    base_url = "https://www.tabnews.com.br/recentes/pagina/"
    response = requests.get(f"{base_url}1")
    html = response.text

    soup = BeautifulSoup(html, features="html.parser")

    # __next > div > div > main > ol > li:nth-child(1) > article > div.Box-sc-g0xbh4-0.ivqXmt > a
    ol = soup.div.div.main.ol.contents


    print("[INFO] Printing post names from TabNews first page...")
    for li in ol:
        print(li.article.div.a.text)


if __name__ == "__main__":
    main()
