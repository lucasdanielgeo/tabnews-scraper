from typing import List

import requests
from bs4 import BeautifulSoup
from requests import Response


def request_page_html(url: str) -> Response:
    response = requests.get(url)

    return response.text


def extract_post_list_items(soup: BeautifulSoup) -> List[str]:
    return soup.div.div.main.ol.contents


def extract_post_title(li: str) -> str:
    title = li.article.div.a.text

    return title if title else ""


def extract_post_titles(posts: List[str]) -> List[str]:
    return [extract_post_title(li) for li in posts]


def main():
    base_url = "https://www.tabnews.com.br/recentes/pagina/"
    page = 1
    html_text = request_page_html(f"{base_url}{page}")

    soup = BeautifulSoup(html_text, features="html.parser")

    post_items = extract_post_list_items(soup=soup)
    post_titles = extract_post_titles(posts=post_items)

    print("[INFO] Printing post names from first page...\n")
    for title in post_titles:
        print(title)


if __name__ == "__main__":
    main()
