from helpers import random_email, random_password, random_username
class UserData:
    EMAIL = 'shutov@yandex.ru'
    PASSWORD = '12345'
    NAME = 'VladimirA'
    NO_EMAIL_USER = {'email': '', 'password': '12345', 'name': 'VladimirA'}
    NO_PASSWORD_USER = {'email': 'shutov@yandex.ru', 'password': '', 'name': 'VladimirA'}
    NO_NAME_USER = {'email': 'shutov@yandex.ru', 'password': '12345', 'name': ''}

    empty_data = [
        {'email': '',
         'password': random_password(),
         'name': random_username()
         },
        {'email': random_email(),
         'password': '',
         'name': random_username()
         },
        {'email': random_email(),
         'password': random_password(),
         'name': ''
         }
    ]

class Ingredients:
    burger_1 = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
                '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

    burger_2 = ['61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6d',
                '61c0c5a71d1f82001bdaaa7a', '61c0c5a71d1f82001bdaaa6f']

    incorrect_hash_ingredient = '61c0c5a71d1f82001bdmma6f'
