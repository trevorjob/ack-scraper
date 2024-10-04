import requests

from bs4 import BeautifulSoup


request = requests.get("https://www.ackuniversal.com/")


request.raise_for_status()

soup = BeautifulSoup(request.content, "html.parser")


def save_page_to_html(url, filename):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Save the content to a file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Page saved to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")


# Usage
url = "https://www.ackuniversal.com/"  # Replace with the URL you want to scrape
filename = "scraped_page.html"  # Name of the file to save the page as
save_page_to_html(url, filename)
