import requests
from bs4 import BeautifulSoup
import os

save_folder = 'images'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
source = requests.get('https://www.freeimages.com/search/dog', headers=headers).text

soup = BeautifulSoup(source, 'lxml')
images_list = []
images = soup.select('img[src^="https://images.freeimages.com/images"]')

for i in range(len(images)):
    images_list.append(images[i]['src'])

for i in range(len(images_list)):
    filename = os.path.join(save_folder, f'image_{i}.png')
    try:
        response = requests.get(images_list[i], headers=headers)
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded {filename}')
    except Exception as e:
        print(f'Error downloading {images_list[i]}: {e}')
