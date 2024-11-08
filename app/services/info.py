import requests
from bs4 import BeautifulSoup


def channel(channel_url, date):
    url = f'{channel_url}?date={date}'

    response = requests.get(url)

    info_list = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div', class_='text-sm')
        for div in divs:
            check = div.find('div', class_='w-12 shrink-0')
            if check:
                time = div.find('div', class_="w-12 shrink-0").text.strip()
                title = div.find_all('div')[1].text.strip()
                info_data = {
                        'time': time,
                        'title': title,
                    }
                info_list.append(info_data)
            else:
                pass
        return info_list
    else:
        print("Ошибка при загрузке страницы")
