import allure
import pytest
import requests
from url import Url
from data import UserData
from helpers import random_email, random_password, random_username

class TestCreatingUser:

    @allure.title('Проверка ручки post на создание уникального пользователя')
    @allure.title('Проверка статуса кода и тела ответа')
    def test_creating_unique_user(self):
        payload = {"email": random_email(), "password": random_password(), "name": random_username()}
        response = requests.post(Url.URLPOSTCREATINGUSER, data=payload)
        deserials = response.json()
        assert (response.status_code == 200
                and deserials['success'] is True
                and 'accessToken' in deserials.keys()
                and 'refreshToken' in deserials.keys()
                and deserials['user']['email'] == payload['email']
                and deserials['user']['name'] == payload['name'])
        # удаление пользователя
        access_token = deserials['accessToken']
        requests.delete(Url.URLDELETEUSER, headers={'Authorization': access_token})

    @allure.title('Проверка ручки post, что вернется ошибка, если такой пользователь уже существует')
    @allure.title('Проверка статуса кода и ручки ответа')
    def test_creating_again_user(self):
        payload = {"email": UserData.EMAIL, "password": UserData.PASSWORD, "name": UserData.NAME}
        response = requests.post(Url.URLPOSTCREATINGUSER, data=payload)
        assert (response.status_code == 403
                and {"success": 'false'}
                and {"message": "User already exists"})

    @allure.title('Проверка ручки post на создание уникального пользователя без указания одного из обязательных полей')
    @allure.title('Проверка статуса кода и тела ответа')
    @pytest.mark.parametrize('user_data', [UserData.NO_PASSWORD_USER, UserData.NO_EMAIL_USER, UserData.NO_NAME_USER])
    def test_creating_no_password_user(self, user_data):
        response = requests.post(Url.URLPOSTCREATINGUSER, data=user_data)
        assert (response.status_code == 403
                and {"success": 'false'}
                and {"message": "Email, password and name are required fields"})
