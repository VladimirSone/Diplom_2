import allure
import requests
from url import Url
from conftest import creating_user_and_delete


class TestGetOrders:

    @allure.title('Проверка успешного получения списка заказов для аутентифицированного пользователя')
    @allure.title('Проверка статуса кода и тело ответа')
    def test_get_orders_authenticated_user_success(self, creating_user_and_delete):
        # создание пользователя и его удаление из базы
        headers = {'Authorization': creating_user_and_delete[1]['accessToken']}
        # получение заказа пользователя
        response = requests.get(Url.URLGETUSERORDERS, headers=headers)
        deserials_order = response.json()
        assert (response.status_code == 200
                and deserials_order['success'] is True
                and 'orders' in deserials_order.keys()
                and 'total' in deserials_order.keys())

    @allure.title('Проверка ответа при запросе на получение списка заказов неаутентифицированного пользователя')
    @allure.title('Проверка статуса кода и тело ответа')
    def test_get_orders_unauthenticated_user_success(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(Url.URLGETUSERORDERS, headers=headers)
        assert (response.status_code == 401
                and {'success': False}
                and {'message': 'You should be authorised'})