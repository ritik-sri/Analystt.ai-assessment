# Product URL
# • Product Name
# • Product Price
# • Rating
# • Number of reviews


from bs4 import BeautifulSoup
import requests
import csv

HEADERS = ({'User-Agent': 'Chrome/44.0.2403.157',
            'Accept-Language': 'en-US, en;q=0.5'})

filename = 'data.csv'
with open(filename, 'a', encoding="utf-8") as csvfile:
    writter = csv.writer(csvfile)
    writter.writerow(['heading', 'link', 'price', 'rating', 'reviews'])

page_no = 1
for page in range(page_no, page_no + 20):  # CHECKING FOR SINGLE PAGE
    link = ""
    if page == 1:
        link = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2"
    else:
        link = f"https://www.amazon.in/s?k=bags&page={page}&crid=2M096C61O4MLT&qid=1697601507&sprefix=ba%2Caps%252&ref=sr_pg_{page}"

    webpage = requests.get(link, headers=HEADERS)
    print(f"Status Code: {webpage.status_code}")

    soup = BeautifulSoup(webpage.content, 'lxml')
    soup_search_result = soup.find_all('div', {"data-component-type": "s-search-result"})

    print(len(soup_search_result))

    for data in soup_search_result:
        d = {
            "heading": data.h2.span.text.replace(',', ''),
            "link": "https://www.amazon.in" + data.h2.a['href'],
            "price": data.find('span', {'class': "a-price-whole"}).text,
            "rating": data.find('span', {'class': "a-icon-alt"}).text,
            "reviews": data.find('span', {'class': "a-size-base s-underline-text"}).text
        }

        with open(filename, 'a', encoding="utf-8") as csvfile:
            writter = csv.writer(csvfile)
            writter.writerow(d.values())