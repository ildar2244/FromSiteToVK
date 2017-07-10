import vk_photos_load

# region PEREMEN
# For ALBUM
title_alb1 = 'Ортезы на бедро'
title_alb2 = 'Наколенники'
about_alb1 = 'Приспособления для стопы; Голеностопы. Легкая степень фиксации; Голеностопы. Полужесткая фиксация; Голеностопы. Жесткая фиксация'
about_alb2 = 'Наколенники. Легкая фиксация; Наколенники. Полужесткая фиксация; Наколенники. Жесткая фиксация'
titles_alb = [title_alb1, title_alb2]
abouts_alb = [about_alb1, about_alb2]

# For PHOTOS
url_img1 = 'http://www.dobrota.ru//UserFiles/Image/new2/img2072_20109s.jpg'
url_img2 = 'http://www.dobrota.ru//UserFiles/Image/img2071_31515s.jpg'
about_img1 = 'Эластичный бурсопротектор Altis Plus - 999руб'
about_img2 = 'Эластичная лента для отведения первого пальца стопы - 1999руб'
urls_img1 = [url_img1, url_img2]
abouts_img1 = [about_img1, about_img2]

url_img3 = 'http://www.dobrota.ru//UserFiles/Image/img9339_39867s.jpg'
url_img4 = 'http://www.dobrota.ru//UserFiles/Image/new1/img2019_54578s.jpg'
about_img3 = 'Наколенник ортопедический согревающий легкой фиксации П-0802 - 369руб'
about_img4 = 'Наколенник эластичный КОЛЭ-АЛЕФ - 419руб'
urls_img3 = [url_img3, url_img4]
abouts_img3 = [about_img3, about_img4]

array_img_urls = [urls_img1, urls_img3]
array_img_caption = [abouts_img1, abouts_img3]
# endregion

# Преобразование ссылки рисунка для скачивания бОльшего размера
def change_url_img(old_url):
    new_url = old_url[:-5] + '_big.jpg'
    return new_url

# Создание фотоальбома и загрузка фоток в ВК-сообщество
def load_to_vk_album():
    #TODO: надо добавить параметры в метод, чтоб принимал 4 списка
    for i in range(len(titles_alb)):
        url_upload = vk_photos_load.get_upload_server(titles_alb[i], abouts_alb[i])
        photos_url = array_img_urls[i]
        photos_cap = array_img_caption[i]

        print('ALBUM' + str(i))

        for y in range(len(photos_url)):
            photo_url = change_url_img(photos_url[y])
            upload_data = vk_photos_load.upload_photo_to_server(url_upload, photo_url)
            vk_photos_load.save_photo(upload_data, photos_cap[y])
            print('IMAGE' + str(y))
    print('FINISH: load_to_vk_album')

if __name__ == '__main__':
    print('FINISH: main')
