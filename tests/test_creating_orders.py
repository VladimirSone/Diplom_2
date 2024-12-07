import allure
import pytest
import requests
from url import Url
from data import Ingredients
from conftest import creating_user_and_delete


class TestCreatingOrders:

    @allure.title('Проверить, что авторизованный пользователь может сделать заказ')
    @allure.title('Проверить статус кода и тело запроса')
    @pytest.mark.parametrize('burger_ingredients', [Ingredients.burger_1, Ingredients.burger_2])
    def test_orders_authorization(self, burger_ingredients, creating_user_and_delete):
        # создаю пользователя и удадяю его из базы
        headers = {'Authorization': creating_user_and_delete[1]['accessToken']}
        # делаю заказ
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Url.URLCREATINGORDERS, data=payload, headers=headers)
        deserials = response.json()
        assert (response.status_code == 200
                and deserials['success'] is True
                and 'name' in deserials.keys()
                and 'number' in deserials['order'].keys())

    @allure.title('Проверка ответа о создании заказа на запрос с указанными ингредиентами неаутентифицированным пользователем')
    @allure.title('Проверка кода и тело ответа')
    @pytest.mark.parametrize('burger_ingredients', [Ingredients.burger_1, Ingredients.burger_2])
    def test_create_order_unauthenticated_user_success(self, burger_ingredients):
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Url.URLCREATINGORDERS, data=payload)
        assert (response.status_code == 200
                and {"success": True})

    @allure.title(
        'Проверка, что ручка post вернет ответ при заказе аутентифицированным пользователем и без указания хеша ингредиентов')
    @allure.title('Проверка статуса кода и тело ответа.')
    def test_order_empty_ingredients_authenticated_user_expected_error(self, creating_user_and_delete):
        headers = {'Authorization': creating_user_and_delete[1]['accessToken']}
        # создаю заказ
        payload = {'ingredients': []}
        response = requests.post(Url.URLCREATINGORDERS, data=payload, headers=headers)
        assert (response.status_code == 400
                and {'success': False}
                and {'message': 'Ingredient ids must be provided'})

    @allure.title('Проверка, что ручка вернет ошибку при создании заказа с неуказанными ингредиентами и неаутентифицированным пользователем и без хеша ингредиента')
    @allure.title('Проверка статуса кода и тело ответа.')
    def test_create_order_empty_ingredients_unauthenticated_user_expected_error(self):
        payload = {'ingredients': []}
        response = requests.post(Url.URLCREATINGORDERS, data=payload)
        assert (response.status_code == 400
                and {'success': False}
                and {'message': 'Ingredient ids must be provided'})

    @allure.title('Проверка ручки post при создании заказа с неверным хэшем ингредиента и аутентифицированным пользователем')
    @allure.title('Проверка статуса кода и тело ответа')
    def test_create_order_invalid_ingredients_authenticated_user_expected_error(self, creating_user_and_delete):
        # создание пользователя и его удаление из базы
        headers = {'Authorization': creating_user_and_delete[1]['accessToken']}
        # создаю заказ
        payload = {'ingredients': [Ingredients.incorrect_hash_ingredient]}
        response = requests.post(Url.URLCREATINGORDERS, data=payload, headers=headers)
        assert (response.status_code == 500
                and {"success": False}
                and {"message": "One or more ids provided are incorrect"})
