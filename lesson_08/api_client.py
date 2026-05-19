import requests


class YouGileApiClient:
    def __init__(self):
        self.base_url = "https://ru.yougile.com/api-v2/"

        # "СЮДА_ВСТАВИТЬ_КЛЮЧ_ИЗ_ИНСТРУКЦИИ"
        self.my_key = "!!!"

        # Headers для авторизации запросов
        self.headers = {
            "Authorization": f"Bearer {self.my_key}",
            "Content-Type": "application/json"
        }

    def create_project(self, body_data):
        """1. Метод [POST] Создание проекта"""
        url = f"{self.base_url}/projects"
        response = requests.post(url, json=body_data, headers=self.headers)
        return response

    def update_project(self, project_id, body_data):
        """2. Метод [PUT] Изменение проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, json=body_data, headers=self.headers)
        return response

    def get_project(self, project_id):
        """3. Метод [GET] Получение проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response


api = YouGileApiClient()
