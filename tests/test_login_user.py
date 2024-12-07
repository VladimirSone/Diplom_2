import allure
import requests
from url import Url
from data import UserData
from helpers import random_password, random_email, random_username
from conftest import creating_user_and_delete

class TestLoginUser:

    @allure.title('Проверка ручки post, что есть вход под логином существующего пользователя')
    @allure.title('Проверка  статуса кода и тела ответа')
    def test_user(self, creating_user_and_delete):
        payload = creating_user_and_delete[0]
        response = requests.post(Url.URLPOSTLOGINUSER, data=payload)
        deserials = response.json()
        assert (response.status_code == 200
                and deserials['success'] is True
                and 'accessToken' in deserials.keys()
                and 'refreshToken' in deserials.keys())

    @allure.title('Проверка ручки post логин с неверным паролем')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_false_email_user(self):
        payload = {"email": UserData.EMAIL, "password": random_password()}
        response = requests.post(Url.URLPOSTLOGINUSER, data=payload)
        assert (response.status_code == 401
                and {"success": 'false'}
                and {"message": "email or password are incorrect"})

    @allure.title('Проверка ручки post логин с неверным  email')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_false_password_user(self):
        payload = {"email": random_email(), "password": UserData.PASSWORD}
        response = requests.post(Url.URLPOSTLOGINUSER, data=payload)
        assert (response.status_code == 401
                and {"success": 'false'}
                and {"message": "email or password are incorrect"})
