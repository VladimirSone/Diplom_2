import allure
import requests
from url import Url
from conftest import creating_user_and_delete
from helpers import random_email, random_password, random_username


class TestChangingUser:
    updated_user_data = {
        'email': random_email(),
        'password': random_password(),
        'name': random_username()
    }

    @allure.title('Проверить, что через ручку patch можно поменять данные пользователя,если он авторизован')
    @allure.title('Проверка статуса кода и тела ответа')
    # проверка авторизованного пользователя
    def test_authorization_user(self, creating_user_and_delete):
        headers = {'Authorization': creating_user_and_delete[1]['accessToken']}
        # меняю данные
        response = requests.patch(Url.URLPATCHUSER, data=TestChangingUser.updated_user_data, headers=headers)
        deserials = response.json()
        assert (response.status_code == 200
                and {'success': True}
                and deserials['user']['email'] == TestChangingUser.updated_user_data['email']
                and deserials['user']['name'] == TestChangingUser.updated_user_data['name'])

    @allure.title('Проверка ручки patch, что нельзя поменять данные неаутентифицированного пользователя')
    @allure.title('Проверка статуса кода и тело ответа')
    def test_update_user_unauthenticated_expected_error(self):
        response = requests.patch(Url.URLPATCHUSER, data=TestChangingUser.updated_user_data)
        assert (response.status_code == 401
                and {'success': False}
                and {'message': 'You should be authorised'})