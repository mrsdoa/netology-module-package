import emoji #emoji-2.2.0.

emoji.emojize(language='alias')

def print_simbol(question):
    if question == 'Да':
        print(emoji.emojize('Python is :red_heart:'))
    else:
        print(emoji.emojize('Python is :cold_sweat:'))


question = input('Тебе нравится Python? Введи: "Да", "Нет":')
# print_simbol(question)