import requests


class UploadToYaDisk:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, name: str):
        """Метод загруджает файл file_path на яндекс диск"""
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        link_upload = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={'path': '/' + name, 'overwrite': 'true'},
            headers=HEADERS,
        )
        if link_upload.status_code == 200:
            print('Ссылка получена, начинаю загрузку')
            with open(file_path, 'rb') as f:
                data = f.read()
            response = requests.put(link_upload.json()['href'], data)
            if response.status_code == 201:
                result = f'Файл {name} загружен'
            else:
                result = f'Ошибка загрузки {name}'
        else:
            result = f'Ссылка на загрузку не получена'
        return result


if __name__ == '__main__':
    TOKEN = ''
    path = ''
    replace_slash = path.replace('\\', '/')
    name = replace_slash.split('/')[-1]
    uploader = UploadToYaDisk(TOKEN)
    result = uploader.upload(path, name)
    print(result)