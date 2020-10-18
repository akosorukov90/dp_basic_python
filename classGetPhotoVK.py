import requests
from urllib.parse import urljoin


class GetPhotoVK:
    API_BASE_URL = 'https://api.vk.com/method/'
    V = '5.21'

    def __init__(self, token):
        self.token = token
        self.list_photo_prop = []

    def get_photo_vk(self, owner_id, album, count_photo):
        photos_get_url = urljoin(self.API_BASE_URL, 'photos.get')
        response = requests.get(photos_get_url, params={
            'access_token': self.token,
            'v': self.V,
            'owner_id': owner_id,
            'album_id': album,
            'extended': 1,
            'count': count_photo
        })
        for item in response.json()['response']['items']:
            max_size_photo = 0
            link_max_size_photo = ''
            count_likes = 0
            date_download = 0
            size = 0
            for key, value in item.items():
                if 'photo_' in key:
                    size_photo = key.split('_')
                    if int(size_photo[1]) > max_size_photo:
                        max_size_photo = int(size_photo[1])
                        link_max_size_photo = value
                        r = requests.head(link_max_size_photo)
                        size = int(r.headers['Content-Length'])
                elif key == 'likes':
                    count_likes = value['count']
                elif key == 'date':
                    date_download = value

            self.list_photo_prop.append({
                'link': link_max_size_photo,
                'count_likes': count_likes,
                'date_download': date_download,
                'photo_size': size
            })

        return self.list_photo_prop
