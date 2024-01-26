from typing import List

import requests
from bs4 import BeautifulSoup


def request_page_html(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"[ERROR] could not get page, stopping scrape. Error: {err}")
        raise SystemExit()

    return response.text


def extract_post_list_items(soup: BeautifulSoup) -> List[str]:
    try:
        post_list_items = soup.div.div.main.ol.contents
    except AttributeError as err:
        print(f"[ERROR] bs4 could not find element. Error: {err}")
        raise SystemExit()

    return post_list_items


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
