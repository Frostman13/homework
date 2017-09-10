ANSWERS = {"привет": "И тебе привет!", "как дела": "Лучше всех"}

def get_answer(question):
    return ANSWERS.get(question)

def ask_user(answers):
    while True:
        try:
            user_input = input('Скажи что-нибудь:\n')
            answer = get_answer(user_input)            
            if str.lower(user_input) == 'пока':
                print('Увидимся')
                break
            print('{}\n'.format(answer))
        except KeyboardInterrupt:
            print('Как жаль что вы уходите')
            break

if __name__ == '__main__':
    ask_user(ANSWERS)
