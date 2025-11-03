# Book Scraper

A Python script that scrapes book information from [Books to Scrape](http://books.toscrape.com), a sandbox website for web scrapers. The script collects the title, price, and star rating for every book on the site and saves the data into a `scraped_books.csv` file.

This project demonstrates proficiency in web scraping, HTML parsing, data extraction, and data storage.

## Features

-   **Multi-Page Scraping:** Automatically navigates through all paginated pages.
-   **Data Extraction:** Gathers multiple data points for each book (title, price, rating).
-   **Robust:** Includes basic error handling for network requests.
-   **Polite:** Pauses for 1 second between page requests to avoid overloading the server.
-   **Structured Output:** Saves the collected data neatly into a CSV file with headers.

## Setup and Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/book-scraper.git
    cd book-scraper
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the scraper:**
    ```bash
    python scraper.py
    ```

The script will print its progress as it scrapes each page. Once completed, you will find a `scraped_books.csv` file in the project directory with all the collected data.

### Example CSV Output (`scraped_books.csv`)

| title                   | price     | rating |
| ----------------------- | --------- | ------ |
| A Light in the Attic    | £51.77    | 3      |
| Tipping the Velvet      | £53.74    | 1      |
| Soumission              | £50.10    | 1      |
| ...                     | ...       | ...    |

## Project Structure
