import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from main import url_handler


def get_data(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=ChromeService(),
        options=chrome_options,
    )
    driver.get(url)
    time.sleep(5)
    # Get the page source after dynamic content is loaded
    page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page_source, "html.parser")

    return soup.find_all("div", class_="gridItem--Yd0sa")


def extract_data(product_containers):
    for product_container in product_containers:
        # Extract relevant information for each product
        try:
            product_name = product_container.find(
                "div", class_="title--wFj93"
            ).a.text.strip()
            product_price = product_container.find(
                "div", class_="price--NVB62"
            ).text.strip()
            product_discount = product_container.find(
                "span", class_="discount--HADrg"
            ).text.strip()
            product_rating = product_container.find(
                "div", class_="rating--ZI3Ol"
            ).text.strip()
            product_reviews = product_container.find(
                "span", class_="rating__review--ygkUy"
            ).text.strip()
            product_location = product_container.find(
                "span", class_="location--eh0Ro"
            ).text.strip()

            # Print or store the information as needed
            print(f"Product Name: {product_name}")
            print(f"Product Price: {product_price}")
            print(f"Discount: {product_discount}")
            print(f"Rating: {product_rating}")
            print(f"Reviews: {product_reviews}")
            print(f"Location: {product_location}")
            print("-" * 30)
        except AttributeError as e:
            print("Error extracting product information:", e)


def main():
    item_to_search = input("Name the item you want to search: ")

    for base_url in url_handler.urls:
        url = f"{base_url}/{item_to_search}"
        product_containers = get_data(url)
        extract_data(product_containers)


if __name__ == "__main__":
    main()
