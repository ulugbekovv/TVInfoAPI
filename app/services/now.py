import requests
from datetime import datetime
from bs4 import BeautifulSoup


def now(channel_url):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    url = f'{channel_url}?date={formatted_date}'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div', class_='flex text-sm text-[#EA580C] font-semibold')
        for div in divs:
            check = div.find('div', class_='w-12 shrink-0')
            if check:
                time = div.find('div', class_="w-12 shrink-0").text.strip()
                title = div.find_all('div')[1].text.strip()
                now_data = {
                        'time': time,
                        'title': title,
                    }
                return now_data
            else:
                pass
    else:
        print("Ошибка при загрузке страницы")
