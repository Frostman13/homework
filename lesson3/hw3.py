from flask import Flask, abort, request
import requests
import settings
import json

app = Flask(__name__)

def get_newborns_data():
    api_key = settings.MOS_API_KEY
    url = 'https://apidata.mos.ru/v1/datasets/2009/rows?api_key={}' \
    .format(api_key)

    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Ошибка запроса')

@app.route('/')
def index():
    result = 'Привет, это главная страница'
    return(result)

@app.route('/names')
def names():
    year = int(request.args.get('year'))
    if 2015 <= year <= 2017:
        newborns_data = get_newborns_data()
        result = """
                <table>
                <tr>
                    <th>Месяц</th>
                    <th>Имя</th>
                    <th>Количество новорожденных</th>
                </tr>
                """ 
        for name in newborns_data:
            name_data = name['Cells']
            if name_data['Year'] == year:
                result += """
                        <tr>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                        </tr>                
                        """.format(name_data['Month'], name_data['Name'], name_data['NumberOfPersons'])
        result += '</table>'
    else:
        result = '<h1>Укажите корректный год</h1>'
    return result



if __name__ == '__main__':
    app.run(port=5000, debug=True)

    # newborns_data = get_newborns_data()
    # print(len(newborns_data))
    # for name in newborns_data:
    #     name_data = name['Cells']
    #     print(name_data)
    #     print('1')
    # print(newborns_data[1]['Cells']['Year'])