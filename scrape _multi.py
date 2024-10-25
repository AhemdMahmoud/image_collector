import os
import requests
from bs4 import BeautifulSoup
import urllib.request
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

def download_images_from_page(url, save_folder, page_number):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    images_list = []
    images = soup.select('img[src^="https://images.freeimages.com/images"]')

    for img in images:
        images_list.append(img['src'])

    for i, img_url in enumerate(images_list):
        # Create a unique filename that includes the page number
        filename = os.path.join(save_folder, f'image_page{page_number}_{i}.jpg')
        try:
            urllib.request.urlretrieve(img_url, filename)
            print(f'Downloaded {filename}')
        except Exception as e:
            print(f'Error downloading {img_url}: {e}')

def main():
    save_folder = 'images'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    base_url = 'https://www.freeimages.com/search/dog'
    num_pages = 5  # Number of pages to scrape
    
    for page in range(1, num_pages + 1):
        url = f'{base_url}/{page}'
        print(f'Scraping {url}')
        download_images_from_page(url, save_folder, page)

if __name__ == "__main__":
    main()
