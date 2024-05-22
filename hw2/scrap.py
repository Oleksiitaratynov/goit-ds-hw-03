import requests
from bs4 import BeautifulSoup
import json
import time

base_url = "http://quotes.toscrape.com"

authors = []
quotes = []
authors_dict = {}

# Функція для скрапінгу інформації про автора
def scrape_author(author_url):
    response = requests.get(author_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    author_details = soup.find('div', class_='author-details')

    fullname = author_details.find('h3', class_='author-title').text.strip()
    born_date = author_details.find('span', class_='author-born-date').text.strip()
    born_location = author_details.find('span', class_='author-born-location').text.strip()
    description = author_details.find('div', class_='author-description').text.strip()
    
    author_info = {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }
    
    return author_info

# Функція для скрапінгу цитат
def scrape_quotes():
    page = 1
    while True:
        response = requests.get(f"{base_url}/page/{page}/")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        quote_elements = soup.find_all('div', class_='quote')
        
        if not quote_elements:
            break
        
        for quote_element in quote_elements:
            quote_text = quote_element.find('span', class_='text').text.strip()
            author_name = quote_element.find('small', class_='author').text.strip()
            tags = [tag.text for tag in quote_element.find_all('a', class_='tag')]
            
            if author_name not in authors_dict:
                author_url = base_url + quote_element.find('a')['href']
                author_info = scrape_author(author_url)
                authors.append(author_info)
                authors_dict[author_name] = author_info
            
            quote = {
                "tags": tags,
                "author": author_name,
                "quote": quote_text
            }
            quotes.append(quote)
        
        page += 1
        time.sleep(1)  # Будемо ввічливі до сервера

scrape_quotes()

# Збереження авторів у файл authors.json
with open('authors.json', 'w', encoding='utf-8') as authors_file:
    json.dump(authors, authors_file, ensure_ascii=False, indent=4)

# Збереження цитат у файл quotes.json
with open('quotes.json', 'w', encoding='utf-8') as quotes_file:
    json.dump(quotes, quotes_file, ensure_ascii=False, indent=4)

print("Скрапінг завершено та дані збережено у файли JSON.")
