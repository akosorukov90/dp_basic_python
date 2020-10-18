from classGetFotoVK import GetPhotoVK

TOKEN_VK = ''
owner_id = 0
album = 'profile'
count_photo = 5

vk_client = GetPhotoVK(TOKEN_VK)
print(vk_client.get_photo_vk(owner_id, album, count_photo))