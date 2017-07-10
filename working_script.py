import vk_photos_load

# region PEREMEN
# For ALBUM
title_alb1 = 'Альбом1'
title_alb2 = 'Альбом2'
about_alb1 = 'Описание альбома1'
about_alb2 = 'Описание альбома2'
titles_alb = [title_alb1, title_alb2]
abouts_alb = [about_alb1, about_alb2]

# For PHOTOS
url_img1 = 'ссылка на картинку1'
url_img2 = 'ссылка на картинку2'
about_img1 = 'картинка1'
about_img2 = 'картинка2'
urls_img1 = [url_img1, url_img2]
abouts_img1 = [about_img1, about_img2]

url_img3 = 'ссылка на картинку3'
url_img4 = 'ссылка на картинку4'
about_img3 = 'картинка3'
about_img4 = 'картинка4'
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
