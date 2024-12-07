class Url:
    BASEURL = 'https://stellarburgers.nomoreparties.site'
    URLGETINGREDIENTS = f'{BASEURL}/api/ingredients'  # список ингредиентов
    URLPOSTCREATINGUSER = f'{BASEURL}/api/auth/register'  # создание пользователя
    URLPOSTLOGINUSER = f'{BASEURL}/api/auth/login'  # логин проверяю
    URLGETUPDATEUSER = f'{BASEURL}/api/auth/user'  # авторизация пользователя
    URLCREATINGORDERS = f'{BASEURL}/api/orders'  # создание заказа
    URLDELETEUSER = f'{BASEURL}/api/auth/user'  # удаление пользователя
    URLPATCHUSER = f'{BASEURL}/api/auth/user'  # обновение данных пользователя
    URLGETUSERORDERS = f'{BASEURL}/api/orders'  # заказ пользователя

