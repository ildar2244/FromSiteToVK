import requests
import json
import urllib.request
import PIL
from my_data import MyVkData
from PIL import Image

# Временные Переменные
title_album = 'Корсеты ортопедические'

# Переменные
token = MyVkData.get_token()
group_id = 141917296
name_img_album = 'market_album.jpg'     # фото обложки
name_img_market = 'market_photo.jpg'    # фото товара
url_album_photo = ''

# Методы ВК API для Подборки Товаров
dev_create_album = MyVkData.API_URL + 'market.addAlbum'
dev_upload_server_album = MyVkData.API_URL + 'photos.getMarketAlbumUploadServer'
dev_save_photo_album = MyVkData.API_URL + 'photos.saveMarketAlbumPhoto'

# Создание и запись данных в файл json-формата
def write_json(data, filename):
    with open(filename, 'w') as file_json:
        json.dump(data, file_json, indent=2, ensure_ascii=False)

# Получаем id новой подборки товаров: создаем её и добавляем обложку
def get_id_new_album_market(photo_album_url):
    upload_data = load_market_album_image(photo_album_url)      # 1.Загружаем фото обложки
    photo_id = save_market_album_image(upload_data)             # 2.Сохраняем обложку
    data_response = add_market_album(photo_id)                  # 3.Создаем подборку под обложку
    pid = data_response['response']['market_album_id']
    return pid

# Создание новой Подборки Товаров
def add_market_album(photo_id):
    owner_id = -group_id
    r = requests.get(dev_create_album, params={'access_token': token,
                                               'owner_id': owner_id,
                                               'title': title_album,
                                               'photo_id': photo_id,
                                               'main_album': 0}).json()
    write_json(r, 'market_album.json')
    return r

# Получение URL-сервера загрузки фото Подборки
def get_market_url_upload_server():
    r = requests.get(dev_upload_server_album, params={'access_token': token,
                                                      'group_id': group_id}).json()
    write_json(r, 'market_album_url.json')
    return r['response']['upload_url']

# Загрузка фото Подборки на ВК-сервер
def load_market_album_image(photo_url):
    # Получение URL ВК-сервера
    url_load = get_market_url_upload_server()
    # скачиваем фотку с сайта по URL
    photo_load = urllib.request.urlopen(photo_url).read()
    out = open(name_img_album, "wb")
    out.write(photo_load)
    out.close()

    # Открываем скачанное фото, проверяем на требования и передаем на сервер ВК
    photo_file = resize_photo(name_img_album)
    r = requests.post(url_load, files=photo_file).json()
    write_json(r, 'market_load_album_image.json')
    return r

# Сохранение фото Подборки как обложки
def save_market_album_image(data):
    r = requests.get(dev_save_photo_album, params={'access_token': token,
                                                   'group_id': group_id,
                                                   'photo': data['photo'],
                                                   'server': data['server'],
                                                   'hash': data['hash']}).json()
    write_json(r, 'market_save_album_image.json')
    response_json = r['response']
    pid = response_json[0]['pid']
    return pid

# Проверка фото на ВК-требования
def resize_photo(file_image):
    old_image = Image.open(file_image)
    width, height = old_image.size
    check_width = 1280

    if width < check_width:
        ratio = (check_width / float(old_image.size[0]))
        height = int((float(old_image.size[1]) * float(ratio)))
        new_image = old_image.resize((check_width, height), PIL.Image.ANTIALIAS)
        new_image.save(name_img_album)

    return {'file': open(name_img_album, 'rb')}

def main():
    # Создание Подборки в Товарах
    alb_pid = get_id_new_album_market(url_album_photo)
    print(alb_pid)
    print('file: vk_market_load')

if __name__ == '__main__':
    main()