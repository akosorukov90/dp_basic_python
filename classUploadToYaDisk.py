import requests


class UploadToYaDisk:
    def __init__(self, token: str):
        self.token = token

    def create_folder(self, name_folder):
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        response = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params={'path': name_folder},
            headers=HEADERS,
        )
        return response.status_code

    def upload(self, path: str, name: str, link: str):
        """Метод загруджает файл на яндекс диск"""
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        response = requests.post(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={'path': '/' + path + '/' + name, 'url': link},
            headers=HEADERS,
        )
        return response.status_code
