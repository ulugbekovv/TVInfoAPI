import requests
from bs4 import BeautifulSoup

def all_categories():
    url = 'https://tvinfo.uz/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('li', class_='grow')
        categories_list = []
        
        for div in divs:
            check = div.find('a', class_='block')
            if check:
                title = div.find('a')
                category_data = {
                    'category_name': title.text.strip(),
                    'url': title.get("href"),
                }
                categories_list.append(category_data)
        
        return categories_list
    else:
        print("Ошибка при загрузке страницы")
        return []
