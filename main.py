from flask import Flask, request
import json
# импортируем функции из нашего второго файла geo
from translater import get_translate

app = Flask(__name__)

UsersINFO = dict()

@app.route('/post', methods=['POST'])
def main():
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    handle_dialog(response, request.json)
    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']

    if req['session']['new']:
        res['response']['text'] = \
            'Привет, я Алиса и я умею переводить слова на английский язык! Давай попробуем! Шаблон: Переведите (переведи) слово: *слово*'
        return


    now_speak = req['request']['original_utterance'].lower()

    if('переведите слово' in now_speak or 'переведи слово' in now_speak):
        now_str = ''
        for i in now_speak:
            if i.isalpha():
                now_str += i
            else:
                now_str += ' '

        now_str = now_str.replace('  ', ' ')
        try:
            if('переведите слово' in now_str):
                need_word = now_str.replace('переведите слово', '').split()[0]
                res['response']['text'] = 'Перевод слова {} - '.format(need_word) + get_translate(need_word)
            else:
                need_word = now_str.replace('переведи слово', '').split()[0]
                res['response']['text'] = 'Перевод слова {} - '.format(need_word) + get_translate(need_word)
        except Exception as error:
            res['response']['text'] = 'Прошу вас выражатся попонятнее'

    else:
        res['response']['text'] = \
            'Простите, но я вас не поняла, воспользуйтесь шаблоном! Шаблон: Переведите (переведи) слово: *слово*'




if __name__ == '__main__':
    app.run()