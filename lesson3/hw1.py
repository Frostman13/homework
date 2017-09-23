import settings
import requests

def get_newborns_data():
    api_key = settings.MOS_API_KEY
    url = 'https://apidata.mos.ru/v1/datasets/2009/rows?api_key={}' \
    .format(api_key)

    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Ошибка запроса')

if __name__ == '__main__':       
    data = get_newborns_data()
    print(data)
    