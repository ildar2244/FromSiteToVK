import os

class MyVkData:
    # Идентификатор моего пользователя вконтакте
    MY_USER_ID = 'user_ID'
    # Общая ссылка для доступа к api
    API_URL = 'https://api.vk.com/method/'
    # Идентификатор приложения вконтакте
    APP_ID = 'standalone_app_id'

    #Мой логин Вконтакте
    @staticmethod
    def get_login_user():
        f = open(os.path.join(os.path.dirname(__file__), 'private_vk_login.txt'), 'r')
        login = f.read().rstrip()
        f.close()
        return login

    # Мой пароль Вконтакте
    @staticmethod
    def get_password_user():
        f = open(os.path.join(os.path.dirname(__file__), 'private_vk_pass.txt'), 'r')
        passw = f.read().rstrip()
        f.close()
        return passw

    # Токен Вконтакте с доступом к Фото и Товарам
    @staticmethod
    def get_token():
        f = open(os.path.join(os.path.dirname(__file__), 'private_vk_token.txt'), 'r')
        token = f.read().rstrip()
        f.close()
        return token

