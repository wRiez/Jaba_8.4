import random as r

answers = ['Норм', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    k = r.randint(0, len(answers)-1)
    return answers[k]

print(how_are_you())