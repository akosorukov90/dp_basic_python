import requests
from urllib.parse import urljoin
from pprint import pprint


def get_photo_vk(owner_id, album):
    photos_get_url = urljoin(API_BASE_URL, 'photos.get')
    response = requests.get(photos_get_url, params={
        'access_token': TOKEN,
        'v': V,
        'owner_id': owner_id,
        'album_id': album,
        'extended': 1
    })
# pprint(response.json())
    for item in response.json()['response']['items']:
        max_size_photo = 0
        link_max_size_photo = ''
        count_likes = 0
        date_download = 0
        for key, value in item.items():
            if 'photo_' in key:
                size_photo = key.split('_')
                if int(size_photo[1]) > max_size_photo:
                    max_size_photo = int(size_photo[1])
                    link_max_size_photo = value
            elif key == 'likes':
                count_likes = value['count']
            elif key == 'date':
                date_download = value

            print(link_max_size_photo)
            print(count_likes)
            print(date_download)
            print()


TOKEN = 'b93d7eaf6bae38f0a79622f61c63df72296bb22a1ab20de06d639c35de64d34a22f416bbc43dbae4eb5c2'
API_BASE_URL = 'https://api.vk.com/method/'
V = '5.21'
owner_id = 552934290
album = 'profile'
get_photo_vk(owner_id, album)