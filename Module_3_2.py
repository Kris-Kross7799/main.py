def send_email(message, recipient, sender='university.help@gmail.com'):
    ends = ('.com', '.ru', '.net')
    if recipient.endswith(ends) and sender.endswith(ends) and "@" in recipient and '@' in sender:
        print('')
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender=='university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}!')

        elif sender!='university.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            print()
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

