import telebot

# логирование. Делаем обёртки командам
def log1(message): 
    file = open('db.csv', 'a', encoding='utf-8')
    file.write(f'{message.from_user.first_name}, \
        {message.from_user.last_name}, \
        {message.from_user.id}, \
        {message.text}\n')
    file.close()