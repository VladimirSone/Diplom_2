import pytest
import requests
from helpers import random_email, random_password, random_username
from url import Url
import allure


@pytest.fixture
@allure.title('Фикстура создает пользователя и удаляет его из базы после теста')
def creating_user_and_delete():
    # создаю пользователя
    payload_user = {"email": random_email(), "password": random_password(), "name": random_username()}
    response = requests.post(Url.URLPOSTCREATINGUSER, data=payload_user)
    deserials = response.json()
    # авторизаця пользователя
    requests.post(Url.URLPOSTLOGINUSER, data=payload_user)

    yield payload_user, deserials

    access_token = deserials['accessToken']
    requests.delete(Url.URLDELETEUSER, headers={'Authorization': access_token})
