import requests
from bs4 import BeautifulSoup
import csv
import time

# The base URL of the website to scrape
BASE_URL = "http://books.toscrape.com/catalogue/"
# The starting page
CURRENT_URL = f"{BASE_URL}page-1.html"

def scrape_books_from_page(url):
    """
    Scrapes all book data from a single page.

    Args:
        url (str): The URL of the page to scrape.

    Returns:
        list: A list of dictionaries, where each dictionary represents a book.
        str: The URL of the next page, or None if it's the last page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page {url}: {e}")
        return [], None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    books_on_page = []
    
    # Find all book articles on the page
    articles = soup.find_all('article', class_='product_pod')
    
    # Mapping of star rating text to a number
    rating_map = {
        'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
    }

    for article in articles:
        # Extract title from the <h3> tag's <a> element
        title = article.h3.a['title']
        
        # Extract price from the <p> tag with class 'price_color'
        price = article.find('p', class_='price_color').text
        
        # Extract star rating from the <p> tag's class name
        rating_class = article.find('p', class_='star-rating')['class'][1]
        rating = rating_map.get(rating_class, 0) # Default to 0 if not found
        
        books_on_page.append({
            'title': title,
            'price': price,
            'rating': rating
        })
        
    # Find the 'next' button to determine the next page URL
    next_button = soup.find('li', class_='next')
    if next_button:
        next_page_url = BASE_URL + next_button.a['href']
    else:
        next_page_url = None
        
    return books_on_page, next_page_url


def save_to_csv(books, filename='scraped_books.csv'):
    """
    Saves a list of book data to a CSV file.

    Args:
        books (list): The list of book dictionaries.
        filename (str): The name of the output CSV file.
    """
    if not books:
        print("No books to save.")
        return

    # The keys of the first dictionary will be our headers
    headers = books[0].keys()

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=headers)
            dict_writer.writeheader()
            dict_writer.writerows(books)
        print(f"Successfully saved {len(books)} books to '{filename}'.")
    except IOError as e:
        print(f"Error writing to file '{filename}': {e}")


if __name__ == "__main__":
    all_books = []
    current_page_url = CURRENT_URL
    page_number = 1

    # Loop through all pages until there is no 'next' page
    while current_page_url:
        print(f"Scraping page {page_number}: {current_page_url}")
        
        books, next_page_url = scrape_books_from_page(current_page_url)
        
        if books:
            all_books.extend(books)
        
        current_page_url = next_page_url
        page_number += 1
        time.sleep(1) # Be a good citizen and don't spam the server

    if all_books:
        save_to_csv(all_books)
    else:
        print("Scraping finished, but no data was collected.")
