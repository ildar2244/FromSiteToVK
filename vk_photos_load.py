import requests
import json
import urllib.request
from my_data import MyVkData

# Переменные
token = MyVkData.get_token()
group_id = 141917296
image_name = 'uploaded_image.jpg'

# Методы ВК API
url_create_album = MyVkData.API_URL + 'photos.createAlbum'
url_upload_server = MyVkData.API_URL + 'photos.getUploadServer'
url_save_photo = MyVkData.API_URL + 'photos.save'

# Создание и запись данных в файл json-формата
def write_json(data, filename):
    with open(filename, 'w') as file_json:
        json.dump(data, file_json, indent=2, ensure_ascii=False)

# Создание нового фотоальбома в сообществе
def get_id_new_album(title, description):
    r = requests.get(url_create_album, params={'access_token': token,
                                               'title': title,
                                               'group_id': group_id,
                                               'description': description,
                                               'upload_by_admins_only': 1}).json()
    #write_json(r, 'album.json')
    return r['response']['aid']

# Получение адреса сервера для загрузки фото в альбом
def get_upload_server(alb_title, alb_description):
    # Создаем новый альбом и берем его id
    album_id = get_id_new_album(alb_title, alb_description)

    # Запрос на получение адреса сервера загрузки фото
    r = requests.get(url_upload_server, params={'access_token': token,
                                                'album_id': album_id,
                                                'group_id': group_id}).json()
    # write_json(r, 'upload_server.json')
    return r['response']['upload_url']

# Загрузка фото на сервер ВК
def upload_photo_to_server(url_server, photo_url):
    # скачиваем фотку с сайта по URL
    photo_load = urllib.request.urlopen(photo_url).read()
    out = open(image_name, "wb")
    out.write(photo_load)
    out.close()

    # Открываем скачанное фото и передаем на сервер ВК
    photo_file = {'file1': open(image_name, 'rb')}
    r = requests.post(url_server, files=photo_file).json()

    # write_json(r, 'upload_photo.json')
    return r

# Сохранение фото в альбоме сообщества
def save_photo(data, caption):
    r = requests.get(url_save_photo, params={'access_token': token,
                                             'album_id': data['aid'],
                                             'group_id': data['gid'],
                                             'server': data['server'],
                                             'photos_list': data['photos_list'],
                                             'hash': data['hash'],
                                             'caption': caption})
    # write_json(r, 'save_photo.json')

def main():
    print('file: vk_photos_load')

if __name__ == '__main__':
    main()