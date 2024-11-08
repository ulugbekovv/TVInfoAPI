import requests
from bs4 import BeautifulSoup

def all_channels():
    url = 'https://tvinfo.uz/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div', class_='lg:rounded-2xl bg-white lg:bg-teal-product-light')
        channels_list = []
        
        for div in divs:
            check = div.find('div', class_='p-4 border-b border-gray-200 lg:border-gray-300 flex space-x-3 items-center')
            if check:
                title = div.find('a', class_="text-[#00897B] font-semibold")
                no_info_element = div.find('div', class_='px-4 py-12 text-center text-sm text-gray-500')
                
                if no_info_element and 'Информация о сеансах отсутствует' in no_info_element.text:
                    continue 
                else:
                    channel_data = {
                        'channel_name': title.text.strip(),
                        'url': title.get("href"),
                    }
                    channels_list.append(channel_data)
        
        return channels_list
    else:
        print("Ошибка при загрузке страницы")
        return []
