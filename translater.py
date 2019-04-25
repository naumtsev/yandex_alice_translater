import requests


def get_translate(word):
    api_key = 'trnsl.1.1.20190425T121546Z.efe600c148bbb598.1d00aba4080761155aa761de84d29c3b9b60ebf5'
    url_translate = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': api_key,
        'format': 'plain',
        'text': word,
        'lang': 'en',
        'options': 1
    }
    try:
        response = requests.get(url_translate, params).json()
        return response['text'][0]
    except Exception as err:
        return 'None'
