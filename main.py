from classGetPhotoVK import GetPhotoVK
from classUploadToYaDisk import UploadToYaDisk


def upload_photo(token_vk, owner_id, album, count_photo, token_ya):
    vk_client = GetPhotoVK(token_vk)
    list_photo = vk_client.get_photo_vk(owner_id, album, count_photo)

    ya_disk = UploadToYaDisk(token_ya)
    folder_name = str(owner_id) + '_' + str(album) + '_photo'
    result = ya_disk.create_folder(folder_name)
    if result == 201 or result == 409:
        print('Начинаю загрузку фотографий')
        for photo in list_photo:
            path = folder_name
            link = photo['link']
            size = photo['photo_size']
            extension = link.split('.')
            name = str(photo['count_likes']) + '_' + str(photo['date_download']) + '.' + extension[-1]

            result = ya_disk.upload(path, name, link)
            if result == 202:
                print(f'Фотография {name} загружена')
            else:
                print(f'Фотография {name} не загружена')
    else:
        print(f'Ошибка. Код {result}')


TOKEN_VK = ''
owner_id = 0
album = 'profile'
count_photo = 5
TOKEN_YaDisk = ''

upload_photo(TOKEN_VK, owner_id, album, count_photo, TOKEN_YaDisk)
